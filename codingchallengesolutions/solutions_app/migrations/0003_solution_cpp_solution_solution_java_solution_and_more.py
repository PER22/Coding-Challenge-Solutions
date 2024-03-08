# Generated by Django 5.0.3 on 2024-03-07 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions_app', '0002_rename_languages_solution_programming_languages'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='cpp_solution',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='java_solution',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='python_solution',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
