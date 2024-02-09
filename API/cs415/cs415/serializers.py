from rest_framework import serializers
from cs415.models import User, InterviewFriend, Ima2Code, Chat


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class InterviewFriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewFriend
        fields = '__all__'

class Ima2CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ima2Code
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
        