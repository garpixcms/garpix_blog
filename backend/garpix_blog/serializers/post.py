from rest_framework import serializers

from garpix_blog.models import PostPage, PostVideo, PostImage


class PostPageVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVideo
        fields = ['id', 'title', 'video', 'created_at', 'updated_at']


class PostPageImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id', 'title', 'image', 'created_at', 'updated_at']


class PostPageSerializer(serializers.ModelSerializer):
    videos = PostPageVideoSerializer(read_only=True, many=True)
    images = PostPageImagesSerializer(read_only=True, many=True)

    class Meta:
        model = PostPage
        fields = [
            'id', 'blog', 'short_description',
            'content', 'image_preview', 'images', 'videos',
        ]


class PostPageListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_url(obj):
        return obj.slug

    class Meta:
        model = PostPage
        fields = [
            'id', 'blog', 'short_description',
            'content', 'image_preview', 'url',
        ]
