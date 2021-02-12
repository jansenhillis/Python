from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True)

    def __repr__(self):
        return f" {self.id} {self.title} {self.desc} "

class Authors(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField(blank=True)
    books = models.ManyToManyField(Books, related_name='authors')

    def __repr__(self):
        return f" {self.id} {self.first_name} {self.last_name} "