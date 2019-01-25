from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (request):
    context = {
        'header' : 'Home',
                'subheading' : 'Project > About ',
        'nav': [
            ['/', 'Home'],
            ['/', 'Blog'],
            ['/blog/news', 'News'],
            ['/blog/recent', 'Recent'],
        ],
        'banner': 'about/img/banner_about.png',

    }
    return render(request,'index.html',context)

def profil (request):
    return HttpResponse('<h3>About Profil</h3>')
