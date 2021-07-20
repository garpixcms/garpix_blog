from rest_framework import serializers

from blog.models import PostPage, PostCategory, PostVideos, PostImages


class PostPageCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = ['id', 'title']


class PostPageVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVideos
        fields = ['id', 'title', 'video', 'created_at', 'updated_at']


class PostPageImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = ['id', 'title', 'image', 'created_at', 'updated_at']


class PostPageSerializer(serializers.ModelSerializer):
    category = PostPageCategorySerializer(read_only=True, many=True)
    videos = PostPageVideosSerializer(read_only=True, many=True)
    images = PostPageImagesSerializer(read_only=True, many=True)

    class Meta:
        model = PostPage
        fields = [
            'id', 'blog', 'short_description',
            'news_content', 'image_preview',
            'type', 'category', 'images', 'videos',
        ]


class PostPageListSerializer(serializers.ModelSerializer):
    category = PostPageCategorySerializer(read_only=True, many=True)
    url = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_url(obj):
        return obj.slug

    class Meta:
        model = PostPage
        fields = [
            'id', 'blog', 'short_description',
            'news_content', 'image_preview',
            'type', 'category', 'url',
        ]
