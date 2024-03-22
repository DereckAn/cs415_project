from rest_framework import serializers
from cs415.models import User, InterviewFriend, Ima2Code, Chat, Userinfo, Pagedata, Addresstype, Useraddress, Phonetype, Userphone


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
        
class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Userinfo
        fields='__all__'
        
class PageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model= Pagedata
        fields='__all__'


class AddressTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Addresstype
        depth=1
        fields = '__all__'


class AddressSerializerGet(serializers.ModelSerializer):
    address_type = AddressTypeSerializer(read_only=True)
    class Meta:
        model = Useraddress
        # depth = 1
        fields = '__all__'


class AddressSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Useraddress
        fields = '__all__'


class PhoneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Phonetype
        depth=1
        fields = '__all__'

class PhoneSerializerGet(serializers.ModelSerializer):
    phone_type = PhoneTypeSerializer(read_only=True)
    class Meta:
        model=Userphone
        fields = '__all__'


class PhoneSerializerPost(serializers.ModelSerializer):
    class Meta:
        model=Userphone
        fields = '__all__'