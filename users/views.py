from .serializers import UserSerializer
from . models import CustomUser
from rest_framework import viewsets
# Create your views here.
class UserListView(viewsets.ModelViewSet):
	queryset = CustomUser.objects.all().order_by('id')
	serializer_class = UserSerializer

