from django.db import models

class ModelProyect(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
