from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/login/$', auth_views.login,
        {'template_name': 'admin/login.html'}),
    url(r'^accounts/logout/$', auth_views.logout),
    url(r'^dashboard/$', views.dashboard, name='dashboard')
]
