# Generated by Django 4.2 on 2024-03-23 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0004_remove_post_file_remove_post_hashtag_storycontent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[
                 ('like', 'Like'), ('dislike', 'Dislike')], max_length=10)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='reactions', to='content.post')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'post')},
            },
        ),
    ]