# Generated by Django 3.2.7 on 2021-10-05 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='contributors',
        ),
        migrations.AddField(
            model_name='contributor',
            name='permissions',
            field=models.CharField(choices=[('restricted', 'Contributor'), ('all', 'Author')], default='restricted', max_length=20),
        ),
        migrations.AddField(
            model_name='contributor',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.project'),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='roles',
            field=models.CharField(choices=[('author', 'Author'), ('responsable', 'Responsable'), ('contributor', 'Contributor')], default='contributor', max_length=20),
        ),
        migrations.RemoveField(
            model_name='contributor',
            name='user',
        ),
        migrations.AddField(
            model_name='contributor',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issues',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('mid', 'Middle'), ('high', 'High')], default='low', max_length=12),
        ),
        migrations.AlterField(
            model_name='issues',
            name='status',
            field=models.CharField(choices=[('todo', 'To Do'), ('inprogress', 'In Progress'), ('done', 'Done')], default='todo', max_length=20),
        ),
        migrations.AlterField(
            model_name='issues',
            name='tag',
            field=models.CharField(choices=[('bug', 'Bug'), ('amelioration', 'Amelioration'), ('tache', 'Tache')], default='bug', max_length=12),
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.TextField(choices=[('back', 'Back-end'), ('front', 'Front-end'), ('ios', 'iOS'), ('android', 'Android')], default='back'),
        ),
    ]
