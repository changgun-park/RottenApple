from rest_framework import serializers
from .models import Article,CommunityComment

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = '__all__'
        fields = ('id', 'title','content','user',)
        # read_only_fields=('like_users','rate','category',)

class CommunityCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityComment
        fields = '__all__'
        read_only_fields=('article',)

class ArticleSerializer(serializers.ModelSerializer):

    # community_comment_set = CommunityCommentSerializer(many=True,read_only=True)
    # community_comment_count = serializers.IntegerField(source='communitycomment_set.count',read_only=True)
    class Meta:
        model = Article
        fields='__all__'
        read_only_fields=('like_users',)