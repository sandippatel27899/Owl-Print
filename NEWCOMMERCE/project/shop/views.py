from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView
from .models import Profile, Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
# Create your views here.


def SignupView(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            password = form.cleaned_data['password1']
            user = authenticate(username=user.username, password=password)
            login(request, user)
            return redirect("products")
        # validation 
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

class ProductListView(ListView):

    model = Product


class ProductDetailView(DetailView):
    
    model = Product
    

def filter(request):
    price_filter = Product.objects.all()
    min = request.GET.get('min')
    max = request.GET.get('max')
    if min:
        price_filter = price_filter.filter(price__gte= min)
    if max:
        price_filter = price_filter.filter(price__lte= max)
    context = {"object_list": price_filter,
                "min" : min,
                "max" : max
            }
    return render(request, 'shop/product_list.html', context)

def search(request):
    q = request.GET.get('q')
    posts = None
    if not q:
        return redirect("products")
    
    products = Product.objects.filter(name__icontains = q)
    
    context = { 'object_list': products}
    return render(request, 'shop/product_list.html', context)


@login_required(login_url="/accounts/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("product-detail", id)


@login_required(login_url="/accounts/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def cart_detail(request):
    GST = 0.18
    cart = Cart(request)
    print(cart.cart)
    subtotal = sum([float(p['quantity']) * float(p['price']) for p in cart.cart.values()])
    tax = GST*subtotal
    total = subtotal + tax
    context = { 
        "subtotal" : subtotal,
        "tax": tax,
        "total": total,
    }
    return render(request, 'cart/cart_detail.html', context)
