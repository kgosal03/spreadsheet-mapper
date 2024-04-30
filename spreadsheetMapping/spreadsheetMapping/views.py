from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.apps import apps
import pandas as pd
from python_calamine import CalamineWorkbook

model_names = [
    model.__name__ 
    for model in apps.get_models()
]

def upload_spreadsheet(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        return ingest_spreadsheet(request, uploaded_file)
    return render(request, 'upload.html')

def ingest_spreadsheet(request, uploaded_file):

    def callback(model_name, workbook):
        Model = apps.get_model(app_label="spreadsheetMapping", model_name=model_name)

        rows = iter(workbook.get_sheet_by_index(0).to_python())
        headers = next(rows)

        model_fields = [ 
            field.name.lower() 
            for field in Model._meta.fields
        ][1:]
        
        for row in rows:
            # Map spreadsheet columns to model fields using verbose names
            contact_data = {
                model_fields[i]: row[i]
                for i in range(len(row))
            }
            # Create Contact instances using the mapped data
            contact = Model(**contact_data)
            # Perform any further actions with the Contact instance
            contact.save() # Save the Contact to the database, for example
    
    workbook = CalamineWorkbook.from_filelike(uploaded_file)
    considering = [
        model_name
        for model_name in model_names
        if model_name in workbook.sheet_names
    ]
    
    for item in considering:
        callback(item, workbook)

    return render(request, 'success.html')

