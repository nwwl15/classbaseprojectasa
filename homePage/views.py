from django.shortcuts import render, redirect
from . models import plans ,home_page ,home_page_investor,home_page_slide

# Create your views here.
def home(request):
    plan = plans.objects.all()
    home_pages_ex_logo = home_page.objects.all()
    home_page_investors = home_page_investor.objects.all()
    home_page_slides = home_page_slide.objects.all()
    conx = {
        'plan':plan,
        'home_pages_ex_logo' :home_pages_ex_logo,
        'home_page_investors' :home_page_investors, 
        'home_page_slides':home_page_slides,
        

         



    }
    return render(request,'html/home.html',conx)