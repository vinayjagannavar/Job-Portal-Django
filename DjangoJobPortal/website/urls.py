from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('job-listing/', views.job_listings, name= "job-listing"),
    path('job-details/<int:pk>', views.job_details, name= "job-details"),
]