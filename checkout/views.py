from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        # manually prevents user accessing the url by typing /checkout
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
    'order_form': order_form,
    'stripe_public_key': 'pk_test_51JJ10gKOsXc51blmj5NHcwnUQXulZqtU6fpGpJsZbEDtwjTiZqMMG0mfLp9hhXq01PuSXONI029jA5UcVLgT0ad700UINkzIZY',
    'client_secret': 'test client secret'
    }

    return render(request, template, context)