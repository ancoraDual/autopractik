from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from .forms import AlumnoAuthForm


def alumnos_index(request):	

	form = AlumnoAuthForm(request.POST or None)
	
	if form.is_valid():
		
		user = form.get_user()
	
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse('alumnos_dashboard'))
		else:
			return render(request, 'alumnos_index.html', {'form': form})
	
	return render(request, 'alumnos_index.html', {'form': form})


def alumnos_logout(request):	
	
	logout(request)
	return HttpResponseRedirect(reverse('alumnos_index'))

@login_required
def alumnos_dashboard(request):	
	return render (request, 'alumnos_dashboard.html') 


import os
from django.conf import settings
from django.views import generic
from django.views.decorators.http import require_POST
from jfu.http import upload_receive, UploadResponse, JFUResponse

from .models import Foto
from autoescuelas.models import Autoescuela

def uploading(request):    
    
    return render (request, 'upload.html', {'fk': '2'}) 


@require_POST
def upload( request ):

    # The assumption here is that jQuery File Upload
    # has been configured to send files one at a time.
    # If multiple files can be uploaded simulatenously,
    # 'file' may be a list of files.
    file = upload_receive( request )

    autoescuela = Autoescuela.objects.get( pk = request.POST.get('fk') )
    instance = Foto( nombre = "la foto", foto = file, autoescuela = autoescuela )
    instance.save()

    basename = os.path.basename( instance.foto.path )

    file_dict = {
        'name' : basename,
        'size' : file.size,

        'url': settings.MEDIA_URL + basename,
        'thumbnailUrl': settings.MEDIA_URL + basename,

        'deleteUrl': reverse('jfu_delete', kwargs = { 'pk': instance.pk }),
        'deleteType': 'POST',
    }

    return UploadResponse( request, file_dict )

@require_POST
def delete( request, pk ):
    success = True
    try:
        instance = Foto.objects.get( pk = pk )
        os.unlink( instance.file.path )
        instance.delete()
    except Foto.DoesNotExist:
        success = False

    return JFUResponse( request, success )
