from django.db import models

# Create your models here.

class HomeText(models.Model):
    title = models.CharField(max_length = 50)
    introduction = models.TextField(max_length = 700)


    def __str__(self):
        return self.title
        
