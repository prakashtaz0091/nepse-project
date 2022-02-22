from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path("superuser/",views.superUser,name="superuser"),
    path("update/",views.update,name="update"),
    path("logoutUser/",views.logoutUser,name="logout"),
]