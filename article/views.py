from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from rest_framework import serializers
from rest_framework import status
# Create your views here.

class articleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"




@api_view(['GET'])
def getAllArticles(request):
    allpost = Post.objects.filter(active = True).all().order_by("-dateCreated")
    
    converted_data = articleSerializer(allpost, many=True)
    return Response(converted_data.data)


@api_view(['GET'])
def getArticle(request, id):
     post = Post.objects.filter(id = id).first()
     converted_data = articleSerializer(post)

     return Response(data=converted_data.data)



@api_view(['POST'])
def createArticle(request):

    
    serializer = articleSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
