from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()

    def __repr__(self):
        return f"{self.id} {self.first_name} {self.last_name} ({self.age}) {self.email_address}"