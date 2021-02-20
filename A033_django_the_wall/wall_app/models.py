from django.db import models
from login_app.models import User

class MessageManager(models.Manager):
    def validator(self, postData):
        errors = {}
        return errors

class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()

    def __str__(self):
        return f"Message: {self.user_id}: {self.message}"
