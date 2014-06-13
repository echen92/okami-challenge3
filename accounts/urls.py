from django.conf.urls import patterns, url

import views


urlpatterns = patterns('',
                       url(r'^add', views.add_user, name='add_user'),
                       url(r'^delete', views.delete_user, name='delete_user'),
                       url(r'^edit', views.edit_user, name='edit_user'),
)
