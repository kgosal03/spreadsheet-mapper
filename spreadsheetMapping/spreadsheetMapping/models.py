from django.db.models import Model, FloatField, TextField, CharField, IntegerField
class Sites(Model):
    latitude = FloatField()
    longitude = FloatField()
    region = CharField(max_length=32, blank=True, null=True)
    name = TextField()
    code = CharField(max_length=32, unique=True, db_index=True)
    c_dates = TextField(blank=True, null=True)
    card_analogue = IntegerField(blank=True, null=True)
    dating_notes = TextField(blank=True, null=True)
    dating_ref = TextField(blank=True, null=True)
