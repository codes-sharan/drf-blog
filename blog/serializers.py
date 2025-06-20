from rest_framework import serializers
from .models import BlogPost, Category, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_username', 'content', 'created_at']
        read_only_fields = ['author', 'created_at']


class BlogPostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False)
    image = serializers.ImageField(required=False)
    comments = CommentSerializer(many=True, read_only=True)
    slug = serializers.ReadOnlyField()

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'slug', 'content', 'author', 'author_username', 'category', 'image',
                  'created_at', 'updated_at', 'published', 'comments']
        read_only_fields = ['author', 'created_at', 'updated_at', 'slug']
