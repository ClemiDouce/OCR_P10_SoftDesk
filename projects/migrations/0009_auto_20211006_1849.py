# Generated by Django 3.2.8 on 2021-10-06 16:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0008_alter_project_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commentaire',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Issues',
            new_name='Issue',
        ),
    ]
