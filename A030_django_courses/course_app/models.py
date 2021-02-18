from django.db import models

class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}

        # validate alphanumerics
        if not postData['name'].isalnum():
            errors['name'] = "Name may only contain alphanumeric characters."
        if not postData['desc'].isalnum():
            errors['desc'] = "Description may only contain alphanumeric characters."

        # Course name > 5 characters
        if len(postData['name']) < 5:
            errors['length'] = "Name is required. Minimum 5 characters."

        # desc > 15 characters
        if len(postData['desc']) < 15:
            errors['desc_length'] = "Description is required. Minimum 15 characters."

        # duplicate course already present
        course = Course.objects.filter(name=postData['name'])
        if course:
            errors['duplicate'] = "Course already present in the database."

        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    objects = CourseManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)