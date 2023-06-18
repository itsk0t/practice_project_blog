from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from comments.forms import CommentsForm
from comments.models import Comments
from news.models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, ListView


# def news_home(request):
#      news = Articles.objects.order_by('-date')
#      paginator = Paginator(news, 2)
#
#      page_number = request.GET.get('page')
#      page_obj = paginator.get_page(page_number)
#      return render(request, 'news/news_home.html', {'news': news, 'page_obj': page_obj})


class NewsHomeView(ListView):
     paginate_by = 2
     model = Articles
     template_name = 'news/news_home.html'
     context_object_name = 'news'


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail_news.html'
    context_object_name = 'article'


class CommentsView(ListView):
    model = Comments
    template_name = 'comments/comments.html'
    context_object_name = 'comm'


def comments_create(request):
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()

    form = CommentsForm()
    data = {
        'form_comm': form
    }

    return render(request, data)


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news:news_home')
        else:
            error = 'Форма была заполненна неверно!'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)


