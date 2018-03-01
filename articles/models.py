from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title


    # lay 50 ki tu tu body de hien thi len trang chu
	def snippet(self):
		return self.body[:50]+"..."


# khi change data base nho run hai cau sao
# python manage.py makemigrations
# python manage.py migrate