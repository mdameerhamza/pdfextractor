from django.db import models

# Create your models here.

class ExtractedData(models.Model):
    email = models.EmailField(unique=True)
    nouns = models.JSONField()
    verbs = models.JSONField()
