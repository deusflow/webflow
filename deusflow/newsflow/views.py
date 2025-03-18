from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
def newsflow_home(request):
    news = Articles.objects.all()
    return render(request,'newsflow/newsflow_home.html',{'newsflow':news})

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'newsflow/create.html'
    form_class = ArticleForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/newsflow/'
    template_name = 'newsflow/news-delete.html'


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'newsflow/details_view.html'
    context_object_name = 'article'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newsflow_home')
        else:
                error = 'Form is not valid'


    form = ArticleForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'newsflow/create.html', data)