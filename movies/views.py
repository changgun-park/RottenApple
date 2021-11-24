from django.shortcuts import render
from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from .models import Movie
from . serializers import MovieSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies,many=True)
    return Response(serializer.data)