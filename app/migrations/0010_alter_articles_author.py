# Generated by Django 4.2.1 on 2023-05-17 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_extenduser_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
