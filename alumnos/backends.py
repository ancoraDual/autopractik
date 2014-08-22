from django.contrib.auth.models import User

class AlumnoAuthBackend(object):
	def authenticate(self, email = None, nombre = None):
		
		try:
			return User.objects.get(username = nombre, email = email)

		except User.DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			return User.objects.get(id = user_id)

		except User.DoesNotExist:
			return None