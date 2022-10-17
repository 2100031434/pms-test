from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('profile/', views.profile, name="profile"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('products/', views.products, name="products"),
    path('managers/<str:id>', views.managers, name="managers"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('service/', views.service, name="service"),
]