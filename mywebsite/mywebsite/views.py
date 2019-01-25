from django.http import HttpResponse
from django.shortcuts import render

#ini method view

# def index(request):
#     return HttpResponse("")

def index(request):
    context = {
                'header' : 'Home',
                'subheading' : 'Project > Home ',
                'banner': 'img/banner_home.png',
                'nav' : [
                    ['/','Home'],
                    ['/blog','Blog'],
                    ['/about','About'],
                    ['/contact','Contact'],
                ],


              }
    return  render(request,'index.html', context)


# def about(request):
#     return  render(request,'about.html')

# def about(request):
#     return HttpResponse("Ini Halaman About")


