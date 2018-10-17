from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class blogModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    blogTitle = models.CharField(max_length=100)
    blogEntry = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.blogTitle
