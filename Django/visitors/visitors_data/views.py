from django.shortcuts import render, redirect
from .models import Visitor
import qrcode
from .forms import VisitorForm
import cv2

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
            visitor = form.save()
            return redirect('visitors_data:confirm', visitor.pk)
    else:
        form = VisitorForm()
    context = {
        'form': form,
    }
    return render(request, 'visitors_data/citizen.html', context)

## https://docs.djangoproject.com/en/3.0/ref/contrib/messages/    => error message custom

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

def qr(request, pk):
    visitor = Visitor.objects.get(pk=pk)
    qr = qrcode.QRCode(version=2, error_correction=qrcode.constants.ERROR_CORRECT_H)
    info = visitor.name + '/' + visitor.number + '/' + visitor.sex
    qr.add_data(info)
    qr.make
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(str(visitor.pk)+'_qrcode.png')


    return render(request, 'visitors_data/qr.html')

# def read_qr(request, pk):
#     img = cv2.imread('hong_qrcode.png')
#     detector = cv2.QRCodeDetector()
#     data, bbox, straight_qrcode = detector.detectAndDecode(img)
    
#     if bbox is not None:
#     print(f"QRCode data:\n{data}")
#     # display the image with lines
#     # length of bounding box
#     n_lines = len(bbox)
#     for i in range(n_lines):
#         # draw all lines
#         point1 = tuple(bbox[i][0])
#         point2 = tuple(bbox[(i+1) % n_lines][0])
#         cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)



#     context = {

#     }
#     return render(request, 'visitors_data/read_qr.html', context)