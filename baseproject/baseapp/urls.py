
from xml.etree.ElementInclude import include
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
   path("",views.demo,name="demo"),
   # path("about/",views.login,name="login"),
    #path("deatils/",views.tables,name="tables"),
    #path("Thanks/",views.Thanks,name="Thanks"),
    #path("name",views.pass_val,name="Pass_val"),
    #path("add/",views.addition,name="addition")

]
