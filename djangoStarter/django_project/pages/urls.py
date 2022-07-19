# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('people/', views.PersonList, name="people"),
    path('people/<str:personid>', views.PersonDetail, name="person"),
    path('create/', views.CreatePerson, name="createperson")
]