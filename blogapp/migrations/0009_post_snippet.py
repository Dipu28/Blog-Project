# Generated by Django 2.2.4 on 2020-08-27 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_auto_20200827_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click the link to read the blog', max_length=255),
        ),
    ]
