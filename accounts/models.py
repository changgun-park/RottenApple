from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.enums import Choices
from movies.models import Genre

# Create your models here.

class User(AbstractUser):

    # adventure = 12
    # fantasy = 14
    # animation = 16
    # drama = 18
    # horror = 27
    # action = 28
    # comedy = 35
    # history = 36
    # western = 37
    # thriller = 53
    # criminal = 80
    # documentary = 99
    # sf = 878
    # mystery = 9648
    # music = 10402
    # romance = 10749
    # family = 10751
    # war = 10752
    # tv = 10770
  

    # GENRE_CHOICE = [
        # (12, '모험'),
        # (14, '판타지'),
        # (16, '애니메이션'),
        # (18, '드라마'),
        # (27, '공포'),
        # (28, '액션'),
        # (35, '코미디'),
        # (36, '역사'),
        # (37, '서부'),
        # (53, '스릴러'),
        # (80, '범죄'),
        # (99, '다큐멘터리'),
        # (878, 'SF'),
        # (9648, '미스터리'),
        # (10402, '음악'),
        # (10749, '로맨스'),
        # (10751, '가족'),
        # (10752, '전쟁'),
        # (10770, 'TV영화'),
    # ]

    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    is_expert = models.BooleanField(default=False)
    # preferences = models.IntegerField(Choices=GENRE_CHOICE, default=None)
    genres = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return self.username
    