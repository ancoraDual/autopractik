from ajaxuploader.backends.base import AbstractUploadBackend
from django.conf import settings

class UploadBackend(AbstractUploadBackend):
    """
    Uses Django's default storage backend to store the uploaded files
    see https://docs.djangoproject.com/en/dev/topics/files/#file-storage
    """

    UPLOAD_DIR = getattr(settings, "UPLOAD_DIR", "uploads")

    def _get_upload_dir(self):
        if callable(self.UPLOAD_DIR):
            return self.UPLOAD_DIR()
        return datetime.datetime.now().strftime(self.UPLOAD_DIR)


    def upload_chunk(self, chunk, *args, **kwargs):
        print 'chunk'
        self._dest.write(chunk)

    def upload_complete(self, request, filename, *args, **kwargs):
        print 'complete'
        self._dest.close()
        print 'ret'
        return {"path": self.path}