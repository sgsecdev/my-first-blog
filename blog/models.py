from django.db import models
from django.utils import timezone as ut

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=ut.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = ut.now()
        self.save()

    def __str__(self):
        return self.title

