from rest_framework.permissions import BasePermission

class IsAuthenticatedViaGateway(BasePermission):
    """
    Allow access only if a trusted user ID header is present.
    """
    def has_permission(self, request, view):
        # Check if the 'X-User-Id' header is present in the request
        return 'X-User-Id' in request.headers