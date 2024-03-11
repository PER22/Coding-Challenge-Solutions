from django.urls import path
from . import views

urlpatterns = [
    path('solutions', views.SolutionsList.as_view(), name='solution_list'),
    path('companies', views.CompanyList.as_view(), name='company_list'),
]
