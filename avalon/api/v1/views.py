import typing

from rest_framework import viewsets, serializers
from avalon.core.models import Mission


class MissionDataSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    votes = serializers.ListField(
        child=serializers.BooleanField(),
        required=False
    )
    number_of_voters = serializers.IntegerField()

    def create(self, data):
        return Mission(number_of_voters=data['number_of_voters']).data


class MissionViewSet(viewsets.ModelViewSet):
    serializer_class = MissionDataSerializer

    def get_queryset(self) -> typing.List[Mission]:
        return Mission.select_all()
