from django.db import models

# Create your models here.

class NewAPIPerson(models.Model):
    name = models.CharField(max_length=45)
    alias = models.CharField(max_length=45)

    def __str__(self):
        return self.name