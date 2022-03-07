"""
Book: Building RESTful Python Web Services
"""
from games.models import Breed
from games.models import Dog
from games.serializers import BreedSerializer
from games.serializers import DogSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse


class BreedList(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    name = 'breed-list'


class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    name = 'breed-detail'


class DogList(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    name = 'dog-list'


class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    name = 'dog-detail'


# class PlayerList(generics.ListCreateAPIView):
#     queryset = Player.objects.all()
#     serializer_class = PlayerSerializer
#     name = 'player-list'


# class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Player.objects.all()
#     serializer_class = PlayerSerializer
#     name = 'player-detail'


# class PlayerScoreList(generics.ListCreateAPIView):
#     queryset = PlayerScore.objects.all()
#     serializer_class = PlayerScoreSerializer
#     name = 'playerscore-list'


# class PlayerScoreDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = PlayerScore.objects.all()
#     serializer_class = PlayerScoreSerializer
#     name = 'playerscore-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'dogs': reverse(DogList.name, request=request),
            'breeds': reverse(BreedList.name, request=request),
            # 'games': reverse(GameList.name, request=request),
            # 'scores': reverse(PlayerScoreList.name, request=request)
            })
