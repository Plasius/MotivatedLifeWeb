from django.conf.urls import url
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from . import views

urlpatterns = [
	url(r'^register/$', views.register_view, name='signup_view'),
	url(r'^login/$', views.login_view, name='signup_view'),
	url(r'^auth/$', views.auth_view, name='auth_view'),
	url(r'^signup/$', views.signup_view, name='signup'),
	url(r'^logout/$', views.logout_view, name='logout'),

	#new
    url(r'^password_reset/$',
        PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),
        name='password_reset'),
    url(r'^password_reset/done/$',
        PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),

    #deals with token
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
        name='password_reset_confirm'),
    #done with token
    url(r'^reset/done/$',
        PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'),
]
