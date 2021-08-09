from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.TextField(max_length= 25)
    image = models.ImageField(upload_to = 'pics' , blank = True)

    def __str__(self):
        return self.name