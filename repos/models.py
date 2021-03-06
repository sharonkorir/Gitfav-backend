from django.db import models

# Create your models here.
class Repo(models.Model):
    repo_url = models.URLField()
    api_url = models.URLField()
    owner = models.CharField(max_length=120)
    description = models.TextField()
    name = models.CharField(max_length=120)
    languages_url = models.URLField()

    def __str__(self):
        return self.name

