from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):

    text = models.TextField()
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    

