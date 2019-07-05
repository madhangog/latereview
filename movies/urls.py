from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index, name = 'user'),
    url(r'^movies/', views.MovieList.as_view(), name = 'movies'),
    url(r'^review/', views.Reviews.as_view(), name = 'movies'),
   
  ]