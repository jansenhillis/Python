from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # validate alphanumerics
        # validate date
        

        # Course name > 5 characters
        # desc > 15 characters

        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    objects = CourseManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)