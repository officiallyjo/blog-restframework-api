from django.urls import path
from blog_app.api.views import MyBlogApiView,MyBlogDetailView

urlpatterns = [
    path('',MyBlogApiView.as_view()),
    path('details/<int:pk>',MyBlogDetailView.as_view())
]
