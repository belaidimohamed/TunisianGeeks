from django.shortcuts import render , get_object_or_404
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated , AllowAny 
from .models import Field
from django.http import JsonResponse , HttpResponse
import json
from django.views.decorators.clickjacking import xframe_options_exempt
from rest_framework.decorators import action
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.core.serializers.json import DjangoJSONEncoder

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

    print('ce50bba92ff107daa7e60b97a6c54f196194ec51')

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

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

#---------------------------------------------- Project shit ----------------------------------------------------------------------

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True , methods=['GET'])
    def getProjects(self,request,pk=None):
        projects = Project.objects.all().filter(field=pk).values()
        data = json.dumps(list(projects))
        return JsonResponse(data, safe=False)

    @action(detail=True , methods=['POST'])
    def post(self,request,*args,**kwargs):
        field = request.data['field'] 
        title = request.data['title'] 
        description = request.data['description'] 
        code_file = request.data['code_file'] 
        bugs = request.data['bugs'] 
        Project.objects.create(field,title,description,code_file,bugs)
        return HttpResponse({'message':'Project created succefully !'},status=200)





class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    @action(detail=True , methods=['GET'])
    def getPhotos(self,request,pk=None):
        photos = Photo.objects.all().filter(project=pk).values()
        data = json.dumps(list(photos))
        print(data)
        return JsonResponse(data, safe=False)
    # def post(self,request,*args,**kwargs):
    #     print(2)
    #     print(request.data)
    #     project = request.data['project'] 
    #     legend = request.data['legend'] 
    #     image = request.data['image'] 
    #     Project.objects.create(project,legend,image)
    #     return HttpResponse({'message':'Project created succefully !'},status=200)




# --------------------------------------------- Comment shit ----------------------------------------------------------
 
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    @action(detail=True , methods=['GET'])
    def getComments(self,request,pk=None):
        comments = Comment.objects.all().filter(project=pk).values('id','project','user','comment','timeSent','jaims')
        for i in comments :
            i['username'] = str(User.objects.get(id=i['user']))
            # if i['jaims']!= None :
            #     i['jaims'] =  {{"id":i['jaims'],"username":str(User.objects.get(id=i['jaims']))}}
        data = json.dumps(list(comments),sort_keys=True,indent=1,cls=DjangoJSONEncoder)
        print(data)
        return JsonResponse(data, safe=False)

class CommentRepondreViewSet(viewsets.ModelViewSet):
    queryset = RepondreComment.objects.all()
    serializer_class =RepondreCommentSerializer



# <QuerySet [{'id': 1, 'project_id': 4, 'user_id': 14, 'comment': 'hello', 'jaims': 0,
#  'timeSent': datetime.datetime(2020, 9, 13, 9, 35, 42, 200080, tzinfo=<UTC>)}]>
def likeComment(request):
    if request.method == "POST":
        print(request.POST)
        print("shit")
        print(request.POST['uid'],'--',request.POST['id'])
        print('maw')
        user = get_object_or_404(User, id=request.POST['uid'])
        comment  = get_object_or_404(Comment, id=request.POST['id'])
        print(user,'--',comment)

        if comment.jaims.filter(id=user.id).exists():
            comment.jaims.remove(user)
        else:
            comment.jaims.add(user)
        print(comment.jaims.all())
        x={'likes':comment.jaims.all().count(),'users':list(comment.jaims.all().values('id','username'))}
        print('@@@',x)

        data = json.dumps(x)
        print('---',data)
        return JsonResponse(data,safe=False)

#------------------------------------------------ Profile Shit ------------------------------------------------------------

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

    @action(detail=True , methods=['POST'])
    def editProfile(self,request,pk=None):
        user = User.objects.get(id=pk)
        print(user)
        print(request.POST)
        print(request.FILES)
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
    @action(detail=True , methods=['POST'])
    def addSkill(self,request,pk=None):
        print(request.POST)
        profile = UserProfile.objects.get(user = pk)
        print(profile.skills)
        if request.method == "POST":
            skills = json.loads(profile.skills)
            skills[request.POST['skill'].capitalize()] = int(request.POST['percentage'])
            # skills= str(skills)
            print('---',skills)
            profile.skills = json.dumps(skills)
            profile.save()
        print(profile.skills)
        return HttpResponse(status=201)
    @action(detail=True , methods=['POST'])
    def addEducation(self,request,pk=None):
        print(request.POST)
    @action(detail=True , methods=['POST'])
    def addLang(self,request,pk=None):
        print(request.POST)
        profile = UserProfile.objects.get(user = pk)
        print(profile.languages)
        if request.method == "POST":
            languages = json.loads(profile.languages)
            languages[request.POST['lang'].capitalize()] = request.POST['level']
            # languages= str(languages)
            print('---',languages)
            profile.languages = json.dumps(languages)
            profile.save()
        print(profile.languages)
        return HttpResponse(status=201)
# <QueryDict: {'bio': ['i am the best'], 'adress': ['ain drahem'],
#  'email': ['mohamedbelaidi408@gmail.com'], 'phone': ['52664796'], 'sex': ['male']}>