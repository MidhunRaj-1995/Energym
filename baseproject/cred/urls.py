
from . import views
from django.urls import path

urlpatterns = [
   path("register",views.demo,name="demo"),
   path("login",views.login_user,name="login_user"),
   path("logout",views.logout_user,name="logout_user")

]
