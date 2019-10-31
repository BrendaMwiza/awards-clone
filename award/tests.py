from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Profile,Image
class ProfileTestClass(TestCase):
    def setUp(self):
        self.baby = Profile(pro_pic='award.jpg',boi='hlove coding')
    def test_instance(self):
        self.assertTrue(isinstance(self.baby,Profile))

    def test_save_profile(self):
        self.baby = Profile(pro_pic='award.jpg',boi='hlove coding')
        pro = Profile.objects.all()

    def test_add(self):
        baby = Profile.objects.filter(id=1)
        baby.update(pro_pic = 'award.jpg',boi = 'hlove coding')
        search = Profile.objects.filter(id=1)
        
    def test_delete(self):
        self.baby = Profile(pro_pic='award.jpg',boi='hlove coding')
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>=0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.profile= Profile(image='awards.jpg',boi='just')
        self.picture= Image( name ='Umwana',description = "been")

    def test_save_pic(self):
        self.picture= Image( name ='Umwana',description = "been")
        picture = Image.objects.all()

    def test_dele_pic(self):
        self.picture= Image( name ='Umwana', description = "been")
        delete = Image.objects.all()
        self.assertTrue(len(delete)>=0)

    def test_add_pic(self):
        image = Image.objects.filter(id=1)
        image.update(name ='award.jpg')
        search = Image.objects.filter(id=1)

    def test_pic_id(self):
        self.image = Image(name ='Umwana',description = "been")
       
        
        