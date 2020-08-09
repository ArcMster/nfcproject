from django.db import models

# Create your models here.
class Stories(models.Model):
    name = models.CharField(max_length=30)
    story = models.TextField(max_length=500)
    photo = models.ImageField(upload_to= 'media', default='media/default.png')

    def __str__(self):
        return self.name

class Videos(models.Model):
    name = models.CharField(max_length=50)
    video_link = models.CharField(max_length=150)

    def __str__(self):
        return self.name