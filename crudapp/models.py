from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=40, unique=True)
    description = models.TextField()
    create = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create']

# Create your models here.
