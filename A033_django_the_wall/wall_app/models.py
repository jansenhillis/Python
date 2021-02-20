from django.db import models
from django.db.models.fields import related
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
        return f"Message: {self.user.id}: {self.message}"

class CommentManager(models.Manager):
    def validator(self, postData):
        errors = {}
        return errors
    
class Comment(models.Model):
    message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()   

    def __str__(self):
        return f"Comment: { self.comment }"
