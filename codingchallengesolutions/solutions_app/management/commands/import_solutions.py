# import_solutions.py
import os
import json
import fnmatch
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import transaction
from solutions_app.models import Solution, Company, ProgrammingLanguage

class Command(BaseCommand):
    help = 'Import solution files and metadata into the database.'

    def add_arguments(self, parser):
        parser.add_argument('solutions_dir', type=str, help='Path to the directory containing solution folders.')

    def handle(self, *args, **options):
        solutions_dir = options['solutions_dir']
        self.import_solutions(solutions_dir)

    @transaction.atomic
    def import_solutions(self, solutions_dir):
        for subdir, dirs, files in os.walk(solutions_dir):
            if 'info.json' in files:
                self.import_solution(subdir)

    def import_solution(self, solution_dir):
        info_path = os.path.join(solution_dir, 'info.json')
        with open(info_path, 'r') as info_file:
            data = json.load(info_file)

        # Create or update the Solution instance
        solution = Solution(
            title=data.get('title'),
            difficulty=data.get('difficulty'),
            site=data.get('site'),
            url=data.get('url') or '',
            python_runtime=data.get('python_runtime'),
            python_solution=self.find_file(solution_dir, '*.py'),
            cpp_runtime=data.get('cpp_runtime'),
            cpp_solution=self.find_file(solution_dir, '*.cpp'),
            java_runtime=data.get('java_runtime'),
            java_solution=self.find_file(solution_dir, '*.java'),
        )
        solution.save()

        # Handling companies
        for company_name in data.get('companies', []):
            company, _ = Company.objects.get_or_create(name=company_name)
            solution.companies.add(company)

        # Automatically determining programming languages
        self.add_programming_languages(solution, solution_dir)

        solution.save()
        print(f'Imported solution: {solution.title}')

    def find_file(self, directory, pattern):
        for filename in os.listdir(directory):
            if fnmatch.fnmatch(filename, pattern):
                relative_path = os.path.join(directory.replace(str(settings.MEDIA_ROOT), '').lstrip('/'), filename)
                return relative_path
        return None

    def add_programming_languages(self, solution, solution_dir):
        programming_languages = {
            'Python': ('*.py', solution.python_solution),
            'C++': ('*.cpp', solution.cpp_solution),
            'Java': ('*.java', solution.java_solution),
        }
        for lang_code, (pattern, solution_path) in programming_languages.items():
            if solution_path:
                lang, _ = ProgrammingLanguage.objects.get_or_create(name=lang_code)
                solution.programming_languages.add(lang)

if __name__ == "__main__":
    Command().handle()
