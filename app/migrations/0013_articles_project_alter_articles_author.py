# Generated by Django 4.2.1 on 2023-05-18 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_articles_author_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.projects'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
