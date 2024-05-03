from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    year = models.IntegerField()

    def __str__(self):
        return self.title + str(self.year)
