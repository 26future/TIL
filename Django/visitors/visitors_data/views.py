from django.shortcuts import render, redirect
from .models import Visitor
import qrcode
from .forms import VisitorForm


# Create your views here.

def home(request):
    context = {

    }
    return render(request, 'visitors_data/home.html', context)

# def create(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/form.html', context)

def citizen(request): # POST
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            # visitor = form.save()
            form.save()
        return redirect('visitors_data:home')
    else:
        form = VisitorForm()
    context = {
        'form': form,
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

def confirm(request, pk):
    visitor = Visitor.objects.get(pk=pk)
    context = {
        'visitor': visitor,

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

def read_qr(request):


    context = {

    }
    return render(request, 'visitors_data/read_qr.html', context)