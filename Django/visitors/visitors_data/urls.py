from django.urls import path
from. import views

app_name = 'visitors_data'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('citizen/', views.citizen, name='citizen'),
    path('foreigner/', views.foreigner, name='foreigner'),
    # path('new/', views.new, name='new'),
    path('confirm/', views.confirm, name='confirm'),
    path('qr/', views.qr, name='qr'),

]