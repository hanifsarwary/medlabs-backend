# Generated by Django 3.0.7 on 2020-10-06 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_auto_20200923_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
    ]