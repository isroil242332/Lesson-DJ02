from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        # Здесь можно добавить обработку формы
        pass
    return render(request, 'contact.html')

# Create your views here.
