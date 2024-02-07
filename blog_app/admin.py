from django.contrib import admin
from blog_app.models import Review,BlogPost

# Register your models here.
admin.site.register(Review)
admin.site.register(BlogPost)