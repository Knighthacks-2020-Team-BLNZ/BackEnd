from django.urls import path
from . import views

urlpatterns = [
    path("", views.helloworld, name='helloworld'),
    path('api/hello/', views.account, name='account'),
    path('signup', views.signup, name='signup'),
    path('your-name/', views.signup, name='your-name'),
    path('thanks/', views.thanks, name='thanks'),
    path('findusers', views.getusers, name='findusers'),
    path('looking/', views.getusers, name='looking')
]