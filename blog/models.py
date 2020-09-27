from django.db import models
from django.utils import timezone
from django.db.models import Avg
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    categorie = models.ForeignKey('Categories', on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    draft = models.BooleanField(default=False)
    tag = models.ManyToManyField('HashTag', blank=True, null=True)

    @property
    def middle(self):
        mark = Mark.objects.filter(post=self).aggregate(Avg('mark'))
        if mark['mark__avg'] is None:
            return 'оценок нет'
        return int(mark['mark__avg'])

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


class Categories(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f'{self.name}'



class HashTag(models.Model):
    name = models.CharField(max_length=44)

    def __str__(self):
        return f'{self.name}'


class Mark(models.Model):
    mark = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.mark}'
