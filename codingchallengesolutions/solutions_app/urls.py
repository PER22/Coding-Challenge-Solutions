from django.urls import path
from . import views

urlpatterns = [
    path('v1/solutions', views.SolutionsList.as_view(), name='solution_list')
]
