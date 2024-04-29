from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
import pandas as pd

def upload_spreadsheet(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        return ingest_spreadsheet(request, uploaded_file)
    return render(request, 'upload.html')

def ingest_spreadsheet(request, uploaded_file):
    df = pd.read_excel(uploaded_file)
    headers = df.columns.tolist()
    
    for _, row in df.iterrows():
        # Map spreadsheet columns to model fields using verbose names
        contact_data = {
            'name': row['Name'],
            'number': row['Number'],
            'address': row['Address']
        }
        # Create Contact instances using the mapped data
        contact = Contact(**contact_data)
        # Perform any further actions with the Contact instance
        contact.save() # Save the Contact to the database, for example
    return render(request, 'success.html')
