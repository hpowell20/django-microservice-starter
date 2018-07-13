from django.urls import path
from . import views

urlpatterns = [
    path(r'random-facts', views.RandomFactsView.as_view(), name='random-facts')
]