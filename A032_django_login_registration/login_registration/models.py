from django.db import models

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        return errors

    def registration(self, postData):
        pass

class User(models.Model):
    first = models.CharField(max_length=60) 
    last = models.CharField(max_length=60)
    email = models.EmailField(max_length=255, unique=True)
    pw = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return f"User: {self.first} {self.last} {self.email}"
