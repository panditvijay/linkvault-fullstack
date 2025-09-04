from rest_framework import serializers
from .models import Bookmark

class BookmarkSerializer(serializers.ModelSerializer):
    # We make user_id read-only because we will set it automatically from the request context
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Bookmark
        fields = ['id', 'url', 'title', 'description', 'user_id', 'created_at']
