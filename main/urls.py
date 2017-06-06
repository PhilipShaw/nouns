from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
    login,
    logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^base/$', views.base, name='base'),
    url(r'^all/$', views.all, name='all'),
    url(r'^about_loggedin/$', views.about, name='about_loggedin'),
    url(r'^user_description/$', views.description_edit, name='user_description'),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^create', views.create, name='create'),
    url(r'^userhome/$', views.userhome, name='userhome'),
    url(r'^people/$', views.people, name='people'),
    url(r'^userhome/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    url(r'^userhome/user_edit/$', views.user_edit, name='user_edit'),
    url(r'^userhome/password/$', views.change_password, name='change_password'),
    url(r'^password_retry/$', views.change_password_retry, name='change_password_retry'),
    url(r'^reset_password/$', password_reset, {'template_name': 'reset_password.html',
    'post_reset_redirect': 'main:password_reset_done',
    'email_template_name': 'reset_password_email.html'}, name='reset_password'),
    url(r'^reset_password/done/$', password_reset_done, {'template_name': 'reset_password_done.html'}, name='password_reset_done'),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
    {'template_name': 'reset_password_confirm.html','post_reset_redirect': 'main:password_reset_complete'}, name='password_reset_confirm'),
    url(r'^reset_password/complete/$', password_reset_complete, {'template_name': 'reset_password_complete.html'}, name='password_reset_complete'),
    url(r'^(?P<noun_id>[0-9]+)/snatch/$', views.snatch, name='snatch'),
    url(r'^(?P<noun_id>[0-9]+)/$', views.nounpage, name='nounpage'),
    url(r'^(?P<id>[0-9]+)/delete/$', views.delete_noun, name='delete_noun'),

]
