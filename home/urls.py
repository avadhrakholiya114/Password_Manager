from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add_password/', views.add_password, name='add_pass'),
    path('manage_password/', views.manage, name='manage_password'),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update),
]
