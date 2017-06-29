from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^sentiment', views.Sentiment, name='Sentiment'),
	url(r'^topviewed', views.TopViewed, name='TopViewed'),
	url(r'^countryviews', views.CountryViews, name='CountryViews'),
	url(r'^channellikes', views.ChannelLikes, name='ChannelLikes'),
	url(r'^categoryuploaded', views.CategoryUploaded, name='CategoryUploaded'),
	url(r'^categorycomments', views.CategoryComments, name='CategoryComments'),
	url(r'^toplikes', views.TopLikes, name='TopLikes'),
	url(r'', views.index, name='index'),
]