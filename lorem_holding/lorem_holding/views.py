from django.shortcuts import render, HttpResponse

#index, about, contact

def show_index(request):
    return render(
        request,
        'index.html',
        {"title": "Index", "hizmetler": "asfklajfa"}
    )

#extend edecegimiz seylerin icerisinde blocklari kullannabiliyoruz
#include icerisinde block calismiyor
#extend ettigimiz dosya icerisinde include kullanabiliyoruz.

def show_about(request):
    return render(
        request,
        'about.html',
        {"title": "About"}
    )
def show_contact(request):
    return render(
        request,
        'contact.html',
        {"title": "Contact"}
    )