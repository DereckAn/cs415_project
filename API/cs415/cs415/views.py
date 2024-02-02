from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cs415.models import User, InterviewFriend, Ima2Code, Chat
from cs415.serializers import UserSerializer, InterviewFriendSerializer, Ima2CodeSerializer, ChatSerializer

class UserAPIView(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})

class InterviewFriendAPIView(APIView):
    def get(self,request):
        interviewfriends = InterviewFriend.objects.all()
        serializer = InterviewFriendSerializer(interviewfriends, many=True)
        return Response({'interviewfriends': serializer.data})

class Ima2CodeAPIView(APIView):
    def get(self,request):
        ima2codes = Ima2Code.objects.all()
        serializer = Ima2CodeSerializer(ima2codes, many=True)
        return Response({'ima2codes': serializer.data})
    
class ChatAPIView(APIView):
    def get(self,request):
        chats = Chat.objects.all()
        serializer = ChatSerializer(chats, many=True)
        return Response({'chats': serializer.data})