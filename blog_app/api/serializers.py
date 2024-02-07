# from rest_framework import serializers
# from blog_app.models import BlogPost,Review

# class ReviewSerializer(serializers.ModelSerializer):
#     author_id= serializers.StringRelatedField(read_only=True )
    
#     class Meta:
#         model = Review
#         fields = '__all__'

# class BlogSerializer(serializers.ModelSerializer):
#     Blog_post = ReviewSerializer(many=True,read_only = True)

#     class Meta:
#         model = BlogPost
#         fields = '__all__'
        
from rest_framework import serializers
from blog_app.models import BlogPost, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # Nested serializer for reviews

    class Meta:
        model = BlogPost
        fields = '__all__'
