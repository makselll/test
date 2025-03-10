# Generated by Django 3.0 on 2020-01-19 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acc', '0002_remove_document_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doc_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='static/documents', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='document',
            name='private',
            field=models.BooleanField(null=True),
        ),
    ]
