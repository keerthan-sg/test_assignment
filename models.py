from django.db import models

# Create your models here.

class login_table(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length=50)


class Meta:
      db_table = "login_table"

class ticket_table(models.Model):
    PWSLab_Project_URL = models.CharField(max_length=300)
    Subject = models.EmailField(max_length = 100)
    Description = models.CharField(max_length=50)

