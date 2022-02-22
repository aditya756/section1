from django.shortcuts import render

# Create your views here.
def demo(request):
    from .models import Destination
    dest1 = Destination()
    dest1.name='Mumbai'
    dest1.desc='The city never sleeps'
    dest1.price=700
    return render(request,'index.html',{'dest1':dest1})

    return render (request,'index.html',{'dest1':dest1})

def sam(request):
    return render (request,'mydemo.html')