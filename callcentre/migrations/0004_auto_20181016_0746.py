# Generated by Django 2.1.1 on 2018-10-16 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callcentre', '0003_incident'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='incident_department',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AddField(
            model_name='incident',
            name='incident_status',
            field=models.BooleanField(default=False),
        ),
    ]
