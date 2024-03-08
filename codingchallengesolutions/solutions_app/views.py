from rest_framework import generics
from django.db.models import Q
from .models import Solution
from .serializers import SolutionSerializer

class SolutionsList(generics.ListAPIView):
    serializer_class = SolutionSerializer

    def get_queryset(self):
        """
        Optionally filters the solutions by the given 'language', 'companies', and 'difficulty'
        parameters in the URL.
        """
        queryset = Solution.objects.all()
        language = self.request.query_params.get('language', None)
        company = self.request.query_params.get('companies', None)
        difficulty = self.request.query_params.get('difficulty', None)

        if language:
            queryset = queryset.filter(programming_languages__name__iexact=language)
        if company:
            queryset = queryset.filter(companies__name__iexact=company)
        if difficulty:
            queryset = queryset.filter(difficulty__iexact=difficulty)

        return queryset
