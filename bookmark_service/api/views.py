from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Bookmark
from .serializers import BookmarkSerializer
from .permissions import IsAuthenticatedViaGateway

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or view it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # This is a placeholder for now. We will make this secure later.
        return obj.user_id == request.user.id


class BookmarkViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    serializer_class = BookmarkSerializer
    # THIS IS A TEMPORARY PERMISSION FOR TESTING
    # We will replace this with a real one
    permission_classes = [IsAuthenticatedViaGateway]

    def get_queryset(self):
        """
        This view should return a list of all the bookmarks
        for the user identified by the gateway header.
        """
        user_id = self.request.headers.get('X-User-Id')
        # Filter the bookmarks to only include those owned by the user
        return Bookmark.objects.filter(user_id=user_id)

    def perform_create(self, serializer):
        """
        Save the bookmark with the user_id from the gateway header.
        """
        user_id = self.request.headers.get('X-User-Id')
        # Save the bookmark instance with the owner's ID
        serializer.save(user_id=user_id)