# Generated by Django 4.2 on 2024-03-23 03:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='hashtag',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to='content.hashtag'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mention',
            name='post',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name='mentions', to='content.post'),
        ),
        migrations.AddField(
            model_name='mention',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='mention',
            unique_together={('post', 'user')},
        ),
    ]