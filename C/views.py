from django.shortcuts import render

# Create your views here.
def five(request):
    return render(request,'five.html')



def six(request):
    return render(request,'six.html')
