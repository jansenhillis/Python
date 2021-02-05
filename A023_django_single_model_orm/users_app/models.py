from django.db import models

class User(models.Model):
    # automatically includes id, updated_at, created_at
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()

