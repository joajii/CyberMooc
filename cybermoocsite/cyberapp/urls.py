from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='login_view'),
    path('admin/', views.admin_access, name='admin_access'),
    path('unvalidated-redirect/', views.unvalidated_redirect, name='unvalidated_redirect'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
