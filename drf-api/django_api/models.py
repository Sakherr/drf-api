from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class API(models.Model):
      reviewer = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
      name = models.CharField(max_length=255)
      desc = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
  
