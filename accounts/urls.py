from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('api/user/current', views.userprofile_detail_view),
    path('api/user/edit/<int:user>', views.userprofile_create_view.as_view()),
    

]
