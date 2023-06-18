from django.shortcuts import render


def main_home(request):
    return render(request, 'main/main_home.html')


def about_us_view(request):
    return render(request, 'main/about_us.html')


def contact_view(request):
    return render(request, 'main/contact.html')
