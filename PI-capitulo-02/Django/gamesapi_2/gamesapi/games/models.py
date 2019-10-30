from django.db import models


class GameCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    played = models.BooleanField(default=False)
    game_category = models.ForeignKey(GameCategory, on_delete=models.CASCADE, related_name='games')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Player(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'),)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=2,
                              choices=GENDER_CHOICES,
                              default=MALE,)


class Score(models.Model):
    score = models.IntegerField()
    score_date = models.DateTimeField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)