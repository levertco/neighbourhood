from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User





#neigbourhood model
class Neigbourhood(models.Model):
    
    neighbourhood_name=models.CharField(max_length=60)
    neighbourhood_location=models.CharField(max_length=60)
    occupant_count=models.PositiveIntegerField()
    admin=models.ForeignKey(User,null=True,on_delete=models.CASCADE)

    @classmethod
    def create_neigborhood():
        pass

    @classmethod
    def delete_neigborhood():
       pass

    @classmethod
    def  find_neigborhood(neigborhood_id):
        pass

    @classmethod
    def update_neighborhood():
        pass

    @classmethod
    def update_occupants():
        pass

        


class User_profile(models.Model):
    name=models.CharField(max_length=60)
    neigbourhood=models.ForeignKey(Neigbourhood,null=True,on_delete=models.CASCADE)
    email=models.EmailField()
    user_id=models.ForeignKey(User,null=True)
    profile_photo=models.ImageField(upload_to='gallery/',blank=True,null=True)


    @classmethod
    def get_profile(cls): 
        profile=User_profile.objects.all()
        return profile


class Business(models.Model):
    Bizname=models.CharField(max_length=60)
    user=models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    neigbourhood=models.ForeignKey(Neigbourhood,on_delete=models.CASCADE)
    biz_email=models.EmailField()
    biz_desc=models.CharField(max_length=100)

    @classmethod
    def search_biz(cls,search_term):
        
        business=cls.objects.filter(Bizname__icontains=search_term)
        return business


    @classmethod
    def create_business():
        pass

    @classmethod
    def delete_business():
        pass

    @classmethod
    def find_business(business_id):
        pass

    @classmethod
    def update_business():
        pass

class Post(models.Model):
    image=models.ImageField(upload_to='gallery/',blank=True,null=True)
    image_caption=models.TextField(max_length=200)
    profile=models.ForeignKey(User_profile,null=True,blank=True)
    postdate=models.DateTimeField(auto_now_add=True,null=True)
    user = models.ForeignKey(User, null=True)        


    class Meta:
        ordering=['-postdate']

  
    @classmethod
    def my_post(cls):
        
        posts = cls.objects.all()
        return posts

    def save_post(self):
        
        self.save()   

    @classmethod
    def get_post_by_id(cls,post_id):
        
        posts=cls.objects.get(id=post_id)

        return posts 

    @classmethod
    def search_by_user(cls,search_term):
        
        posts=cls.objects.filter(post_icontains=search_term)
        return posts


    @classmethod
    def delete_post():    
       pass


    @classmethod
    def update_caption():   
       pass








def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = User_profile.objects.create(user_id=kwargs['instance'])


post_save.connect(create_profile, sender=User)





    
