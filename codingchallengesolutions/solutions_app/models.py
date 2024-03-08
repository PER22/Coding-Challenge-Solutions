from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProgrammingLanguage(models.Model):
    LANGUAGE_CHOICES = [
        ('cpp', 'CPP'),
        ('java', 'Java'),
        ('python', 'Python'),
    ]
    name = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)  # Added max_length

    def __str__(self):
        return self.get_name_display()  # This returns the human-readable name for the choice


class Solution(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    

    title = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=6, choices=DIFFICULTY_CHOICES, default='easy')
    companies = models.ManyToManyField(Company, related_name='solutions')
    programming_languages = models.ManyToManyField(ProgrammingLanguage, related_name='solutions') 
    site = models.CharField(max_length=100)
    url = models.URLField(null=True, blank=True)

    python_runtime = models.FloatField(null=True, blank=True)
    python_solution = models.CharField(max_length=255, blank=True, null=True)

    cpp_runtime = models.FloatField(null=True, blank=True)
    cpp_solution = models.CharField(max_length=255, blank=True, null=True)
    
    java_runtime = models.FloatField(null=True, blank=True)
    java_solution = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.title
