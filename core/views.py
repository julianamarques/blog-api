from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import User
from .serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

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
    name = 'user-detail'
