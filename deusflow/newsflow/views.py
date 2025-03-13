from django.shortcuts import render

# Create your views here.
def newsflow_home(request):
    return render(request,'newsflow/newsflow_home.html')