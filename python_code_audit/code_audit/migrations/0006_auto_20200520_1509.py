# Generated by Django 2.2.6 on 2020-05-20 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('code_audit', '0005_file_filext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='auther',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='文件所属'),
        ),
    ]
