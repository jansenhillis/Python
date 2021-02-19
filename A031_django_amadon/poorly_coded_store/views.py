from django.shortcuts import render, redirect
from .models import Order, Product
from django.contrib import messages

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_model = float(Product.objects.get(id=request.POST['product_id']).price)
    total_charge = quantity_from_form * price_from_model

    print(f"Charging credit card... {total_charge}")
    order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    messages.info(request, f"We charged your credit card for ${ order.total_price }")

    return redirect('/confirm')

def confirm(request):
    net_spend = 0
    for order in Order.objects.all():
        net_spend += order.total_price

    messages.info(request, f"You have ordered { Order.objects.all().count() } \
        items so far and spent ${ net_spend } with Amadon.com!")

    return render(request, "store/checkout.html")