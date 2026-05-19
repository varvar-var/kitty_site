from django.shortcuts import render, redirect
from . models import Cat, Volunteer
from . forms import VolunteerForms

# Create your views here.
def index(request):
    cat = Cat.objects.all()
    context = {"cats" : cat}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def help(request):
    if request.method == 'POST':
        form = VolunteerForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kitty:help')   
    else:
        form = VolunteerForms()
    context = {"form" : form, 'donation_details': {
            'bank': 'Тинькофф Банк',
            'card_number': '1234 5678 9012 3456',
            'phone': '+7 (999) 123-45-67',
            'yoomoney': '4100123456789'
        }}    
    return render(request, 'help.html', context)