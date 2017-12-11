# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from app1.models import Snippet
# from app1.serializers import SnippetSerializer

# class JSONResponse(HttpResponse):
#     ## An HttpResponse that renders its content into JSON
#     def __init__(self,data,**kwargs):
#         content=JSONRenderer().render(data)
#         kwargs['content_type']='application/json'
#         super(JSONResponse,self).__init__(content,**kwargs)

# @csrf_exempt
# def snippet_list(request):
#     ## List all code snippets ,or create a new snippet.
#     if request.method=="GET":
#         snippets=Snippet.objects.all()
#         serializer=SnippetSerializer(snippets,many=True)
#         return JSONResponse(serializer.data)

#     elif request.method=="POST":
#         data=JSONParser().parse(request)
#         serializer=SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data,status=201)
#         return JSONResponse(serializer.errors,status=400)

# @csrf_exempt
# def snippet_detail(request,pk):
#     ##Retrieve ,update or delete a code snippet
#     try:
#         snippet=Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(404)

#     if request.method=="GET":
#         serializer=SnippetSerializer(snippet)
#         return JSONResponse(serializer.data)

#     elif request.method=="PUT":
#         data=JSONParser.parse(request)
#         serializer=SnippetSerializer(snippet,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)

#     elif request.method=="DELETE":
#         snippet.delete()
#         return HttpResponse(status=204)



###******************RECODING*****

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from app1.models import Snippet
# from app1.serializers import SnippetSerializer

# @api_view(['GET','POST'])
# def snippet_list(request,format=None):
#     ##列出所有的代码片段，或者创建一个代码片段
#     if request.method=="GET":
#         snippets=Snippet.objects.all()
#         serializer=SnippetSerializer(snippets,many=True)
#         return Response(serializer.data)

#     else:
#         serializer=SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def snippet_detail(request,pk,format=None):
#     try:
#         snippet=Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method=="GET":
#         serializer=SnippetSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method=="PUT":
#         serializer=SnippetSerializer(snippet,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     elif request.method=="DELETE":
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



###*******************RECODING .....AGAIN******
from app1.models import Snippet
from app1.serializers import SnippetSerializer
from app1.serializers import UserSerializer
from rest_framework import generics

from django.contrib.auth.models import User
from rest_framework import permissions
from app1.permissions import IsOwnerOrReadOnly

class SnippetList(generics.ListCreateAPIView):
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer