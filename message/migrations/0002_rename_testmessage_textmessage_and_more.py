# Generated by Django 4.2 on 2024-03-23 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TestMessage',
            new_name='TextMessage',
        ),
        migrations.AlterField(
            model_name='imagemessage',
            name='image',
            field=models.ImageField(upload_to='message_photos/'),
        ),
    ]
