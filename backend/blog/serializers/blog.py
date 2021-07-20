from blog.models import BlogPage
from rest_framework import serializers
from .post import PostPageSerializer


class BlogPageSerializer(serializers.ModelSerializer):
    posts = PostPageSerializer(read_only=True, many=True)

    class Meta:
        model = BlogPage
        fields = '__all__'


class BlogPageListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_url(obj):
        return obj.slug

    class Meta:
        model = BlogPage
        fields = ['title', 'url']
