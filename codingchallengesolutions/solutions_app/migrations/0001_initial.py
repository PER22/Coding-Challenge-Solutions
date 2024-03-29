# Generated by Django 5.0.3 on 2024-03-07 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('cpp', 'C++'), ('java', 'Java'), ('python', 'Python')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('difficulty', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default='easy', max_length=6)),
                ('py_runtime', models.FloatField(blank=True, null=True)),
                ('cpp_runtime', models.FloatField(blank=True, null=True)),
                ('java_runtime', models.FloatField(blank=True, null=True)),
                ('site', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True, null=True)),
                ('companies', models.ManyToManyField(related_name='solutions', to='solutions_app.company')),
                ('languages', models.ManyToManyField(related_name='solutions', to='solutions_app.programminglanguage')),
            ],
        ),
    ]
