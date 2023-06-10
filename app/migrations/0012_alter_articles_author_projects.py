# Generated by Django 4.2.1 on 2023-05-18 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_articles_author_alter_extenduser_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(default='posts/default.png', upload_to='posts/')),
                ('title', models.CharField(default='Untitled', max_length=255)),
                ('description', models.TextField(default='')),
                ('markdownFile', markdownx.models.MarkdownxField()),
                ('project_status', models.IntegerField(choices=[(0, 'Private'), (1, 'Public')], default=0)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
