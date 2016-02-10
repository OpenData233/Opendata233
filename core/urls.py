from django.conf.urls import url, patterns,include

from core import views

urlpatterns = [

 url(r'^$', views.home, name='home'), # this is the projects main landing page
 url(r'^about/',views.about, name='about'),
 url(r'^candidates/', views.candidatebio, name='candidates'),
 url(r'^mahama/',views.mahama, name='mahama'),
 url(r'^nana/', views.nana, name='nana'),
 url(r'^green/', views.greenstreet, name='greenstreet'),
]

