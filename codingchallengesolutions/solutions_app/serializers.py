from rest_framework import serializers
from .models import Solution, Company, ProgrammingLanguage


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name']

class ProgrammingLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = ['name']

class SolutionSerializer(serializers.ModelSerializer):
    companies = CompanySerializer(many=True, read_only=True)
    programming_languages = ProgrammingLanguageSerializer(many=True, read_only=True)

    class Meta:
        model = Solution
        fields = [ 'title', 'difficulty', 'companies', 'programming_languages', 'site', 'url', 'python_runtime', 'python_solution', 'cpp_runtime', 'cpp_solution', 'java_runtime', 'java_solution']
