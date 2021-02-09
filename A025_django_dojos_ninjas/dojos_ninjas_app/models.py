from django.db import models

class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.TextField(blank=True)

    def __repr__(self):
        return f"Dojo: {self.name} ({self.city}, {self.state})"

class Ninjas(models.Model):
    dojo = models.ForeignKey(Dojos, related_name='ninjas', on_delete="models.PROTECT")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __repr__(self):
        return f"Ninja: {self.first_name} {self.last_name} '{self.dojo.name}'"