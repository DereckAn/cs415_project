from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
        
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
    # profile_bio = models.CharField(max_length=500, blank=True, null=True)
    profile_picture = models.CharField(max_length=100, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserInfo'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.created_date}'