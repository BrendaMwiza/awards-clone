from rest_framework import serializers
from .models import Profile,Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("user_name","id","name","description","link","pic")

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("user_name","pro_pic","boi")