# Generated by Django 3.2.8 on 2021-10-14 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0011_auto_20211014_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_author', to=settings.AUTH_USER_MODEL),
        ),
    ]
