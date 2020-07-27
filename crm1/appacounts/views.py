from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.contrib import messages

# Create your views here.

from .models import *
from .forms import ordersForm, CreateUserForm, CustumerForm
from .filters import Orderfilter
from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def registerPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            #form.save()
            #user = form.cleaned_data.get('username')

            username = form.cleaned_data.get('username')

            # group = Group.objects.get(name='custumer')
            # user.groups.add(group)

            # custumer.objects.create(
            #     user=user,
            # )

            messages.success(request,'account was created for '+ username)

            return redirect('login')

    context = {'form':form}
    return render(request,'appacounts/register.html', context)

@unauthenticated_user
def loginPage(request):
    #  if request.user.is_authenticated:
    #     return redirect('home')
    #  else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request ,'username or password is  incorrect')

    context = {}
    return render(request, 'appacounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
@admin_only
def home(request):
    orderser = orders.objects.all()
    custumers = custumer.objects.all()

    total_custumers = custumers.count()

    total_orders = orderser.count()
    delivered = orderser.filter(status='Delivered').count()
    pending = orderser.filter(status='Pending').count()

    context = {'custumers':custumers,
             'orderser':orderser,
             'total_orders':total_orders,
             'delivered': delivered,
             'pending':pending
             }

    return render(request, 'appacounts/dashboard.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['custumer'])
def userPage(request):

    orders = request.user.custumer.orders_set.all()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()


    context = {'orders':orders,
             'total_orders':total_orders,
             'delivered': delivered,
             'pending':pending
             }


    return render(request, 'appacounts/users.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['custumer'])
def accountSettings(request):
    custumer = request.user.custumer
    form = CustumerForm(instance=custumer)

    if request.method == 'POST':
        form = CustumerForm(request.POST, request.FILES, instance=custumer)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request,'appacounts/account_settings.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])   
def products(request):
    products = product.objects.all()

    return render(request,'appacounts/products.html', {'products':products})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def custumers(request, pk_test):
     custumers = custumer.objects.get(id=pk_test)

     orders = custumers.orders_set.all()
     order_count = orders.count()

     myFilter = Orderfilter(request.GET, queryset=orders)
     orders = myFilter.qs

     context = {'custumers':custumers,
                 'orders':orders, 
                 'order_count':order_count,
                 'myFilter':myFilter,
                 }

     return render(request,'appacounts/custumer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(custumer, orders, fields=('product', 'status'), extra=10)
    custumers = custumer.objects.get(id=pk)
    formset = OrderFormSet(queryset=orders.objects.none() , instance=custumers)
    #form = ordersForm(initial={'custumer':custumers})
    if request.method == 'POST':
        #form = ordersForm(request.POST)
        formset = OrderFormSet(request.POST ,instance=custumers)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    
    context = {'formset':formset}
    return render(request, 'appacounts/order_form.html', context)


@login_required(login_url='login') 
@allowed_users(allowed_roles=['admin']) 
def updateorder(request, pk):

    order = orders.objects.get(id=pk)
    form = ordersForm(instance=order)

    if request.method == 'POST':
        form = ordersForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'appacounts/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = orders.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request,'appacounts/delete.html', context)