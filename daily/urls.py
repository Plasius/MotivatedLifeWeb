from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
	url(r'^dashboard/$', views.dashboard, name='dashboard_view'),
    url(r'^favorite/$', views.favorite, name='favorite_view'),
]
