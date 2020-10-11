from django.urls import path
from . import views

urlpatterns = [
    path("", views.helloworld, name='helloworld'),
    path('signup', views.signup, name='signup'),
    path('looking/', views.api_root, name='looking')
]