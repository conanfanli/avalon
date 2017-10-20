import uuid
import typing
from django.core.cache import cache
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


class MissionData(typing.NamedTuple):
    id: str
    votes: typing.List[bool]
    number_of_voters: int


class Mission:
    data: MissionData

    def __init__(self, number_of_voters: int) -> None:
        super().__init__()
        self.data = MissionData(
            id=str(uuid.uuid4()),
            votes=[],
            number_of_voters=number_of_voters
        )

        missions = cache.get('missions', [])
        missions.append(self.data)
        cache.set('missions', missions)

    @classmethod
    def select_all(cls) -> typing.List['Mission']:
        return cache.get('missions')
