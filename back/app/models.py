from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField , ArrayField


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) 
    fullname = models.CharField(default='none',max_length=50)
    profilePicture = models.ImageField(upload_to='profile/',null=True)
    sex = models.CharField(default='None',max_length=10)
    bio = models.CharField(null=True, max_length=100)
    adress = models.CharField(null=True,max_length=100)
    phone = models.CharField(null=True,max_length=20)
    email = models.EmailField(null=True,max_length=254)
    about = models.TextField(null=True)
    languages = JSONField(null=True)
    education =  JSONField(null=True)
    experience = JSONField(null=True)
    skills = JSONField(null=True)


    def __str__(self):
        return self.fullname

class Field(models.Model):
    user = models.ForeignKey(User ,  on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title + ' - ' + str(self.user)
        
class Project(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(default="none")
    code_file = models.FileField(upload_to='projects/',null=True)
    bugs = models.TextField(default="No bugs found ")
    comments = JSONField(null=True)
    def __str__(self):
        return str(self.id)+' - ' + self.title

class Photo(models.Model):
    project = models.ForeignKey(Project , on_delete=models.CASCADE)
    legend = models.TextField(default="")
    image = models.ImageField( upload_to='photos/', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.legend

# class Comment(models.Model):
#     project =  models.ForeignKey(Project , on_delete=models.CASCADE)
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     comment = models.TextField(default="")
#     jaims = models.ManyToManyField(User,default=0,blank=True,related_name='jaims')
#     timeSent = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.comment

        
# class RepondreComment(models.Model):
#     comment =  models.ForeignKey(Comment , on_delete=models.CASCADE)
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     reponse =  models.TextField(default="")
#     jaims = models.IntegerField(default=0,blank=True)
#     timeSent = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.reponse
