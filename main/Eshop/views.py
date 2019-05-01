from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Category
from .forms import CategoryForm
from .forms import CategoryModelForm

from .models import Product
from .forms import ProductModelForm

from .models import Cart
from .models import CartItem

from .models import Order

from .models import Adress
from .forms import AdressForm

from .forms import getQuantity

from rest_framework import viewsets
from .serializers import ProductSerializer


from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from pprint import pprint

# Create your views here.
def home(request):
    # account_obj = Account.objects.all()
    # account_obj = Account.objects.raw("SELECT * FROM accounts_account;")
    # for p in Person.objects.raw('SELECT * FROM Product'):
    #     print(p)
    allProducts = Product.objects.all()

    kortingen = Product.objects.filter(korting__gt=0)
    kortingen3 = kortingen[:3]
    niewste = Product.objects.all().order_by('-timestamp')
    niewste3 = niewste[:3]

    context = {
            'niewste': niewste3,
            'kortingen': kortingen3
        }
    return render(request, 'Eshop/home.html', context)

# form die enkel forms formule gebruikt
def adminCustom(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['soort']
            print(name)
            myCategory = Category()
            myCategory.soort = name
            myCategory.publish()
    form = CategoryForm()

    context = {
            'categorys': Category.objects.all(),
            'form': form
            }
    return render(request, 'Eshop/adminCustom.html', context)

def adminCustom2(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CategoryModelForm(request.POST)
            if form.is_valid():
                print("valid")
                name = form.cleaned_data['soort']
                myCategory = Category()
                myCategory.soort = name
                myCategory.publish()

        form = CategoryModelForm()

        context = {
                'categorys': Category.objects.all(),
                'form': form
                }
        return render(request, 'Eshop/adminCustom2.html', context)
    else: 
        return redirect('Eshop:home')  
def createProduct(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            print("valid")
            # naam = form.cleaned_data['naam']
            # prijs = form.cleaned_data['prijs']
            # btw = form.cleaned_data['btw']
            # merk = form.cleaned_data['merk']

            # myProduct = Product()
            # myProduct.naam = naam

            # #myProduct.category = category
            # #user = User.objects.filter(username='CoreyMS').first()


            # myProduct.prijs = prijs
            # myProduct.btw = btw
            # myProduct.merk = merk
            # myProduct.publish()
            #print(form.cleaned_data['category'])
            CategoryId = form['category'].value()
            category2 = Category.objects.get(id=CategoryId)
            print(category2)

            post2 = Product(naam=form.cleaned_data['naam'],
                        category=category2,
                        prijs = form.cleaned_data['prijs'],
                        btw = form.cleaned_data['btw'],
                        korting=form.cleaned_data['korting'],
                        merk = form.cleaned_data['merk'],
                        image = form.cleaned_data['image'],
                        productCount= form.cleaned_data['productCount'])
            post2.publish()
        else:
            print("not valid") 
            #print(form.cleaned_data['category'])
            CategoryId = form['category'].value()
            category2 = Category.objects.get(id=CategoryId)
            print(category2)

            post2 = Product(naam=form.cleaned_data['naam'],
                        category=category2,
                        prijs = form.cleaned_data['prijs'],
                        btw = form.cleaned_data['btw'],
                        merk = form.cleaned_data['merk'],
                        image = form.cleaned_data['image'],
                        productCount= form.cleaned_data['productCount'])
            # Product.objects.create(naam=form.cleaned_data['naam'],
            #             category=category2,
            #             prijs = form.cleaned_data['prijs'],
            #             btw = form.cleaned_data['btw'],
            #             merk = form.cleaned_data['merk'])
            post2.publish()      
    form = ProductModelForm()

    context = {
            'form': form
            }
    return render(request, 'Eshop/createProduct.html', context)



def allProducts(request):

    alleProducten = Product.objects.all()
    context = {
        'products': alleProducten,
        }
    return render(request, 'Eshop/allProducts.html', context)

def logout_request(request):
    logout(request)
    messages.info(request, "logged out")
    return redirect('Eshop:home')  

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account created : {username}")
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect('Eshop:home')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}form.error_messages[msg]")
            return render(request = request,
                    template_name = "Eshop/register.html",
                    context={"form":form})

    form = UserCreationForm
    return render(request,
                   'Eshop/register.html',
                   context={"form": form})

def productDetailPage(request, id):
    print('id {}'.format(id))
    obj = Product.objects.get(id = id)
    context = {
        "object":obj
    }
    return render(request, 'Eshop/product_detail.html', context)

def cart(request):
    try:
        the_id = request.session['cart_id']
        the_count = request.session['items_total']
    except:
        the_id = None
        the_count = 0
    if the_id:
        cart =  Cart.objects.get(id=the_id)
        context = {
            'cart': cart,
            'count': the_count
        }
    else:
        context = {"empty": True}
       
    #pprint(vars(alleCarts))
    return render(request, 'Eshop/cart.html', context)

def add_to_cart(request, id):
    request.session.set_expiry(12000000)
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)
    productIns = None
    try: 
        productIns = Product.objects.filter(id=id).first()
    except product.DoesNotExist:
        pass
    except:
        pass

    if request.method == 'POST':
        print("valid")
        qty = request.POST.get('qty')
        print(qty)
    # changed
    # { "cart item object", "true/false"}
    cart_item, created = CartItem.objects.get_or_create(cart = cart, product = productIns, quantity= qty)
    if created:
        print("itemGecreerd")
    # changed



        
    # if not cart_item in cart.items.all():
    #     cart.items.add(cart_item)
    # else:
    #     cart.items.remove(cart_item)
    
    new_total = 0.00
    line_total= 0.00
    for item in cart.cartitem_set.all():
        line_total += float(item.product.prijs) * item.quantity
        new_total += float(item.product.prijs)

    request.session['items_total'] = cart.cartitem_set.count()
    cart.total = line_total
    #cart.total = new_total 
    print(cart.total)
    cart.save()

    return redirect('Eshop:cart')


def deleteFromCard(request, id):
    request.session['items_total'] =  request.session['items_total'] -1
    # cart = Cart.objects.all()[0]
    # productIns = None
    # try: 
    #     productIns = Product.objects.filter(id=id).first()
    #     prijsWeg = productIns.prijs
    #     cart.products.remove(productIns)
    #     cart.total = cart.total - prijsWeg
    #     cart.save()
    # except product.DoesNotExist:
    #     pass
    # except:
    #     pass
    print("het id is", id)
    cartId = request.session['cart_id']
    cart = Cart.objects.get(id = cartId)
    print(cart)
    product = Product.objects.get(id = id)
    print(product)
    cart_item = CartItem.objects.get(cart = cart, product = product)
    cart_item.delete()

    new_total = 0.00
    line_total= 0.00
    for item in cart.cartitem_set.all():
        line_total += float(item.product.prijs) * item.quantity
        new_total += float(item.product.prijs)

    request.session['items_total'] = cart.cartitem_set.count()
    cart.total = line_total
    cart.save()
    #cart.total = new_total 

    #delete nog
    return redirect('Eshop:cart')


def order(request, id):
    context = { }
    try:
        the_id = request.session['cart_id']
        the_count = request.session['items_total']
    except:
        the_id = None
        the_count = 0

    cart = Cart.objects.get(id = the_id)
    print(cart)
    print(cart.total)
    OrderAanmaken = Order(order_id= "AAAA",
                    #billingAdress = AdressInstance,
                    cart = cart,
                    status = "created",
                    shipping_total = 5 ,
                    total = cart.total)

    
    if request.method == 'POST':
        form = AdressForm(request.POST)
        if form.is_valid():
            print("valid")

            straat = form['straat'].value()
            nr = form['nr'].value()
            stad = form['stad'].value()
            postcode = form['postcode'].value()
            land = form['land'].value()

            AdressInstance, created = Adress.objects.get_or_create(
                straat = straat,
                nr = nr,
                stad = stad,
                postcode =  postcode,
                land = land
            )

            if created:
   
                OrderAanmaken.billingAdress = AdressInstance
                OrderAanmaken.publish()
                # context = {
                #     'order': OrderAanmaken,  
                #     'count': the_count,
                #     'form': form
                #     }
                del request.session['cart_id']
                del request.session['items_total']
                return redirect('Eshop:home')

            else:
               print ("error")
    else:
        context = {}
        form = AdressForm(request.POST)
        context = {
            'order': OrderAanmaken,  
            'count': the_count,
            'form': form
            }
    
    return render(request, 'Eshop/order.html', context)


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['michiel.roelants@student.ehb.be'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('Eshop:success')
    return render(request, "Eshop/emailView.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer