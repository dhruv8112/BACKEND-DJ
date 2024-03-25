from django.db import models

# Create your models here.
class userModel(models.Model):
    userUsername = models.CharField(max_length=10)
    userFullName = models.CharField(max_length=20)
    userEmail = models.EmailField(max_length=50)
    userContact = models.IntegerField()
    userBirth=models.DateField(auto_now_add=True)
    userAddress=models.TextField()

    def _str_(self):
        return self.userUsername
    