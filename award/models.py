from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    class Meta:
        db_table='profile'
    pro_pic = models.ImageField(upload_to='profile/',blank=True,null=True)
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    boi = models.TextField(max_length=300,null=True,default="bio")
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls,profile_item):
        pro = cls.objects.filter(user_name__name__icontains=profile_item)

    def __str__(self):
        return self.user_name.email

class Projects(models.Model):
    name = models.CharField(max_length =10)
    description = models.TextField(max_length =100)
    user_name = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
    project = models.ImageField(upload_to='links/', null=True)
    views = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    posting = HTMLField(null=True)
    profiles = models.ForeignKey(Profile,null=True)

    def save_project(self):
        self.save()  

    def delete_project(cls,id):
        project = cls.objects.get(PrimaryKey=id)
        project.delete()

    @classmethod
    def update_project(cls,update):
        project = cls.objects.filter(id=id).update(id=id)
        return project

    @classmethod
    def get_project_by_id(cls,id):
        project = cls.objects.get(PrimaryKey=id)
        return project

    @classmethod
    def search_user(cls,user_item):
        pic = cls.objects.filter(name__icontains=user_item)
