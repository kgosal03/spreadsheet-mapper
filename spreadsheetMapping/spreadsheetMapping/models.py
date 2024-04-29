from django.db.models import Model, CharField
class Contact(Model):
    name = CharField(max_length=255)
    number = CharField(max_length=20)
    address = CharField(max_length=255)
