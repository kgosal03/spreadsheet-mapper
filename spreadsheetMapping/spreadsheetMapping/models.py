from django.db.models import Model, FloatField, TextField, CharField, IntegerField
class Sites(Model):
    dating_notes = TextField(blank=True, null=True, help_text="H")
    card_analogue = IntegerField(blank=True, null=True, help_text="G")
    longitude = FloatField(help_text="B")
    code = CharField(max_length=32, unique=True, db_index=True, help_text="E")
    dating_ref = TextField(blank=True, null=True, help_text="I")
    latitude = FloatField(help_text="A")
    region = CharField(max_length=32, blank=True, null=True, help_text="C")
    name = TextField(help_text="D")
    c_dates = TextField(blank=True, null=True, help_text="F")
