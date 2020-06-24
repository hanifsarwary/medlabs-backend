# Generated by Django 3.0.7 on 2020-06-21 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_create_appointment_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='appointment',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]