from django.shortcuts import render

# added by me
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views/ functions here.


def home(request):
    return render(request, 'home/index.html', {'today': datetime.today()})


@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})


def services(request):
    return render(request, 'home/services.html', {})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact = request.POST.get("phone-number")
        message = request.POST.get("message")

        data = {
            'name': name,
            'email': email,
            'contact': contact,
            'message': message
        }
        message = '''
        New message: {}

        from: {}
        
        '''.format(data['message'], data['email'])
        send_mail(data['contact'], data['email'],
                  '', ['mgqolozana123@gmail.com'])
        return HttpResponse('Submitted Successfully!')
    return render(request, 'home/contact.html', {})


def map(request):
    return render(request, 'home/map.html', {})


def products(request):
    return render(request, 'home/products.html', {})
