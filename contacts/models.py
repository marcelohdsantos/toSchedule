from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=150, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    showfild = models.BooleanField(default=True)

    def __str__(self):
        return self.name

