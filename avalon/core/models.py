from django.db import models


class Mission(models.Model):
    number_of_voters = models.SmallIntegerField()


class Vote(models.Model):
    voter = models.CharField(max_length=10)
    decision = models.BooleanField()
