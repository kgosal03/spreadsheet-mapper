from django.db.models import Model, CharField

class Contact(Model):
    name = CharField(max_length=255)
    number = CharField(max_length=20)
    address = CharField(max_length=255)

    class SpreadsheetMeta:
        columns = {
            'name': 'A',
            'number': 'B',
            'address': 'C'
        }

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name