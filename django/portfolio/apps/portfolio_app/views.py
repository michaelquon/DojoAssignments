from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'portfolio_app/index.html')

def testimonials(request):
    return render(request, 'portfolio_app/testimonials.html')