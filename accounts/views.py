from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from accounts.serializers import UserSerializer
from accounts.models import User
from core.models import Cart  # Import Cart model from core app


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        if self.action == 'me':
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated(), permissions.IsAdminUser()]

    @action(detail=False, methods=['get'])
    def me(self, request):
        """
        Return the authenticated user.
        Endpoint: /accounts/me/
        Returns:
            Authenticated user
        """
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        response = super().create(request)
        # Get the user object
        user = User.objects.get(email=response.data['email'])
        user.set_password(request.data.get('password'))
        user.is_active = True
        user.save()
        Cart.objects.create(user=user)

        return response
