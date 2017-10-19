# from django.db import models
# from django.conf import settings
#
#
# class Mission(models.Model):
#     number_of_voters = models.SmallIntegerField()
#
#
# class Vote(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL)


class Mission:
    def __init__(self, players):
        self.players = players
