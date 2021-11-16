from django.db import models
reason_for_email = [
	('greeting', 'Just saying Hi!'),
	('work', "Business"), 
	('ideas', 'Ideas'),
	('hm', 'Hate mail'), 
	('bored', 'Other'),
]
# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	reason = models.CharField(choices=reason_for_email, default ='Just saying Hi!' ,max_length=50)
	subject = models.CharField(max_length=200)
	message = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Contact"

	def __str__(self):
		return f'{self.name}-{self.email}'