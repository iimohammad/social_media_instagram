# Generated by Django 4.2 on 2024-03-23 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_rename_testmessage_textmessage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemessage',
            name='message_ptr',
        ),
        migrations.RemoveField(
            model_name='textmessage',
            name='message_ptr',
        ),
        migrations.AddField(
            model_name='message',
            name='TextContent',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='message',
            name='file',
            field=models.FileField(blank=True, upload_to='message_files/'),
        ),
        migrations.DeleteModel(
            name='AudioMessage',
        ),
        migrations.DeleteModel(
            name='ImageMessage',
        ),
        migrations.DeleteModel(
            name='TextMessage',
        ),
    ]