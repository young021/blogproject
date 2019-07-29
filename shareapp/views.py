from django.shortcuts import render

# Create your views here.
def sharemain(request):
    return render(request,'sharemain.html')

def photo(request):
    return render(request, 'photo.html')

def sports(reques):
    return render(reques, 'sports.html')
