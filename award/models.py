from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    class Meta:
        db_table='profile'
    pro_pic = models.ImageField(upload_to='profilePic/',blank=True,null=True)
    user_name = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
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

class Image(models.Model):
    name = models.CharField(max_length =10)
    description = models.TextField(max_length =100)
    user_name = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
    pic = models.ImageField(upload_to='pictures/', null=True)
    link = models.CharField(max_length=255)
    profiles = models.ForeignKey(Profile,null=True)

    def save_pic(self):
        self.save()  

    def delete_pic(cls,id):
        pic = cls.objects.get(PrimaryKey=id)
        pic.delete()

    @classmethod
    def update_pic(cls,update):
        pic = cls.objects.filter(id=id).update(id=id)
        return pic

    @classmethod
    def get_pic_by_di(cls,id):
        pic = cls.objects.get(PrimaryKey=id)
        return pic


    @classmethod
    def search_by_pic(cls,search_term):
        image = cls.objects.filter(pic__name__icontains=search_term)
        return image


class Rates(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ForeignKey(Image, on_delete=models.CASCADE,blank=True)

    # code from Django ratings on google
    design = models.IntegerField(choices=[(i,i) for i in range(1,11)], null=True)
    usability = models.IntegerField(choices=[(i,i) for i in range(1,11)], null=True)
    content = models.IntegerField(choices=[(i,i) for i in range(1,11)], null=True)
     

    def __str__(self):
        return f'{self.user.username} {self.pic.name} Rating'
