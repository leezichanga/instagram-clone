from django.test import TestCase
from .models import Image,Profile,Comment
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    #setup method
    def setUp(self):
        #set up user class
        self.new_user = User(username="liz",email="elizabethichanga@yahoo.com")
        self.new_user.save()
        #set up profile class
        self.Profile(bio="Feeling natural",user=self.new_user)
        self.save_profile()

        # self.user.add(self.liz)

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Profile))

    def test_save_profile(self):
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete_profile(self):
        self.save_profile()
        self.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)<1)

    def test_find_profile(self):
        self.save_profile()
        me = Profile.objects.all()
        profiles = Profile.find_profile('liz')
        self.assertEqual(profiles,profiles)

    def test_get_profile(self):
        self.save_profile()
        prof = Profile.get_profile()
        self.assertEqual(len(prof),1)

class ImageTestClass(TestCase):
    def setUp(self):
        #set up user class
        self.new_user = User(username="liz",email="elizabethichanga@yahoo.com")
        self.new_user.save()
        #set up for profile class
        self.new_profile=Profile(bio="I am awesome",user=self.new_user)
        self.new_profile.save()
        #set up for Image class
        self.flower=Image(caption="legacy goals",likes=200,profile=self.new_profile)
        self.flower.save_image()

    def tearDown(self):
        Profile.objects.all().delete()
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.flower,Image))

    def test_save_image(self):
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_image(self):
        self.flower.save_image()
        self.flower.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)<1)

    def test_get_images(self):
        self.flower.save_image()
        images = Image.get_images()
        self.assertEqual(len(images),1)

    def test_get_image_by_id(self):
        pass
