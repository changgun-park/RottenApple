from rest_framework import serializers
from .models import Article,CommunityComment
from accounts.serializers import UserDetailSerializer
from rest_framework.fields import CurrentUserDefault


class ArticleListSerializer(serializers.ModelSerializer):
    # user = CurrentUserDefault()
    class Meta:
        model = Article
        # fields = '__all__'
        fields = '__all__'
        read_only_fields=('user','like_users','category','rate',)
        
        # def save(self):
        #     user = CurrentUserDefault()

class CommunityCommentSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    
    class Meta:
        model = CommunityComment
        fields = '__all__'
        read_only_fields=('article',)

class ArticleSerializer(serializers.ModelSerializer):

    communitycomment_set = CommunityCommentSerializer(many=True,read_only=True)
    # community_comment_count = serializers.IntegerField(source='communitycomment_set.count',read_only=True)
    class Meta:
        model = Article
        fields='__all__'
        read_only_fields=('user','like_users','category','rate',)