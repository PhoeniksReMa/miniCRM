from django.http import HttpResponse, HttpRequest, HttpResponseServerError, JsonResponse
from django.shortcuts import render
from .models import Contact
import json

def home_page(request):
    return render(request, 'essence/home_page.html')
def contacts_page(request):
    return render(request, 'essence/contacts_page.html')
def deals_page(request):
    return render(request, 'essence/deals_page.html')

def new_contact(request):
    name = request.GET.get('name')
    phone = request.GET.get('phone')
    adress = request.GET.get('adress')
    new_cont = Contact(name=name, phone=phone, adress=adress)
    new_cont.save()
    return JsonResponse(new_cont.toDict())

def get_contacts(request):
    contacts=Contact.objects.all()
    out=[]
    for i in contacts:
        out.append(i.toDict())
    return JsonResponse(out, safe=False)

def get_contact(request:HttpRequest):
    try:
        rkId = int(request.GET.get('id'))
    except ValueError:
        return JsonResponse(data, encoder=MyJSONEncoder)
    contact=Contact.objects.get(pk=rkId)
    contact_json = json.dumps(contact.toDict())
    return HttpResponse(contact_json, headers={'Content-Type':'application/json'})