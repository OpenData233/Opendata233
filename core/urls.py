from django.conf.urls import url, patterns,include

from . import views

from feedreader.views import *

urlpatterns = [

 url(r'^$', views.home, name='home'), # this is the projects main landing page
 url(r'^about/',views.about, name='about'),
 url(r'^candidates/', views.candidatebio, name='candidates'),
 url(r'^mahama/',views.mahama, name='mahama'),
 url(r'^nana/', views.nana, name='nana'),
 url(r'^green/', views.greenstreet, name='greenstreet'),
 url(regex=r'^$',
       view=FeedList.as_view(),
       name='feed_list'),
 url(regex=r'^entry_list/$',
       view=EntryList.as_view(),
       name='entry_list'),
 url(regex=r'^num_unread/$',
       view=NumbersUnread.as_view(),
       name='num_unread'),
 url(regex=r'^mark_entry_read/$',
       view=MarkEntryRead.as_view(),
       name='mark_entry_read'),
 url(regex=r'^search/$',
       view=Search.as_view(),
       name='search'),
 url(regex=r'^edit_feeds/$',
       view=EditFeeds.as_view(),
       name='edit_feeds'),
   url(regex=r'^export_opml/$',
       view=ExportOpml.as_view(),
       name='export_opml'),
   url(regex=r'^update/$',
       view=UpdateItem.as_view(),
       name='update_item'),
]

