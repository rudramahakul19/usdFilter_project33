from django.shortcuts import render

# Create your views here.

def userfilter(request):
    d={'data':'HeLLO MaHAKul havE A niCE DAy'}

    return render(request,'userfilter.html',d)