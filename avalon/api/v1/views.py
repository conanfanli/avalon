import typing

from rest_framework import viewsets, serializers
from avalon.core.models import Mission, Vote


class MissionDataSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    votes = serializers.ListField(
        child=serializers.BooleanField(),
        required=False
    )
    number_of_voters = serializers.IntegerField()


class MissionSerializer(serializers.Serializer):
    data = MissionDataSerializer()

    def create(self, validated_data):
        return Mission.create(number_of_voters=validated_data['data']['number_of_voters'])

    def update(self, obj, validated_data):
        new_fields = {}
        for (key, value) in validated_data['data'].items():
            new_fields[key] = value

        obj.data._replace(**new_fields)
        obj.save()
        return obj


class MissionViewSet(viewsets.ModelViewSet):
    serializer_class = MissionSerializer

    def get_queryset(self) -> typing.List[Mission]:
        return Mission.select_all()

    def get_object(self):
        pk = self.kwargs['pk']
        return Mission.get_by_id(pk)


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote


class VoteViewSet(viewsets.ModelViewSet):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()
