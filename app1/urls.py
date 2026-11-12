from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"), 
    path("logout/", views.logout_auth, name="logout"),
    path("login/", views.login_auth, name="login"),
    path("service/", views.service, name="service"),
    path("service_list/", views.service_list, name="service_list"),
]