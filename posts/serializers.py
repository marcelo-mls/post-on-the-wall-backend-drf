from rest_framework import serializers
from posts.models import Post
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "initials"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Post
        fields = ["url", "id", "post", "user", "created_at"]
