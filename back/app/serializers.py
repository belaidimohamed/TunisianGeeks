from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ['id','username','password']
        extra_kwargs = {'password':{'write_only':True , 'required':True}}
    def create(self,validated_data): 
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta :
        model = UserProfile
        fields = [ 'user','fullname','profilePicture','sex','bio','adress',
                   'phone','email','about','skills','languages','education','experience']

class FieldSerializer(serializers.ModelSerializer):
    class Meta :
        model = Field
        fields = ['user','title']
class ProjectSerializer(serializers.ModelSerializer):
    class Meta :
        model = Project
        fields = ['field','title','description','code_file','bugs']
        
class PhotoSerializer(serializers.ModelSerializer):
    class Meta :
        model = Photo
        fields = ['project','legend','image']

class CommentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Comment 
        fields = ['project','comment','user','jaims']

class RepondreCommentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Comment 
        fields = ['comment','user','reponse','jaims']

class TestSerializer(serializers.ModelSerializer):
    class Meta :
        model = Test
        fields = ['code_file']