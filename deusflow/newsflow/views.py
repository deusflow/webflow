from django.shortcuts import render
from .models import Articles

# Create your views here.
def newsflow_home(request):
    news = Articles.objects.all()
    return render(request,'newsflow/newsflow_home.html',{'newsflow':news})

def create(request):
    return render(request, 'newsflow/create.html')