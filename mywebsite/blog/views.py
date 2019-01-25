from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (request):
    context = {
        'header' : 'Home',
        'subheading' : 'Project > Blog ',
        'banner': 'blog/img/banner_blog.png',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/blog/news', 'News'],
            ['/blog/recent', 'Recent'],
        ],


    }
    return render(request,'index.html',context)

def recent (request):
    context = {
        'judul': 'Recent',
        'kontributor': 'Kurniawan',
        'nav': [
            ['/', 'Home'],
            ['/', 'Blog'],
            ['/blog/news', 'News'],
            ['/blog/recent', 'Recent'],
        ]
    }

    return render(request, 'index.html',context)


def news (request):
    context = {
        'judul': 'News',
        'kontributor': 'Kurniawan',
        'nav': [
            ['/', 'Home'],
            ['/', 'Blog'],
            ['/blog/news', 'News'],
            ['/blog/recent', 'Recent'],
        ]
    }
    return render(request, 'index.html',context)

