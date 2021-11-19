from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Article,CommunityComment
from .serializers import ArticleListSerializer,CommunityCommentSerializer,ArticleSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles,many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','DELETE','PUT'])
def article_detail(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(Article,pk=article_pk)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete':f'데이터 {article_pk}번이 삭제되었습니다.'
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)

    elif request.mehood == 'PUT':
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def article_comment_list(request):
    comments = get_list_or_404(CommunityComment)
    serializer = CommunityCommentSerializer(comments,many=True)
    return Response(serializer.data)


@api_view(['GET','DELETE','PUT'])
def article_comment_detail(request,article_comment_pk):
    comment = get_object_or_404(CommunityComment,article_comment_pk)

    if request.method == 'GET':
        serializer = CommunityCommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'message': f'댓글 {article_comment_pk}번이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommunityCommentSerializer(comment,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
def article_comment_create(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    serializer = CommunityCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data,status=status.HTTP_201_CREATED)




