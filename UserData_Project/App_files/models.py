from django.db import models

# Create your models here.
class User(models.Model):
    U_name=models.CharField(max_length=64)
    U_pass=models.CharField(max_length=64)
    def __str__(self):
        return self.U_name
