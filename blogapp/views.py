from django.shortcuts import render

# Create your views here.
def mainhome(request):
    return render(request, 'mainhome.html')
    
def sharemain(request):
    return render(request,'sharemain.html')

def photo(request):
    return render(request, 'photo.html')

def sports(reques):
    return render(reques, 'sports.html')

def sellhome(request):
    return render(request, 'sellhome.html')