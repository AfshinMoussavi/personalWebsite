from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages

def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, 'Your ticket submited succesfully')
        else:
            messages.add_message(request,messages.ERROR, "Your ticket didn't submited succesfully")

    form = ContactForm()
    return render(request, 'website/contact.html', {'form':form})