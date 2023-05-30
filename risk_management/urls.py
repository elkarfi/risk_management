from django.urls import path
from . import views

urlpatterns = [
  
  path('login/', views.login_page, name="login"),
  path('logout/',views.logout_employee, name="logout"),
  path('home/', views.home, name="home"),
  path('create-risk', views.create_risk, name="create-risk"),
  path('update_risk/<str:pk>/', views.update_risk, name="update_risk"),
  path('delete_risk/<str:pk>/', views.delete_risk, name="delete_risk"),
  path('create_department', views.create_department, name="create_department"),
  path('delete_department/<str:pk>/', views.delete_department, name="delete_department"),
  path('view_department/', views.view_department, name="view_department"),
  path('create_employee', views.create_employee, name="create_employee"),
  path('update_employee/<str:pk>/', views.update_employee, name="update_employee"),
  path('delete_employee/<str:pk>/', views.delete_employee, name="delete_employee"),
  path('view_employee/', views.view_employee, name="view_employee"),


]
