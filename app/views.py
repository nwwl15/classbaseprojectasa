from django.shortcuts import render,redirect
from django.contrib.auth.models import User
user = User
from django .contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
# Create your views here.
from . models import userdetail,user_card_payment,KYC_verification,user_id
from . payment_update_form import update_payment

def loginuser(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
       
        if user.objects.filter(username=username):
            if user.objects.filter(email=email):
                usersxx= authenticate(request,username = username ,email=email ,password= password)
                login(request,usersxx)
                userd = user_id.objects.get(user =request.user)
                return redirect('room', pk = userd.ids)
                  
            else:
                messages.info(request,'email  does`t exist')
    
   
        else:
           messages.info(request,'Username and password does`t exist')


           return redirect('loginuser')
            
  

    return render(request,'html/login.html')
def registeruser(request):
    try:
         if request.method == 'POST':
             username = request.POST['username']
             email = request.POST['email']
             password = request.POST['password']
             password2 = request.POST['password2']
             if password == password2:
                 password = make_password(password)
                
                 if user.objects.filter(email=email).exists():
                     return redirect('registeruser')
                     messages.info(request,'the email is already taken')
                 elif user.objects.filter(username=username).exists():
                     
                     return redirect('registeruser')
                     messages.info(request,'Username and password can`t be empty')
                 elif username == '' and email == '':
                     return redirect('registeruser')
                     messages.info(request,'username can`t be empty')
                 else:
                     
                     users = user.objects.create(  username = username, email=email, password=password )
                     userx = userdetail.objects.create(user = users)
                     userxx = user_id.objects.create(user = users)
                     userx.save()
                     userxx.save()
                     users.save()
                     return redirect('loginuser')
             else:
                 messages.info(request,'passwored does`nt match')
                 return redirect('registeruser')
             
    except:
        messages.info(request,'some went wrong')
        return redirect('registeruser')
    return render(request,'html/register.html')
def room(request,pk):
    # userd = user.objects.get(id =pk)
    userd = user_id.objects.get(ids =pk)
                

    userx = request.user
    usercon = userdetail.objects.filter(user = userx)
    usercon_kyc = KYC_verification.objects.filter(user = userx)
    usercon_cardxx = user_card_payment.objects.filter(user = userx)
    # usercon_cardxx = user_card_payment.objects.all()
    conx = {
        'usercon' : usercon,
        'usercon_cardxx' : usercon_cardxx,
        'usercon_kyc' : usercon_kyc,
    }
    return render(request,'html/dashboard.html',conx)
def pending_payment(request,pk):
    # userd = user.objects.get(id =pk)
    userd = user_id.objects.get(ids =pk)
    userx = request.user
    usercon = userdetail.objects.filter(user = userx)
    usercon_kyc = KYC_verification.objects.filter(user = userx)
    usercon_cardxx = user_card_payment.objects.filter(user = userx)
    # usercon_cardxx = user_card_payment.objects.all()
    conx = {
        'usercon' : usercon,
        'usercon_cardxx' : usercon_cardxx,
        'usercon_kyc' : usercon_kyc,
    }
    return render(request,'html/pendfund.html',conx)
def profile(request,pk):
    userd = user.objects.get(id =pk)
    userd = user_id.objects.get(ids =pk)

    userx = request.user
    usercon = userdetail.objects.filter(user = userx)
    usercon_kyc = KYC_verification.objects.filter(user = userx)
    usercon_cardxx = user_card_payment.objects.filter(user = userx)
    # usercon_cardxx = user_card_payment.objects.all()
    conx = {
        'usercon' : usercon,
        'usercon_cardxx' : usercon_cardxx,
        'usercon_kyc' : usercon_kyc,
    }
    return render(request,'html/profile.html',conx)
def usercon_card(request,pk):
    # userd = user .objects.get(id =pk)
    userd = user_id.objects.get(ids =pk)

    userx = request.user
    usercon_cards = user_card_payment.objects.filter(user = userx)
    if request.method == 'POST':
        number = request.POST['number']
        ccv = request.POST['ccv']
        expiredate = request.POST['expiredate']
        pin = request.POST['pin']
        if number:
            users = user_card_payment.objects.create( user= userx , card_number = number, card_ccv=ccv, card_expire_date=expiredate, card_pin =pin, submited = False)
            users.save()
            return redirect('usercon_card', pk = userd.id)
        else:
            return redirect('room', pk = users.id)
            message.error(request,'the username is already taken')
              


    conx = {
      
    }
    return render(request,'card_payment.html',conx)


def usercon_card_update(request,pk):
    # userd = user.objects.get(id=pk)
    userd = user_id.objects.get(ids =pk)

    userx = request.user
    formx = update_payment(instance=userd)
    usercon = user_card_payment.objects.filter(user = userx)
    if request.method == 'POST':
        usercon = user_card_payment.objects.filter(user = userx)
        number = request.POST['number']
        ccv = request.POST['ccv']
        expiredate = request.POST['expiredate']
        pin = request.POST['pin']
        submited = True
        if usercon:
            for usercon in usercon:
                usercon.user = userx
                usercon.card_number = number
                usercon.card_ccv = ccv
                usercon.card_expire_date = expiredate
                usercon.card_pin = pin
                usercon.submited = submited
                usercon.save()
                print(usercon.card_number)
                return redirect('room', pk = userd.id)
                


        
      
        

    else:
        print('wong')
            

  

    conx = {
      'form':formx
    }
    return render(request,'card_payment_update.html',conx)




def logoutuser(request):
    logout(request)
    return redirect('home')
