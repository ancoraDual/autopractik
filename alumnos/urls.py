from django.conf.urls import patterns, include, url

urlpatterns = patterns('',


	url(r'^$', 'alumnos.views.alumnos_index', name='alumnos_index'),
	url(r'^logout/', 'alumnos.views.alumnos_logout', name='alumnos_logout'),
	# url(r'^upload/', 'alumnos.views.alumnos_upload', name='alumnos_upload'),
	url(r'^dashboard/', 'alumnos.views.alumnos_dashboard', name='alumnos_dashboard'),


	url( r'uploading/', 'alumnos.views.uploading', name = 'uploading' ),
	url( r'upload/', 'alumnos.views.upload', name = 'jfu_upload' ),
    url( r'delete/(?P<pk>\d+)$', 'alumnos.views.delete', name = 'jfu_delete' ),
	
)