from rest_framework import generics
from api.models import Capybara
from .serializers import ListCapySerializer
from .serializers import DetailCapySerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions

class ReadDetailPermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        # if request.method in SAFE_METHODS:
        #     return True

        return request.user in obj.parent.all()

class CapyList(generics.ListAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset=Capybara.objects.all()
    serializer_class=ListCapySerializer
    

class CapyDetail(generics.RetrieveAPIView):
    permission_classes=[ReadDetailPermission]
    queryset=Capybara.objects.all()
    serializer_class=DetailCapySerializer
    # lookup_field="pk"
    
    