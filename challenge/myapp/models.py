from django.db import models

# currently unused model as placeholder
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name
