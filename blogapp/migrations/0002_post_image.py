# Generated by Django 2.2.4 on 2020-08-25 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='berlin.jpg', upload_to=''),
        ),
    ]
