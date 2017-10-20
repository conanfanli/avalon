import uuid
import typing
from django.db import models
#
#
class Mission(models.Model):
    number_of_voters = models.SmallIntegerField()


class Vote(models.Model):
    voter = models.CharField(max_length=10)
    decision = models.BooleanField()


class MissionData(typing.NamedTuple):
    id: str
    votes: typing.List[bool]
    number_of_voters: int


class Mission:
    PREFIX = 'missions'
    data: MissionData

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.data = MissionData(**kwargs)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)

    @property
    def key(self):
        return f'{self.PREFIX}:{self.data.id}'

    def save(self):
        cache.set(self.key, self, timeout=None)
        return self

    @classmethod
    def create(cls, number_of_voters: int) -> 'Mission':
        mission = Mission(
            id=str(uuid.uuid4()),
            votes=[],
            number_of_voters=number_of_voters
        )
        mission.save()
        return mission

    @classmethod
    def get_by_id(cls, id) -> 'Mission':
        missions = cls.select_all()
        return [m for m in missions if m.data.id == id][0]

    @classmethod
    def select_all(cls) -> typing.List['Mission']:
        keys = cache.keys(f'{cls.PREFIX}:*')
        return list(cache.get_many(keys).values())
        # return [mission for mission in cache.get(cls.PREFIX, [])]
