from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    
    url(r'^login/', 'autoescuelas.views.logIn', name='logIn'),	
	url(r'^logout/', 'autoescuelas.views.logOut', name='logOut'),

	url(r'^dashboard/', 'autoescuelas.views.dashboard', name='autoescuelas_dashboard'),
	
	url(r'^vehiculos/save/(?P<id>[0-9]+)/', 'autoescuelas.views.vehiculos_save', name='vehiculos_save'),
	url(r'^vehiculos/edit/(?P<id>[0-9]+)/', 'autoescuelas.views.vehiculos_edit', name='vehiculos_edit'),
	url(r'^vehiculos/', 'autoescuelas.views.vehiculos', name='vehiculos_list'),

	url(r'^alumnos/save/(?P<id>[0-9]+)/', 'autoescuelas.views.alumnos_save', name='alumnos_save'),
	url(r'^alumnos/edit/(?P<id>[0-9]+)/', 'autoescuelas.views.alumnos_edit', name='alumnos_edit'),
	url(r'^alumnos/', 'autoescuelas.views.alumnos', name='alumnos_list'),

	url(r'^profesores/save/(?P<id>[0-9]+)/', 'autoescuelas.views.profesores_save', name='profesores_save'),
	url(r'^profesores/edit/(?P<id>[0-9]+)/', 'autoescuelas.views.profesores_edit', name='profesores_edit'),
	url(r'^profesores/', 'autoescuelas.views.profesores', name='profesores_list'),
	
	url(r'^saldos/save/(?P<id>[0-9]+)/', 'autoescuelas.views.saldos_save', name='saldo_save'),
	url(r'^saldos/edit/(?P<id>[0-9]+)/', 'autoescuelas.views.saldos_edit', name='saldo_edit'),
	url(r'^saldos/', 'autoescuelas.views.saldos', name='saldos_list'),

	url(r'^practicas/save/(?P<id>[0-9]+)/', 'autoescuelas.views.practicas_save', name='practicas_save'),
	url(r'^practicas/edit/(?P<id>[0-9]+)/', 'autoescuelas.views.practicas_edit', name='practicas_edit'),
	url(r'^practicas/', 'autoescuelas.views.practicas', name='practicas_list'),

	url(r'^horarios/save/(?P<id>[0-9]+)/', 'autoescuelas.views.horarios_save', name='horarios_save'),
	url(r'^horarios/edit/(?P<id>[0-9]+)/', 'autoescuelas.views.horarios_edit', name='horarios_edit'),
	url(r'^horarios/', 'autoescuelas.views.horarios', name='horarios_list'),
	
	
	url(r'^perfil/', 'autoescuelas.views.perfil', name='autoescuelas_perfil'),
	url(r'^$', 'autoescuelas.views.home', name='home'),
)