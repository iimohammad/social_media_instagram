# Generated by Django 4.2 on 2024-03-23 08:39

import content.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hashtag',
            field=models.CharField(blank=True, max_length=30, validators=[
                                   content.validators.validate_hashtag]),
        ),
        migrations.DeleteModel(
            name='Hashtag',
        ),
    ]
