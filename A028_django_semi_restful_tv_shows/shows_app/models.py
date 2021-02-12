from django.db import models

class TVShow(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField()

    def __repr__(self):
        return f"{self.title} {self.network}, ({self.release_date})"