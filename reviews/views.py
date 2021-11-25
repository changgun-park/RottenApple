from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework.response import Response
from .models import Review, ReviewComment
from .serializers import ReviewCommentSerializer, ReviewListSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
# Create your views here.


# Review 목록 출력
@api_view(['GET'])
@permission_classes([AllowAny])
def reviews_list(request):
    reviews = get_list_or_404(Review)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewListSerializer(review)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def review_comments(request, review_pk):
    comments = get_list_or_404(ReviewComment, review=review_pk)
    serializer = ReviewCommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def review_comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review,user=request.user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

# @api_view(['POST'])
# def review_comment_update(request, review_pk):
#     review = get_object_or_404(Review, pk=review_pk)
#     for comment in request.data:
#         serializer = ReviewCommentSerializer(data=comment)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(review=review)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)



