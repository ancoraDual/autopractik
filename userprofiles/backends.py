from django.contrib.auth.models import User

class EmailBackend(object):
	def authenticate(self, email = None, nombre = None):
		
		user = User.objects.get(username = nombre, email = email)
		return user

	def get_user(self, user_id):
		try:
			return User.objects.get(id = user_id)

		except User.DoesNotExist:
			return None
