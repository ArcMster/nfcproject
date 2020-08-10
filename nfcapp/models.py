from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Stories(models.Model):
    name = models.CharField(max_length=30)
    story = RichTextField(blank=False)
    photo = models.ImageField(upload_to= 'media', default='media/default.png')

    def __str__(self):
        return self.name

class Videos(models.Model):
    name = models.CharField(max_length=255)
    video_link = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Quote_list(models.Model):
    date = models.DateField(max_length=30)
    quote = models.CharField(max_length=255)

    def __str__(self):
        return self.date

class Emails(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)