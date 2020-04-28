from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.
from django.forms import inlineformset_factory
from django.shortcuts import redirect, render

from travello.forms import CreateUserForm, OrderForm
from travello.models import Destination, Customer, Order
from django.contrib import messages
import logging

logger=logging.getLogger("logger2")

def index(request):
    offers=Destination.objects.all()
    context={'offers':offers}

    return render(request,"pages/index.html",context)

def signup(request):
    formSet=CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            form.save()
            group= Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
                name=user.username,
                email=user.email
            )
            logger.info("new user signed up with this username =" + str(user.username))
            return redirect('signin')
        else:
            logger.error("sign up failed")
    context={'formSet':formSet}
    return render(request,"pages/signup.html",context)


def signin(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)

            logger.info(str(username) + " signed in successfully")

            return redirect('user_page',user.customer.id)
        else:
            logger.error("sign in failed")
    return render(request,"pages/signin.html")

def signout(request):
    logout(request)

    logger.info(" user signed out successfully")
    return redirect('')


@login_required(login_url='signin')
def userPage(request,pk):
    orderFormSet = inlineformset_factory(Customer, Order, fields=('destination', 'orderCount'),extra=1)
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    orderCount=orders.count()
    offers=Destination.objects.all()
    formSet = orderFormSet(queryset=Order.objects.none(),instance=customer)
    if request.method == "POST":
        formSet = orderFormSet(request.POST,instance=customer)
        for form in formSet:
            if form['orderCount'].value():
                if formSet.is_valid():
                    if formSet is not None:
                        formSet.save()

                        messages.add_message(request, messages.INFO, "successfully added to your reservation.")

                        orders=customer.order_set.all()
                        for order in orders:
                            if order.totalOrderCost is None:
                                order.totalOrderCost=order.destination.price * order.orderCount
                                order.save()
                        return redirect('user_page',pk)
            else:
                messages.add_message(request, messages.INFO, "please complete destination and adults sections")
                return redirect('user_page', pk)


    context={
        'offers':offers,
        'formSet':formSet,
        'orders':orders,
        'customer':customer,
        'orderCount':orderCount,
    }
    return render(request,'pages/userpage.html',context)

def reservations(request,pk):
    orderFormSet = inlineformset_factory(Customer, Order, fields=('destination', 'orderCount'), extra=3)
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    formSet=orderFormSet(queryset=Order.objects.all(),instance=customer)
    context={
        'formSet':formSet,
        'orders':orders,
        'customer':customer
    }
    return render(request,'pages/reservations.html',context)

def about(request):
    return render(request,'pages/about.html')