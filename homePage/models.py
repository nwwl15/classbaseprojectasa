from django.db import models

# Create your models here.
class plans(models.Model):
    plan_name = models.CharField( max_length=50)
    plan_max_pay = models.CharField( max_length=50)
    plan_min_pay = models.CharField( max_length=50)
    plan_duration = models.CharField( max_length=50)
    plan_min_pay = models.CharField( max_length=50)
    plan_url = models.URLField( max_length=200,blank=True, null=True)

    def __str__(self):
        return self.plan_name


class home_page(models.Model):
    site_name = models.CharField( max_length=50,blank=True, null=True)
    site_contact_number = models.CharField( max_length=200,blank=True, null=True)
    site_top_investor = models.ForeignKey("home_page_investor", on_delete=models.CASCADE,blank=True, null=True)
    site_disc = models.TextField(blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)
    facebook_link = models.URLField( max_length=200,blank=True, null=True)
    tweeter_link = models.URLField( max_length=200,blank=True, null=True)
    instargram_link = models.URLField( max_length=200,blank=True, null=True)

  


class home_page_investor(models.Model):
    name = models.CharField( max_length=50)
    person_pic = models.ImageField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True )
    date_join = models.DateField(auto_now=False , blank=True, null=True)
    rate = models.CharField( max_length=50)

    def __str__(self):
        return self.name

class home_page_slide(models.Model):
    img = models.ImageField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    url = models.URLField( max_length=200,blank=True, null=True)


    def __str__(self):
        return self.text

    

    
