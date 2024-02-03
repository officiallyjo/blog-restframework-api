from django.urls import path
from blog_app.api.views import blog

urlpatterns = [
    path('',blog),
]
