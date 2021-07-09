from django.shortcuts import render

def view_bag(request):
    """ A view to return shopping bag """

    return render(request, 'bag/bag.html')