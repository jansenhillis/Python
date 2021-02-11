from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True)

    def __repr__(self):
        return f"{self.id} {self.title} {self.desc} "

