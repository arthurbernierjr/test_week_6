from django.db import models

# Create your models here.


class Thing(models.Model):
    content = models.CharField(max_length=200)

    def __str__(self):
        return '%s ' % self.content