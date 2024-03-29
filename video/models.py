from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    slug = models.SlugField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return(self.title)

