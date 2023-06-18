from django.shortcuts import render
from django.views.generic import ListView

from comments.forms import CommentsForm
from comments.models import Comments


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