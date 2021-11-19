from django.db import models
from django.conf import settings

# Create your models here.

class Article(models.Model):

    # num_choices = zip(range(1, 10 + 1), range(1, 10 + 1))
    # num_choices = ((1,1), (2, 2).....(10, 10))

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(default=0)
    category = models.CharField(max_length=50,blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles")

    def __str__(self):
        return self.title
    

class CommunityComment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    