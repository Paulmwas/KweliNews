from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=700)
    image = models.ImageField(upload_to='articleImages/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    