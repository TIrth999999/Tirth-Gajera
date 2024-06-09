from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    name = models.CharField(max_length = 122,default = "NULL")
    email = models.CharField(max_length = 122,default = "NULL")
    subject = models.CharField(max_length = 100,default = "NULL")
    message = models.CharField(max_length = 1000,default = "NULL")

    def __str__(self):
        return self.name