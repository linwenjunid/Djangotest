from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponse('success!%s'%cd)
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})#设置初始值
    return render(request, 'contact_form.html',{'form': form})

