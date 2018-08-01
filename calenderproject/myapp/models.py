from django.db import models

class Entry(models.Model):
    name = models.CharField(max_length=50, blank=True)
    date = models.DateTimeField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



# Create your models here.
