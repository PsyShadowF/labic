# Generated by Django 4.2.1 on 2023-05-16 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_articles_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='cover',
            field=models.ImageField(default='uploads/default.png', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='description',
            field=models.TextField(default='', max_length=424),
        ),
    ]
