from django.contrib import admin

# Register your models here.
from .models import Company
from .models import ProgrammingLanguage
from .models import Solution

admin.site.register(Company)
admin.site.register(ProgrammingLanguage)
admin.site.register(Solution)