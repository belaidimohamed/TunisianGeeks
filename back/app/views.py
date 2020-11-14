import json
from .serializers import *
from .models import *
from .permissions import IsOwner

from django.shortcuts import  get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse , HttpResponse
from django.contrib.auth.models import User

from rest_framework import viewsets ,generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated , AllowAny 
from rest_framework.decorators import action , permission_classes , api_view
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id,
            'name': user.username
        })
class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    @action(detail=True , methods=['GET'])
    def getFields(self,request,pk=None):  
        id=pk  
        fields = Field.objects.all().filter(user=id)
        x = {}
        l=[]
        for i in fields :
            x['title'] = i.title
            x['id'] = i.id
            x['user'] = id
            l.append(x)
            x={}

        data = json.dumps(l)
        return JsonResponse(data, safe=False)

#---------------------------------------------- Project shit ----------------------------------------------------------------------

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True , methods=['GET'])
    def getComments(self,request,pk=None):
        comments = Project.objects.all().filter(id=pk).values('comments')[0]['comments']
        comments = json.loads(comments)
        for i in range(len(comments)) :
            infos = UserProfile.objects.all().filter(user=comments[i]['user']).values('fullname','profilePicture')[0]
            comments[i].update(infos)
        data = json.dumps(comments)
        return JsonResponse(data, safe=False)

    @action(detail=True , methods=['GET'])
    def getProjects(self,request,pk=None):
        projects = Project.objects.all().filter(field=pk).values()
        data = json.dumps(list(projects))
        return JsonResponse(data, safe=False)

    @action(detail=True , methods=['POST'])
    def Like(self,request,pk=None):
        project = Project.objects.get(id = pk)
        comments = json.loads(project.comments)
        uid = int(request.data['userId'])
        cid = int(request.data['commentId'])
        if uid in set().union(*(d.values() for d in comments[cid]['jaims'])) :
            comments[cid]['jaims'] =  [i for i in comments[cid]['jaims'] if (i['id']!=uid)]
            project.comments = json.dumps(comments)
        else:
            x={}
            name = UserProfile.objects.all().filter(user=uid).values('fullname')[0]['fullname']
            x['name'] = name
            x['id'] = uid
            x['type'] = 'thumb'
            comments[cid]['jaims'].append(x)
            project.comments = json.dumps(comments)
        project.save()
        return HttpResponse(status=200)



    @action(detail=True , methods=['POST'])
    def post(self,request,*args,**kwargs):
        field = request.data['field'] 
        title = request.data['title'] 
        description = request.data['description'] 
        code_file = request.data['code_file'] 
        bugs = request.data['bugs'] 
        Project.objects.create(field,title,description,code_file,bugs,comments="[]")
        return HttpResponse({'message':'Project created succefully !'},status=200)

    @action(detail=True , methods=['POST'])
    def addComment(self,request,pk=None):
        project = Project.objects.get(id = pk)
        # self.check_object_permissions(request, project)
        comments = json.loads(project.comments)
        temp = {}
        temp['id'] = len(comments)
        for i in request.data :
            temp[i] = request.data[i]
        comments.append(temp)
        project.comments = json.dumps(comments)
        project.save()
        return HttpResponse(status=201)

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    @action(detail=True , methods=['GET'])
    def getPhotos(self,request,pk=None):
        photos = Photo.objects.all().filter(project=pk).values()
        data = json.dumps(list(photos))
        return JsonResponse(data, safe=False)
    # def post(self,request,*args,**kwargs):
    #     print(2)
    #     print(request.data)
    #     project = request.data['project'] 
    #     legend = request.data['legend'] 
    #     image = request.data['image'] 
    #     Project.objects.create(project,legend,image)
    #     return HttpResponse({'message':'Project created succefully !'},status=200)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True , methods=['GET'])
    def getProfile(self,request,pk=None):
        profile = UserProfile.objects.all().filter(user=pk).values()[0]
        data = json.dumps(profile)
        return JsonResponse(data, safe=False)

    @action(detail=True , methods=['POST'], permission_classes=[IsOwner])
    def editProfile(self,request,pk=None):
        user = User.objects.get(id=pk)
        self.check_object_permissions(request, user)
        if request.method == "POST":
            fullname = request.POST['fullname']
            bio = request.POST['bio']
            adress = request.POST['adress'] 
            email = request.POST['email']
            phone = request.POST['phone']
            sex = request.POST['sex']
            profilePicture = request.FILES['profilePicture']
            b = UserProfile(user=user,bio=bio,adress=adress,email=email, phone = phone, sex= sex,profilePicture=profilePicture,
                fullname=fullname, skills= "{}",languages="{}",education="{}",experience="{}")
            b.save()
            return HttpResponse(status=201)

    @action(detail=True , methods=['POST'], permission_classes=[IsOwner])
    def addSkill(self,request,pk=None):
        profile = UserProfile.objects.get(user = pk)
        self.check_object_permissions(request, profile)
        skills = json.loads(profile.skills)
        skills[request.POST['skill'].capitalize()] = int(request.POST['percentage'])
        profile.skills = json.dumps(skills)
        profile.save()
        return HttpResponse(status=201)

    @action(detail=True , methods=['POST'], permission_classes=[IsOwner])
    def addEducation(self,request,pk=None):
        profile = UserProfile.objects.get(user = pk)
        self.check_object_permissions(request, profile)
        educ = json.loads(profile.education)
        temp = {}
        for i in request.POST :
            temp[i] = request.POST[i]
        educ[len(educ)+1] = temp
        profile.education = json.dumps(educ)
        profile.save()
        return HttpResponse(status=201)

    @action(detail=True , methods=['POST'], permission_classes=[IsOwner])
    def addExperience(self,request,pk=None):
        profile = UserProfile.objects.get(user = pk)
        self.check_object_permissions(request, profile)
        exp = json.loads(profile.experience)
        temp = {}
        for i in request.POST :
            temp[i] = request.POST[i]
        exp[len(exp)+1] = temp
        profile.experience = json.dumps(exp)
        profile.save()
        return HttpResponse(status=201)

    @action(detail=True , methods=['POST'], permission_classes=[IsOwner])
    def addLang(self,request,pk=None):
        profile = UserProfile.objects.get(user = pk)
        self.check_object_permissions(request, profile)
        languages = json.loads(profile.languages)
        languages[request.POST['lang'].capitalize()] = request.POST['level']
        profile.languages = json.dumps(languages)
        profile.save()
        return HttpResponse(status=201)

