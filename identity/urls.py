from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^me', views.my_identity_view, name='me'),
	url(r'^create_identity', views.create_identity_view, name='create_identity'),
	url(r'^make_identity', views.make_identity_view, name='make_identity'),
	url(r'^', views.main, name='main'),
]
