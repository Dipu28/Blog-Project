# Generated by Django 2.2.4 on 2020-08-27 03:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
