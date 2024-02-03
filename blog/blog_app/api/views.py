from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404



from blog_app.models import BlogPost
from  blog_app.api.serializers import BlogSerializer


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
    def get(self,request,pk):
        blog_posts = get_object_or_404(BlogPost ,pk= pk)
        serializer = BlogSerializer(blog_posts)
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