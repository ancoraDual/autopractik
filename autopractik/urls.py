from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from autoescuelas.urls import url
from alumnos.urls import url
from profesores.urls import url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/', 'userprofiles.views.signup', name="signup"),
    url(r'^signin/', 'userprofiles.views.signin', name="signin"),
    url(r'^bienvenido/', 'userprofiles.views.bienvenido', name="bienvenido"),

    url(r'^autoescuelas/', include('autoescuelas.urls')),
    url(r'^alumnos/', include('alumnos.urls')),
    url(r'^profesores/', include('profesores.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += patterns('',
    url(r'^$', 'autopractik.views.home', name='home'),
)
