# Generated by Django 3.0.7 on 2020-10-16 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0007_auto_20201013_0654'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['sorting_order', 'id']},
        ),
        migrations.AlterModelOptions(
            name='panel',
            options={'ordering': ['sorting_order', 'id']},
        ),
        migrations.AlterModelOptions(
            name='test',
            options={'ordering': ['sorting_order', 'id']},
        ),
        migrations.AlterModelOptions(
            name='timeslot',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='category',
            name='icon_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='category',
            name='main_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='category',
            name='sorting_order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='panel',
            name='sorting_order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='test',
            name='sorting_order',
            field=models.IntegerField(default=0),
        ),
    ]