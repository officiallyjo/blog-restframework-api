from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404



from blog_app.models import BlogPost,Review
from  blog_app.api.serializers import BlogSerializer,ReviewSerializer


class MyBlogApiView(APIView):
    def get(self,request):
        blog_posts = BlogPost.objects.all()
        serializer = BlogSerializer(blog_posts,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = BlogSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
class MyBlogDetailView(APIView):
    def get(self, request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        serializer = BlogSerializer(blog_post)
        return Response(serializer.data)
    
    
    
    def put(self,request,pk):
        blog_post = get_object_or_404(BlogPost,pk= pk)
        serializer = BlogSerializer(blog_post , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    # def delete(self,request,pk):
    #     blog_post = get_object_or_404(BlogPost,pk= pk)
    #     blog_post.delete()
        
    def delete(self, request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        blog_post.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
class CreateReview(APIView):
    def post(self, request, pk): 
        blog_post = get_object_or_404(BlogPost, pk=pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
class ReviewList(APIView):
    def get(self,request,pk):
        reviews = Review.objects.filter(blogpost_id=pk)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
class ReviewDetail(APIView):
    def get(self,request,pk):
        review = get_object_or_404(Review ,pk= pk)
        serializer = BlogSerializer(review)
        return Response(serializer.data)