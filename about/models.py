from django.db import models

# Create your models here.

class About(models.Model):
    what_we_do = models.TextField(max_length=1000)
    our_message = models.TextField(max_length=1000)
    our_goal = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='about/')

    def __str__(self):
       return str(self.id)
    
class FAQ(models.Model):
    title = models.CharField( max_length=50)
    description = models.TextField(max_length=1000)
    def __str__(self):
       return self.title