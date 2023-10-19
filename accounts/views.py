from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserProfile
import re



def signin(request):
    if request.method == 'POST' and 'btnlogin' in request.POST:
        username = request.POST['user']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            if 'rememberme' not in request.POST:
                request.session.set_expiry(0)
            auth.login(request,user)
            #messages.success(request,'You are logged in successfully')
        else:
            messages.error(request,'username and password are incorrect')
        return redirect('signin')
    else:
        return render(request , 'accounts/signin.html')


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('/')


def signup(request):
    if request.method == 'POST' and 'btnsignup' in request.POST:
        #variables for fieles
        first_name = None
        last_name = None
        address = None
        address2 = None
        city = None
        state = None
        zip_number = None
        email = None
        username = None
        password = None
        terms = None
        is_added = None
        
        #GET value from form
        if 'first_name' in request.POST: first_name = request.POST['first_name']
        else: messages.error(request,'Error in frist name')
        if 'last_name' in request.POST: last_name = request.POST['last_name']
        else: messages.error(request,'Error in last name')
        if 'address' in request.POST: address = request.POST['address']
        else: messages.error(request,'Error in  address')
        if 'address2' in request.POST: address2 = request.POST['address2']
        else: messages.error(request,'Error in  address 2')
        if 'city' in request.POST: city = request.POST['city']
        else: messages.error(request,'Error in  city')
        if 'state' in request.POST: state = request.POST['state']
        else: messages.error(request,'Error in  state')
        if 'zip_number' in request.POST: zip_number = request.POST['zip_number']
        else: messages.error(request,'Error in  zip number')
        if 'email' in request.POST: email = request.POST['email']
        else: messages.error(request,'Error in  email')
        if 'username' in request.POST: username = request.POST['username']
        else: messages.error(request,'Error in  user name')
        if 'password' in request.POST: password = request.POST['password']
        else: messages.error(request,'Error in  password')
        if 'terms' in request.POST: terms = request.POST['terms']
        
        #check all values
        if first_name and last_name and address and address2 and city and state and zip_number and email and username and password:
            if terms == 'on':
                #check if username
                if User.objects.filter(username=username).exists():
                    messages.error(request,'User name is taken')
                else:
                    #check email is taken
                    if User.objects.filter(email=email).exists():
                        messages.error(request,'E-Mail is taken')
                    else:
                        patt = "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$" #صيغة الايميل
                        if re.match(patt,email):
                            # add User
                            user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password) #حقل ديجانجو = متغير الخاص بي
                            user.save()
                            # add user profile
                            userprofile = UserProfile(user=user,address=address,address2=address2,city=city,state=state,zip_number=zip_number)
                            userprofile.save()
                            #clear fields
                            first_name = ''
                            last_name = ''
                            address = ''
                            address2 = ''
                            city = ''
                            state = ''
                            zip_number = ''
                            email = ''
                            username = ''
                            password = ''
                            terms = None
                            #Success message
                            messages.success(request,'Your account has been created successfully')
                            is_added = True
                        else:
                            messages.error(request,'Invalid e-mail')
            else:
                messages.error(request,'You must agree to the terms')
        else:
            messages.error(request, 'Check empty fields')
        return render(request, 'accounts/signup.html',{
                'first_name': first_name,
                'last_name': last_name,
                'address': address,
                'address2': address2,
                'city': city,
                'state': state,
                'zip_number': zip_number,
                'email': email,
                'username': username,
                'password': password,
                'is_added': is_added,
        })
    else:
        return render(request , 'accounts/signup.html')


def profile(request):
    if request.method == 'POST' and 'btnsave' in request.POST:
        messages.info(request,'This is POST and btnsave')
        return redirect('profile')
    else:
        return render(request,'accounts/profile.html')