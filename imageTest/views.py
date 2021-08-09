from django.db.models import query
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, serializers , status
from rest_framework.parsers import MultiPartParser , FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from rest_framework.parsers import JSONParser 
from .models import Post
from rest_framework.decorators import api_view , parser_classes
from .models import Post
# Create your views here.


class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer    

#PostView
@csrf_exempt
@api_view(['POST' , 'GET' , 'DELETE'])
@parser_classes([MultiPartParser , FormParser])
def PostUpload(request , format = None):

    if request.method == 'POST':
        print(request.data)
        serializer = PostSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)    

    elif request.method == 'GET':
        post = Post.objects.all()

        serializer = PostSerializer(data = post , many = True)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        count = Post.objects.all().delete()
        return Response({'message': '{} Posts were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

#DetailView
@api_view(['GET' , 'PUT' , 'DELETE'])
def PostDetail(request , pk , format = None):
    try:
        post = Post.objects.get(pk = pk)
    except Post.DoesNotExist:
        return Response({'message': 'The Post does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET': 
        serializer = PostSerializer(post) 
        return Response(serializer.data) 

    elif request.method == 'PUT':
        serializer = PostSerializer(post,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)          


    elif request.method == 'DELETE':
        post.delete()
        return Response({'message': 'Post was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        




