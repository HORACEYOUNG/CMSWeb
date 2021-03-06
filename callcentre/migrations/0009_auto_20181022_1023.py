# Generated by Django 2.0.9 on 2018-10-22 02:23

from django.db import migrations, models
import utilities.incidenttype
import utilities.region


class Migration(migrations.Migration):

    dependencies = [
        ('callcentre', '0008_remove_incident_incident_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='incident_category',
            field=models.CharField(choices=[(utilities.incidenttype.IncidentType('Emergency Ambulance'), 'Emergency Ambulance'), (utilities.incidenttype.IncidentType('Rescue & Evacuation'), 'Rescue & Evacuation'), (utilities.incidenttype.IncidentType('Fire Fighting'), 'Fire Fighting'), (utilities.incidenttype.IncidentType('Gas Leak Control'), 'Gas Leak Control')], default='NULL', max_length=100),
        ),
        migrations.AddField(
            model_name='incident',
            name='incident_department',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AddField(
            model_name='incident',
            name='incident_description',
            field=models.CharField(default='NULL', max_length=400),
        ),
        migrations.AddField(
            model_name='incident',
            name='incident_region',
            field=models.CharField(choices=[(utilities.region.Region('South West'), 'South West'), (utilities.region.Region('North West'), 'North West'), (utilities.region.Region('Central Singapore'), 'Central Singapore'), (utilities.region.Region('South East'), 'South East'), (utilities.region.Region('North East'), 'North East')], default='NULL', max_length=100),
        ),
    ]
