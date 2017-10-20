from django.core.cache import cache
from django.shortcuts import redirect
from rest_framework import viewsets, serializers
from rest_framework.response import Response
from rest_framework.decorators import list_route

from avalon.core.models import Vote, Mission


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'voter', 'decision']


class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ['id', 'number_of_voters']


class VoteViewSet(viewsets.ModelViewSet):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()

    @list_route(methods=['POST'])
    def reset(self, request):
        number_of_voters = request.data.get('number_of_voters')
        if number_of_voters:
            cache.set('number_of_voters', number_of_voters)
        else:
            cache.set('number_of_voters', 0)
        Vote.objects.all().delete()
        return redirect('v1:mission-show')


class MissionViewSet(viewsets.ModelViewSet):
    serializer_class = MissionSerializer
    queryset = Mission.objects.all()

    @list_route(methods=['GET'])
    def show(self, request):
        return Response({
            'number_of_voters': cache.get('number_of_voters', 0),
            'votes': Vote.objects.values_list('decision', flat=True)
        })
