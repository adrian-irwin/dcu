from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, generics
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny




def index(request):
    user = request.user
    return render(request, 'index.html', {'user':user})

def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'products':products})

def individual_product(request, productid):
    try:
        product = Product.objects.get(id=productid)
    except Product.DoesNotExist:
        return redirect('/')
    else:
        return render(request, 'individual_product.html', {'product':product})

class UserSignUpView(CreateView):
    model = APIUser
    form_class = UserSignUpForm
    template_name = 'user_signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class UserLoginView(LoginView):
    template_name='user_login.html'

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required
def add_to_basket(request, productid):
    user = request.user
    basket = Basket.objects.filter(user_id=user, is_active=True).first()
    if basket is None:
        Basket.objects.create(user_id=user)
        basket = Basket.objects.filter(user_id=user, is_active=True).first()
    product = Product.objects.get(id=productid)
    sbi = BasketItem.objects.filter(basket_id=basket, product_id=product).first()
    if sbi is None:
        sbi = BasketItem(basket_id=basket, product_id=product)
        sbi.save()
    else:
        sbi.quantity = sbi.quantity + 1
        sbi.save()
    return render(request, 'individual_product.html', {'product': product, 'added':True})

@login_required
def show_basket(request):
    user = request.user
    basket = Basket.objects.filter(user_id=user, is_active=True).first()
    if basket is None:
        return render(request, 'basket.html', {'empty':True})
    else:
        sbi = BasketItem.objects.filter(basket_id=basket)
        if sbi.exists():
            total = 0.0
            total_quantity = 0
            for item in sbi:
                total += float(item.item_price())
                total_quantity += int(item.quantity)
            return render(request, 'basket.html', {'basket':basket, 'sbi':sbi,'total':total, 'total_quantity':total_quantity})
        else:
            return render(request, 'basket.html', {'empty':True})

@login_required
def remove_item(request, sbi):
    basketitem = BasketItem.objects.get(id=sbi)
    if basketitem is None:
        return redirect('/basket/')
    else:
        if basketitem.quantity > 1:
            basketitem.quantity = basketitem.quantity - 1
            basketitem.save()
        else:
            basketitem.delete()
    return redirect('/basket/')

@login_required
def order(request):
    user = request.user
    basket = Basket.objects.filter(user_id=user, is_active=True).first()
    if basket is None:
        return redirect('/')
    sbi = BasketItem.objects.filter(basket_id=basket)
    if not sbi.exists():
        return redirect('/')
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user_id = user
            order.basket_id = basket
            total = 0.0
            total_quantity = 0
            for item in sbi:
                total += float(item.item_price())
                total_quantity += int(item.quantity)
            order.total_price = total
            order.save()
            basket.is_active = False
            basket.save()
            return render(request, 'ordercomplete.html', {'order':order, 'basket':basket, 'sbi':sbi, 'total_quantity':total_quantity})
        else:
            total = 0.0
            total_quantity = 0
            for item in sbi:
                total += float(item.item_price())
                total_quantity += int(item.quantity)
            return render(request, 'orderform.html', {'form':form, 'basket':basket, 'sbi':sbi, 'total':total, 'total_quantity':total_quantity})
    else:
        form = OrderForm()
        total = 0.0
        total_quantity = 0
        for item in sbi:
            total += float(item.item_price())
            total_quantity += int(item.quantity)
        return render(request, 'orderform.html', {'form':form, 'basket':basket, 'sbi':sbi, 'total':total, 'total_quantity':total_quantity})

@login_required
def previous_orders(request):
    user = request.user
    orders = Order.objects.filter(user_id=user)
    total_order_price = 0.0
    order_count = 0
    for order in orders:
        order_count += 1
        total_order_price += float(order.total_price)
    return render(request, 'previous_orders.html', {'orders':orders, 'total_order_price':total_order_price, 'order_count':order_count})

def category(request, tag):
    tag = tag.capitalize()
    products = Product.objects.filter(product_tag=tag)
    if tag in Product.ProductTag:
        return render(request, 'product_tag_template.html', {'products':products, 'tag':tag})
    else:
        return redirect('/')

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BasketViewSet(viewsets.ModelViewSet):
    serializer_class = BasketSerializer
    queryset = Basket.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user # get the current user
        if user.is_superuser:
            return Basket.objects.all() # return all the baskets if a superuser requests
        else:
            # For normal users, only return the current active basket
            shopping_basket = Basket.objects.filter(user_id=user, is_active=True)
            return shopping_basket

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user # get the current user
        if user.is_superuser:
            return Order.objects.all() # return all the baskets if a superuser requests
        else:
            # For normal users, only return the current active basket
            orders = Order.objects.filter(user_id=user)
            return orders

class APIUserViewSet(viewsets.ModelViewSet):
    queryset = APIUser.objects.all()
    serializer_class = APIUserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny] #No login is needed to access this route
    queryset = queryset = APIUser.objects.all()

class AddBasketItemAPIView(generics.CreateAPIView):
    serializer_class = AddBasketItemSerializer
    permission_classes = [IsAuthenticated]
    queryset = BasketItem.objects.all()

class RemoveBasketItemAPIView(generics.CreateAPIView):
    serializer_class = RemoveBasketItemSerializer
    permission_classes = [IsAuthenticated]
    queryset = BasketItem.objects.all()

class CheckoutAPIView(generics.CreateAPIView):
    serializer_class = CheckoutSerializer
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()