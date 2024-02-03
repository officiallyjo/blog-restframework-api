from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class BlogPost(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    review = models.CharField(max_length=100,null=True, blank=True)
    rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    blogpost = models.ForeignKey(BlogPost,on_delete = models.CASCADE,related_name ="reviews",blank=True,null=True)
    
    def __str__(self):
        return str(self.rating) # + " | " + self.blogpost.title                 
