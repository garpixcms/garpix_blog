from garpix_blog.models import BlogPage, CategoryPage
from rest_framework import serializers
from .post import PostPageSerializer


class PostPageCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryPage
        fields = ['id', 'title']


class BlogPageSerializer(serializers.ModelSerializer):
    category = PostPageCategorySerializer(read_only=True, many=True)
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
