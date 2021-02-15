from django.db import models

class TVShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        # Validate size/presence of input
        if len(postData['title']) < 2:
            errors['title'] = "Movie title is required. Should be at least 2 characters."
        if len(postData['network']) < 3:
            errors['network'] = "Network is required. Should be at least 3 characters."
        if len(postData['release_date']) < 1:
            errors['release_date'] = "Release Date is required."
        if len(postData['description']) < 10 and len(postData['description']) > 0:
            errors['description'] = "Description is optional, but requires at least 10 characters."


        # Validate email regex
        # Valdiate date object is in the past
        # validate alphanumerics
        return errors

class TVShow(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TVShowManager()

    def __repr__(self):
        return f"{self.title} {self.network}, ({self.release_date})"