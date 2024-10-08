from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer
from rest_framework import status


class UserCreateAPIView(CreateAPIView):
    """
    Эндпоинт для создания пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"message": "Пользователь успешно зарегистрирован"},
            status=status.HTTP_201_CREATED
        )
