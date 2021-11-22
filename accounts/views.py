from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    # Client가 보낸 데이터 중 비밀번호 확인
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다'})
    
    genres = request.data.get('selected')

    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # 비밀번호 해싱
        user.set_password(request.data.get('password'))
        # DB 반영
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

