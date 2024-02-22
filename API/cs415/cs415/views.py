from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cs415.models import User, InterviewFriend, Ima2Code, Chat
from cs415.serializers import UserSerializer, InterviewFriendSerializer, Ima2CodeSerializer, ChatSerializer
from cs415.settings import JWT_AUTH
from cs415.authentication import JWTAuthentication
import datetime

class UserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        request.data['created_date'] = str(datetime.datetime.now())
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
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
    
class Login(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({'success': False,
                             'error': 'Email and Password must have a value'},
                             status = status.HTTP_400_BAD_REQUEST)

        check_user = User.objects.filter(email=email).exists()
        if check_user == False:
            return Response({'success': False,
                             'error': 'User with this email does not exist'},
                             status=status.HTTP_404_NOT_FOUND)

        check_pass = User.objects.filter(email = email, password=password).exists()
        if check_pass == False:
            return Response({'success': False,
                             'error': 'Incorrect password for user'},
                             status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.get(email = email, password=password)

        # add last login to User table
        serializer = UserSerializer(user, data={'last_login': str(datetime.datetime.now())}, partial=True)
        if serializer.is_valid():
            serializer.save()

        if user is not None:
            jwt_token = JWTAuthentication.create_jwt(user)
            data = {
                'token': jwt_token
            }
            return Response({'success': True,
                             'user_id': user.user_id,
                             'token': jwt_token},
                             status=status.HTTP_200_OK)
        else:
            return Response({'success': False,
                             'error': 'Invalid Login Credentials'},
                             status=status.HTTP_400_BAD_REQUEST)


class GetSingleUserAPIView(APIView):
    def get(self,request,id):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user_data = {}
        user = User.objects.get(pk=id)
        user_serial = UserSerializer(user)
        user_data.update({"user": user_serial.data})
        return Response(user_data)
    
class GetSingleUserInfoAPIView(APIView):
    def get(self,request,id):
        if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
        user = User.objects.get(pk=id)
        info = Userinfo.objects.filter(user=user)
        serializer = UserinfoSerializer(info, many=True)
        return Response({'info': serializer.data})
    
# class GetSingleUserAPIView(APIView):
#     def get(self,request,id):
#         if JWT_AUTH: JWTAuthentication.authenticate(self,request=request)
#         user_data = {}
#         user = User.objects.get(pk=id)
#         user_serial = UserSerializer(user)
#         user_data.update({"user": user_serial.data})
#         addresses = AddressSerializerGet(Useraddress.objects.filter(user=user), many=True)
#         user_data.update({"addresses": addresses.data})
#         info = UserinfoSerializer(Userinfo.objects.filter(user=user), many=True)
#         user_data.update({"info": info.data})
#         phone = PhoneSerializerGet(Userphone.objects.filter(user=user).select_related(), many=True)
#         user_data.update({"phones": phone.data})
#         return Response(user_data)