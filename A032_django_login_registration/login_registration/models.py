from django.db import models

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        return errors

class User(models.Model):
    objects = UserManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=255, unique=True)
    pw = models.CharField(max_length=255)

    def __str__(self):
        return f"User: {self.first_name} {self.last_name} {self.email}"
