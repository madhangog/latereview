from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index, name = 'user'),
    url(r'^register/', views.UserList.as_view(), name = 'register'),
    url(r'^login/', views.Login.as_view(), name = 'login'),
    url(r'^logout/', views.Logout.as_view(), name ='logout'),
    url(r'^checklogin/', views.CheckLogin.as_view(), name = 'checklogin'),

]