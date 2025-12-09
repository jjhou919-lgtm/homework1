from django.shortcuts import render,HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("This is a test view.")

def bweb(request):
    return HttpResponse("This is the bweb view!!!!!!!!!!")