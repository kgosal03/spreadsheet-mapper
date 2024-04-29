# Generated by Django 5.0.4 on 2024-04-29 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spreadsheetMapping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.CharField(max_length=20, verbose_name='Number'),
        ),
    ]
