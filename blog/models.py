from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    draft = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text}'
