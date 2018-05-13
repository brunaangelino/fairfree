from django.urls import path

from fair import views

urlpatterns = [
    path('', views.home),
]

