# Generated by Django 3.2 on 2022-04-04 08:48

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universeinfotech_app', '0019_career_job_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='job_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
