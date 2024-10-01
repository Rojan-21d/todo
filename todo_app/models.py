from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)  #varchar
    description = models.TextField(null=True, blank=True) #varchar
    
    def __str__(self):
        return self.title