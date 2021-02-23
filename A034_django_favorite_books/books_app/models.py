from django.db import models
from login_app.models import User

class BookManager(models.Manager):
    def validator(self, postData):
        errors = {}
        
        if not postData['title']:
            errors['title'] = "Title must not be blank."
        if len(postData['desc']) < 5:
            errors['description'] = "Description must at least 5 characters long."

        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_by_id = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    favorited_by_id = models.ManyToManyField(User, related_name="books_favorited")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BookManager()

    def __str__(self):
        return f"Book: {self.title} uploaded by {self.uploaded_by_id}"