# Generated by Django 2.1.1 on 2018-10-04 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('callcentre', '0002_delete_incident'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_time', models.CharField(max_length=100)),
                ('incident_location', models.CharField(max_length=100)),
                ('incident_category', models.CharField(max_length=100)),
                ('incident_description', models.CharField(max_length=400)),
            ],
        ),
    ]
