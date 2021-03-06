from django.conf import settings
from django.db import models

# Create your models here.


class Review(models.Model):
    RANKS = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]

    title = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=50)
    rank = models.PositiveIntegerField(choices=RANKS, default=5)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    like = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_reviews')

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    content = models.CharField(max_length=100)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content}'
