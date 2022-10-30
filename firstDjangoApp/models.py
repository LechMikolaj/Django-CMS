from django.db import models
from django.db.models import Model
from django.utils import timezone
import datetime



class Post(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField(max_length=200)


    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.body

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# Create your models here.
