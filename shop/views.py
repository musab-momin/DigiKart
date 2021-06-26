from django.core.checks import messages
from django.db.utils import ProgrammingError
from shop.models import Product
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product
from .models import User as my_user
from .models import Order
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from .PayTm import Checksum
MERCHANT_KEY = 'TKXCejhTUgmeFnQj'

# Create your views here.
def index(request):
    # if request.user.is_anonymous:
    #     return redirect('/login')
    a = Product.objects.all()
    e = Product.objects.raw('select * from shop_Product where category=%s', ['Electronics'])
    c = Product.objects.raw('select * from shop_Product where category=%s', ['Cloths'])
    params = {'product': a, 'Eproduct': e, 'Cproduct': c}
    return render(request, 'index.htm', params)

def contact(request):
    return HttpResponse('This is contact page...')

def about(request):
    return HttpResponse('This is about page...')

def tracker(request):
    return HttpResponse('This is tracker page....')


def search(request):
    return HttpResponse('This is search page...')

def productview(request, id):
    #fetching product using id
    single_product = Product.objects.filter(id=id)
    print(single_product)
    return render(request, 'productview.htm', {'product': single_product[0]})

def checkout(request):
    if request.user.is_anonymous:
        messages.success(request, 'login before checkout')
        return redirect('/login')
    if request.method == 'POST':
        email = request.POST.get('email')
        bill_amount = request.POST.get('amount')
        print('This is email: ' , email, 'this is bill ', bill_amount)

        order = Order(email=email, amount = bill_amount)
        order.save()
        print('order is saved')        

        #making paytem request for money transfer
        data_dict = {
            'MID': 'LDYxUY86818217872725',
            'ORDER_ID': str(order.id),
            'TXN_AMOUNT': str(bill_amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/handlepayment',
        }

        data_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, MERCHANT_KEY)
        return render(request, 'paytm.htm', {'data_dict': data_dict})

    return render(request, 'checkout.htm')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        userpassword = request.POST.get('userpassword')
        print(username,'     ', userpassword)

        #authenticating
        user = authenticate(request, username=username, password=userpassword)
        print('got the user' , user)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, 'Invalid credentials...')
            return redirect('/login')
        
        
    return render(request, 'login.htm')


def registerUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        useremail = request.POST.get('useremail')
        userpassword = request.POST.get('userpassword')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        print(username," ", useremail," ", userpassword,' ',address,' ',city,' ',state,' ', zipcode)
        #saving user in database
        user = my_user(user_name = username, user_email = useremail, user_password = userpassword, address = address, city = city, state = state, zipcode = zipcode)
        # print(user)
        duser = User.objects.create_user(username=username, email=useremail, password=userpassword)
        duser.save()
        print('django user saved')
        user.save()
        messages.success(request, 'Your account created successfully...')
        return render(request, 'signup.htm')
        
    else:
        return render(request, 'signup.htm')

def logoutUser(request):
    logout(request)
    messages.success(request, 'logout successfully...')
    return redirect('/login')



#paytm reqeust comes here
@csrf_exempt
def handlepayment(request):

    #handling paytm reqeust 
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])


    return render(request, 'paymentstatus.htm', {'response': response_dict})

