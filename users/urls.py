from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index, name = 'user'),
    url(r'^registerUser/', views.UserList.as_view(), name = 'registerUser'),
    url(r'^registerAdmin/', views.CriticList.as_view(), name = 'registerAdmin'),
    url(r'^login/', views.Login.as_view(), name = 'login'),
    url(r'^logout/', views.Logout.as_view(), name ='logout'),
    url(r'^checklogin/', views.CheckLogin.as_view(), name = 'checklogin'),
    url(r'^', views.index, name = 'index'),
]