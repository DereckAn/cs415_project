from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
        # db_table = 'user' este fue para el database en aws
        
        
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class InterviewFriend(models.Model):
    name_interview = models.CharField(max_length=255, blank=True, null=True)
    question = models.CharField(max_length=5000, blank=True, null=True)
    response = models.CharField(max_length=5000, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interview_friend'
        
    def __str__(self):
        return f'{self.question} {self.response}'
        
        
class Ima2Code(models.Model):
    ima = models.CharField(max_length=5000, blank=True, null=True)
    code = models.CharField(max_length=5000, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ima2code'
    
    def __str__(self):
        return f'{self.ima} {self.code}'


class Chat(models.Model):
    fecha = models.DateTimeField(blank=True, null=True)
    question = models.CharField(max_length=255, blank=True, null=True)
    response = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat'
    
    def __str__(self):
        return f'{self.question} {self.response}'


class Userinfo(models.Model):
    user_info_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    profile_bio = models.CharField(max_length=500, blank=True, null=True)
    profile_picture = models.CharField(max_length=100, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserInfo'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.created_date}'
    
    
class Pagedata(models.Model):
    page_data_id = models.AutoField(primary_key=True)
    page_name = models.CharField(max_length=150)
    page_title = models.CharField(max_length=150)
    page_description = models.TextField()
    page_picture = models.CharField(max_length=250)
    page_menu = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'PageData'

    def __str__(self):
        return f'{self.page_name}'


class Phonetype(models.Model):
    phone_type_id = models.AutoField(primary_key=True)
    phone_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'PhoneType'

    def __str__(self):
        return f'{self.phone_type}'
    
class Addresstype(models.Model):
    address_type_id = models.AutoField(primary_key=True)
    address_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'AddressType'

    def __str__(self):
        return f'{self.address_type}'

class Useraddress(models.Model):
    user_address_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    street_1 = models.CharField(max_length=30, blank=True, null=True)
    street_2 = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    st = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    address_type = models.ForeignKey(Addresstype, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'UserAddress'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.address_1}'


class Userphone(models.Model):
    user_phone_id = models.AutoField(primary_key=True)
    phone_type = models.ForeignKey(Phonetype, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserPhone'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.phone_type.phone_type}'