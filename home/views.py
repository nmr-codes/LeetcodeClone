from django.shortcuts import render

def homePageView(request):
    return render(request, 'home/home_page.html')
