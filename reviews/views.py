from django.shortcuts import get_list_or_404, render
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewListSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
# Create your views here.


# Review 목록 출력
@api_view(['GET'])
@permission_classes([AllowAny])
def reviews_list(request):
    reviews = get_list_or_404(Review)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)