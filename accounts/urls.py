from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^register/$', views.register_view, name='signup_view'),
	url(r'^login/$', views.login_view, name='signup_view'),
	url(r'^auth/$', views.auth_view, name='auth_view'),
	url(r'^signup/$', views.signup_view, name='signup'),
	url(r'^logout/$', views.logout_view, name='logout'),
]