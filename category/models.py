from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='uploads/')
    sub = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
