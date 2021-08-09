from django.urls import path , include
from .views import PostView , PostDetailView , PostUpload , PostDetail

urlpatterns = [
    path("" , PostView.as_view()),
    path("<int:pk>/" , PostDetailView.as_view()),
    path("post" , PostUpload),
    path("post/<int:pk>" , PostDetail)
]
