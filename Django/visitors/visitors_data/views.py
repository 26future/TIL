from django.shortcuts import render, redirect
from .models import Visitor
import qrcode


# Create your views here.

def home(request):
    context = {

    }
    return render(request, 'visitors_data/home.html', context)


def citizen(request): # POST
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     number = request.POST.get('number')

    #     visitor = Visitor(name=name, number=number)
    #     visitor.save()
    
    #     return redirect('visitors_data:detail', visitor.pk)

    # else:
    context = {

    }
    return render(request, 'visitors_data/citizen.html', context)

def foreigner(request): # POST
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     number = request.POST.get('number')

    #     visitor = Visitor(name=name, number=number)
    #     visitor.save()
    
    #     return redirect('visitors_data:detail', visitor.pk)

    # else:
    context = {

    }
    return render(request, 'visitors_data/foreigner.html', context)

def confirm(request):
    name = request.GET.get('name')
    number = request.GET.get('number')

    context = {
        'name': name,
        'number': number,
    }
    return render(request, 'visitors_data/confirm.html', context)

def qr(request):
    qr = qrcode.QRCode(version=2, error_correction=qrcode.constants.ERROR_CORRECT_H)
    url = 'www.naver.com'
    qr.add_data(url)
    qr.make
    img = qr.make_image(fill_color='black', back_color='white')
    img.save('naver_qrcode_sample.png')


    return render(request, 'visitors_data/qr.html')