from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
	"""Um assunto sobre o qual o usuário está aprendendo"""
	text = models.CharField(max_length=200)
	date_add = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	# def __init__(self, arg):
	#	super(Topic, self).__init__()
	#	self.arg = arg


	def __str__(self):
		"""Um assunto sobre o qual o usuário está aprendendo"""
		return self.text

class Entry(models.Model):
    """Algo específico aprendido sobre o assunto"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # Adicione on_delete
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.text[:50] + "..."