
from django.db import models

class destination(models.Model):
    Dest_Name = models.CharField(max_length=50,primary_key=True)
    Dest_Desc = models.CharField(max_length=255)
    Dest_Img = models.ImageField(upload_to='img')     
    
    def __str__(self):
        return self.Dest_Name

class Place(models.Model):
    State = models.ForeignKey(destination, on_delete=models.CASCADE)
    Place_Name = models.CharField(max_length=50, default='Any' , primary_key=True)
    Day=models.CharField(max_length=6 ,default='1/Day')
    Night=models.CharField(max_length=7 ,default='1/Night')
    Place_Desc = models.TextField()
    Place_high=models.TextField(default='ALL are High')
    Place_Img = models.ImageField()
    Place_price = models.FloatField()
    
    def __str__(self) :
        return self.Place_Name
    
class sliderImage(models.Model):
    sliderImg=models.ImageField()
    sliderName=models.ForeignKey(destination,on_delete=models.CASCADE)
    sliderParent=models.ForeignKey(Place,on_delete=models.CASCADE)
    

class contactModel(models.Model):
    Name=models.CharField(max_length=10)
    Email=models.EmailField()
    Contact=models.IntegerField()
    Message=models.TextField()
   
    def __str__(self):
        return self.Name
    
    
    
class reviewModel(models.Model):
    Name=models.CharField(max_length=40)
    Subject=models.CharField(max_length=50)
    Content=models.TextField()
    
    