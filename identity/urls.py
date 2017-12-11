from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^me', views.my_identity_view),
	url(r'^create_identity', views.create_identity_view),
	url(r'^', views.main, name='main'),
]
