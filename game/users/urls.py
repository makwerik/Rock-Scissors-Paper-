from django.urls import path
from .views import *

urlpatterns = [
    path('', show_results, name='show_results')
]