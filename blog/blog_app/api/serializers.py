from rest_framework import serializers
from blog_app.models import BlogPost,Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    Blog_post =ReviewSerializer(many=True,read_only = True)

    class Meta:
        model = BlogPost
        fields = '__all__'
        