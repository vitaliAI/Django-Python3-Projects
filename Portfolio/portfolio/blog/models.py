from django.db import models

# Create your models here.


# Add the Blog app to the settings


# Creating a migration


# Migrate

# Add to the admin
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')