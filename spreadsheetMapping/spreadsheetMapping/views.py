from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.apps import apps
import pandas as pd
from python_calamine import CalamineWorkbook

def upload_spreadsheet(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        return ingest_spreadsheet(request, uploaded_file)
    return render(request, 'upload.html')

def ingest_spreadsheet(request, uploaded_file):
    model_names = [
        model.__name__ 
        for model in apps.get_models()
    ]
    
    Model = apps.get_model(app_label="spreadsheetMapping", model_name=model_names[-1])

    workbook = CalamineWorkbook.from_filelike(uploaded_file)
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
    return render(request, 'success.html')
