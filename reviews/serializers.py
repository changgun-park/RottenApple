from rest_framework import serializers
from .models import Review

class ReviewListSerializer(serializers.ModelSerializer):
    # 영화 이름 출력
    movie = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ('movie', 'title', 'user', 'created_at', 'views')