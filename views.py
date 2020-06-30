from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1= Destination()
    dest1.name ='Munbai'
    dest1.desc = 'The City that Never Sleeps'
    dest1.price=760
    return render(request,'index.html',{'dest1':dest1})