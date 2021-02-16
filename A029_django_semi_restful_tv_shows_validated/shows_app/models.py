from django.db import models
from datetime import date, datetime

class TVShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        # Validate size/presence of input
        if len(postData['title']) < 2:
            errors['title'] = "Show title is required. Should be at least 2 characters."
        if len(postData['network']) < 3:
            errors['network'] = "Network is required. Should be at least 3 characters."
        if len(postData['description']) < 10 and len(postData['description']) > 0:
            errors['description'] = "Description is optional, but requires at least 10 characters."
        
        # Validate alphanumerics
        if not postData['title'].isalnum():
            errors['title'] = "Show title can only contain alphanumeric characters"

        # Validate release_date is in the past, ignoring edge case of adding a new show the day it released
        if len(postData['release_date']) < 1:
            errors['release_date'] = "Release Date is required."
        else:
            release_date = datetime.strptime(postData['release_date'], "%Y-%m-%d")
            today = datetime.now()

            if release_date > today:
                print(release_date, today)
                errors['release_date'] = "Release Date must be in the past."

        # Validate that a show doesn't already exist before creation
        result = TVShow.objects.filter(title=postData['title'])
        if result:
            print(result)
            errors['title'] = f"The movie '{ postData['title'] }'' already exists."
            
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