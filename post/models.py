from django.db import models

from category.models import Category


class Post(models.Model):
    post_number = models.UUIDField()
    subject = models.CharField(max_length=200)
    content = models.TextField()
    views = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.subject


class PostImage(models.Model):
    img = models.ImageField(upload_to='uploads/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.img)
