from django.shortcuts import render
from .models import Articles
from .forms import ArticleForm

# Create your views here.
def newsflow_home(request):
    news = Articles.objects.all()
    return render(request,'newsflow/newsflow_home.html',{'newsflow':news})

def create(request):
    form = ArticleForm()

    data = {
        'form': form
    }

    return render(request, 'newsflow/create.html', data)