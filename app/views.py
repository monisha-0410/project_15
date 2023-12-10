from django.shortcuts import render

# Create your views here.
def kalpu(request):
    return render(request,'kalpu.html')


def bg(request):
    return render(request,'bg.html')



def checkbox(request):
    return render(request,'checkbox.html')


def fieldset(request):
    return render(request,'fieldset.html')


def Horizodiv(request):
    return render(request,'Horizodiv.html')


def forms(request):
    return render(request,'forms.html')


def layout(request):
    return render(request,'layout.html')


def list(request):
    return render(request,'list.html')

def section(request):
    return render(request,'section.html')


def table(request):
    return render(request,'table.html')