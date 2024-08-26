from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name='Category name')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Post title')
    description = models.TextField()
    image = models.ImageField(upload_to='posts/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    value = models.IntegerField()
    author = models.CharField(max_length=50, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Likes(models.TextChoices):
        like = '👍🏻'
        notlike = '👎🏻'

    text = models.TextField()
    like = models.CharField(max_length=2, choices=Likes.choices, default=Likes.like)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Rating(models.Model):
    class RatingStarsChoices(models.TextChoices):
        STAR_5 = '5',
        STAR_4 = '4',
        STAR_3 = '3',
        STAR_2 = '2',
        STAR_1 = '1',
        STAR_0 = '0',

    value = models.CharField(max_length=2, choices=RatingStarsChoices.choices, default=RatingStarsChoices.STAR_0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.value}'


class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    url = models.URLField()


class Settings(models.Model):
    telegram_url = models.URLField()
    instagram_url = models.URLField()
    twitter_url = models.URLField()
    facebook_url = models.URLField()

    def __str__(self):
        return 'Settings'

