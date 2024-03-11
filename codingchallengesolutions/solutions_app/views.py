from rest_framework import generics
from django.db.models import Q
from .models import Solution
from .models import Company
from .serializers import SolutionSerializer
from .serializers import CompanySerializer

class SolutionsList(generics.ListAPIView):
    serializer_class = SolutionSerializer

    from django.db.models import Q

class SolutionsList(generics.ListAPIView):
    serializer_class = SolutionSerializer

    def get_queryset(self):
        """
        Optionally filters the solutions by the given 'language', 'companies', and 'difficulty'
        parameters in the URL.
        """
        queryset = Solution.objects.all()
        language = self.request.query_params.get('language', None)
        companies = self.request.query_params.getlist('companies', None)  
        difficulty = self.request.query_params.get('difficulty', None)

        if language:
            queryset = queryset.filter(programming_languages__name__iexact=language)
        if companies:
            queryset = queryset.filter(companies__name__in=companies).distinct()
        if difficulty:
            queryset = queryset.filter(difficulty__iexact=difficulty)

        return queryset

class CompanyList(generics.ListAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        """
        Optionally filters the solutions by the given 'language', 'companies', and 'difficulty'
        parameters in the URL.
        """
        queryset = Company.objects.all()
        return queryset
