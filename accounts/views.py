from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserProfile
from products.models import Product
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


from django.contrib import messages

def profile(request):
    if request.method == 'POST' and 'btnsave' in request.POST:
        if request.user is not None and not request.user.is_anonymous:
            userprofile = UserProfile.objects.get(user=request.user)
            if all(request.POST.get(key) for key in ['first_name', 'last_name', 'address', 'address2', 'city', 'state', 'zip_number', 'email', 'username', 'password']):
                request.user.first_name = request.POST['first_name']
                request.user.last_name = request.POST['last_name']
                userprofile.address = request.POST['address']
                userprofile.address2 = request.POST['address2']
                userprofile.city = request.POST['city']
                userprofile.state = request.POST['state']
                userprofile.zip_number = request.POST['zip_number']
                # request.user.email = request.POST['email']
                # request.user.username = request.POST['username']
                if not request.POST['password'].startswith('pbkdf2_sha256$600000$'):#pbkdf2_sha256$600000$<---->name of dp
                    request.user.set_password(request.POST['password'])
                request.user.save()
                userprofile.save()
                auth.login(request,request.user)#sve login in state change data in profile
                messages.success(request, 'Your data has been saved')
            else:
                messages.error(request, 'Check your values and elements')
        return redirect('profile')
    else:
        #if request.user.is_anonymous: return redirect('/')
        #if request.user.id == None: return redirect('/')
        #حل لمشكلة لدخول صفحة البروفايل بطريقة غير مباشرة ولكن في ادق منوا
        
        if request.user is not None:
            context = None
            #if not request.user.is_anonymous:==if request.user.id !=None      the same of answe and the peats of enter profile in state not allow
            if not request.user.is_anonymous:
                userprofile = UserProfile.objects.get(user=request.user)
                context = {
                'first_name':request.user.first_name,
                'last_name':request.user.last_name,
                'address':userprofile.address,
                'address2':userprofile.address2,
                'city':userprofile.city,
                'state':userprofile.state,
                'zip_number':userprofile.zip_number,
                'email':request.user.email,
                'username':request.user.username,
                'password':request.user.password,
                }
            return render(request,'accounts/profile.html',context)
        else:
            return redirect('profile')
        


def product_favorite(request, product_id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        product_favorite = Product.objects.get(pk=product_id)
        if UserProfile.objects.filter(user=request.user, product_favorites=product_favorite).exists():
            messages.success(request, 'Already added to favorites')
        else:
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile.product_favorites.add(product_favorite)
            messages.success(request, 'Product has been added to favorites')
    else:
        messages.error(request,'You must be logged in')
    return redirect('/products/' + str(product_id))


def show_favorite(request):
    context = None
    if request.user.is_authenticated and not request.user.is_anonymous:
        user_info = UserProfile.objects.get(user=request.user)
        products = user_info.product_favorites.all()
        context = {'products':products}
    return render(request,'products/products.html',context)





