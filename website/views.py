from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def portfolio(request):
    return render(request, 'website/portfolio.html')

def pricing(request):
    return render(request, 'website/pricing.html')

def contact(request):
    return render(request, 'website/contact.html')

def contact_submit(request):
    if request.method == 'POST':
        # Process the form submission data here
        # For example, you can access form data using request.POST.get('<field_name>')
        # Perform any necessary validation and save data to the database
        return HttpResponse('Thank you for your message! We will get back to you soon.')
    else:
        # Handle GET requests or other methods here
        return HttpResponse('Invalid request method.')
