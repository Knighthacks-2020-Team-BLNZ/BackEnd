from django.urls import path
from . import views

urlpatterns = [
    path("", views.helloworld, name='helloworld'),
    path('api/hello/', views.account, name='account'),
]