from django.db import models

# Create your models here.
class slider(models.Model) :
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.ImageField(upload_to='slider/', blank=False)

    def _str_(self):
        return self.title