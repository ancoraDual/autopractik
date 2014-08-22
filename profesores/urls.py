from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^$', 'profesores.views.index', name='profesores_index'),

)