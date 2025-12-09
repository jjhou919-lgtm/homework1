from django.shortcuts import render,HttpResponse
 # A
# Create your views here.
def test(request):
    return HttpResponse("This is a test view.")

def aweb(request):
    return render(request, 'aweb.html')