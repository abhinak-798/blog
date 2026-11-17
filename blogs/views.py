from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from blogs.models import Post
from blogs.serializers import BlogSerializer
from blogs.permissions import IsAutherOrReadOnly


# Create your views here.
class ListcreateView(APIView):
    permission_classes = [IsAutherOrReadOnly]
    def get(self,request):
        qs=Post.objects.all()
        serializer_instance=BlogSerializer(qs,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer_instance=BlogSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(author=request.user)
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateDelete(APIView):
    permission_classes = [IsAutherOrReadOnly]
    def get(self,request,id):
        e=get_object_or_404(Post,id=id)
        serializer_instance=BlogSerializer(e)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        e=get_object_or_404(Post,id=id)
        serializer_instance=BlogSerializer(e,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(author=request.user)
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        e=get_object_or_404(Post,id=id)
        serializer_instance=BlogSerializer(e,data=request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save(author=request.user)
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        e=get_object_or_404(Post,id=id)
        e.delete()
        return Response({'message':'deleted succesfully'})