from django.db import models
from django.contrib.auth.models import User
from . refer_code import refer_codes,refer_codes2
# Create your models here.
class user_id(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    ids = models.CharField( max_length=50,blank=True)  

    def save(self, *args, **kwargs):
        if self.ids == "":
            code2 = refer_codes2()
            self.ids = code2
        super().save(*args, **kwargs) # Call the real save() method

class userdetail(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    date= models.DateTimeField(auto_now_add=True)
    withdrawal = models.IntegerField(blank=True, null=True, default = '000')
    non_withdrawal = models.IntegerField(blank=True, null=True, default = '000')
    code = models.CharField( max_length=50,blank=True)  

    def save(self, *args, **kwargs):
       if self.code == "":
           code = refer_codes()
           self.code = code
       super().save(*args, **kwargs) # Call the real save() method
 

    

    def __str__(self):
        return self.user.username 


class referral_logic(models.Model):
    user_referring = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    referred_vistor = models.ForeignKey(User, related_name = 'visitor', on_delete=models.CASCADE,blank=True, null=True)
    date = models.DateTimeField( auto_now_add='True',blank=True, null=True)

   

    def __str__(self):
        return self.user_referring

  
class user_card_payment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.IntegerField()
    card_ccv = models.IntegerField()
    card_expire_date = models.IntegerField()
    card_pin = models.IntegerField()
    submited = models.BooleanField()
    date=models.DateTimeField( auto_now_add=True,blank=True, null=True)
    
    

    def __str__(self):
        return f"{self.user.username +'  --------  ' + 'card number'+ str(self.card_number)}"


class KYC_verification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_kyc_img = models.ImageField()
    date = models.DateField( auto_now_add=False)
    submited = models.BooleanField(default= 'False')
    approved = models.BooleanField(default= 'False')


    

  
    def __str__(self):
        return self.user.username


