# Generated by Django 5.0.3 on 2024-03-07 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solutions_app', '0003_solution_cpp_solution_solution_java_solution_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solution',
            old_name='py_runtime',
            new_name='python_runtime',
        ),
    ]