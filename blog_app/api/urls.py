from django.urls import path
from blog_app.api.views import MyBlogApiView,MyBlogDetailView,CreateReview,ReviewList,ReviewDetail

urlpatterns = [
    path('',MyBlogApiView.as_view()),
    path('<int:pk>',MyBlogDetailView.as_view()),
    path('<int:pk>/review-create', CreateReview.as_view(), name='review-create'),
    path('<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
 
]
