from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import User, Post
from .serializers import UserSerializer, PostSerializer


class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)
    name = 'users-list'

    def post(self, request):
        try:
            user = User.objects.create(name=request.data['name'], email=request.data['email'])
        
            user.set_password(request.data['password'])
            user.save()

            return Response({'Message' : 'Usuário cadastrado!'}, status=status.HTTP_201_CREATED)
            
        except Exception:
            return Response({'Message' : 'Erro ao cadastrar usuário!'}, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    name = 'user-detail'


class PostsList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'posts-list'


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'


class PublicPostsList(generics.ListAPIView):
    queryset = Post.objects.filter(public=True)
    serializer_class = PostSerializer
    name = 'public-posts-detail'


class PrivatePostsList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    name = 'private-posts-detail'

    def get(self, request):
        posts = Post.objects.filter(public=false, user=request.user)
        return Response(data=posts)
