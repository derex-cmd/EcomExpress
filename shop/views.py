from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Product
from math import ceil
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import Contact
from .forms import ContactForm



def index(request):
    products = Product.objects.all()
    n = len(products)
    products_per_slide = 4
    nSlides = n // products_per_slide + ceil((n / products_per_slide) - (n // products_per_slide))
    allProds = []
    for i in range(0, n, products_per_slide):
        allProds.append(products[i:i + products_per_slide])
    params = {'allProds': allProds, 'range': range(1, nSlides + 1)}  # Fixed range to include last slide
    return render(request, 'shop/index.html', params)

def productview(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    return render(request, 'shop/productview.html', {'product': product})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            contact = form.save()
            # Return a success response
            return JsonResponse({'status': 'success'})
        else:
            # Return an error response with form errors
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    else:
        form = ContactForm()

    return render(request, 'shop/contact.html', {'form': form})
