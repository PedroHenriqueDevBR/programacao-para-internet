from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from games.models import Game
from games.serializers import GameSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def games_list(request):
    if request.method == 'GET':
        games = Game.objects.all()
        games_serializer = GameSerializer(games, many=True)
        return Response(games_serializer.data)
    
    elif request.method == 'POST':
        games_serializer = GameSerializer(data=request.data)
        if games_serializer.is_valid():
            games_serializer.save()
            return Response(games_serializer.data, status=status.HTTP_201_CREATED)
        return Response(games_serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def games_update(request, id):
    try:
        game = Game.objects.get(id=id)
    except Exception:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        games_serializer = GameSerializer(game)
        return Response(games_serializer.data)
    elif request.method == 'PUT':
        games_serializer = GameSerializer(game, data=request.data)
        if games_serializer.is_valid():
            games_serializer.save()
            return Response(games_serializer.data)
        return Response(games_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':

        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
