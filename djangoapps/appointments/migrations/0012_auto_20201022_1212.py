# Generated by Django 3.0.7 on 2020-10-22 12:12

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0011_auto_20201022_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='secondary_description',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
