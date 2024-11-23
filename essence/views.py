from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import Contact, Deal
import json

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
    return HttpResponse(out, headers={'Content-Type':'application/json'})

def get_contact(request:HttpRequest):
    rkId = int(request.GET.get('id'))
    contact=Contact.objects.get(pk=rkId)
    contact_json = json.dumps(contact.toDict())
    return HttpResponse(contact_json, headers={'Content-Type':'application/json'})

def update_contact(request:HttpRequest):
    rkId = int(request.GET.get('id'))
    contact = Contact.objects.get(pk=rkId)
    name = request.GET.get('name', contact.name)
    phone = request.GET.get('phone', contact.phone)
    adress = request.GET.get('adress', contact.adress)
    deals = request.GET.get('deals', contact.deals)

    contact.name = name
    contact.phone = phone
    contact.adress = adress
    contact.deals = deals
    contact.save()

    return JsonResponse(contact.toDict())

def delete_contact(request:HttpRequest):
    rkId = int(request.GET.get('id'))
    person = Contact.objects.get(id=rkId)
    person.delete()
    return HttpResponse(f"Контакт {rkId} — удален",  headers={'Content-Type':'application/json'})

# Сделки

def new_deal(request):
    pkId = int(request.GET.get('contact'))
    name = request.GET.get('name')
    description = request.GET.get('description')
    contact = Contact.objects.get(pk=pkId)
    new_deal = Deal(name=name, description=description, contact=contact)
    new_deal.save()
    return JsonResponse(new_deal.toDict())

def get_deals(request):
    deals=Deal.objects.all()
    out=[]
    for i in deals:
        out.append(i.toDict())
    return HttpResponse(out, headers={'Content-Type':'application/json'})

def get_deal(request:HttpRequest):
    rkId = int(request.GET.get('id'))
    deal=Deal.objects.get(pk=rkId)
    deal_json = json.dumps(deal.toDict())
    return HttpResponse(deal_json, headers={'Content-Type':'application/json'})

def update_deal(request:HttpRequest):
    rkId = int(request.GET.get('id'))
    pkId = int(request.GET.get('contact'))

    deal=Deal.objects.get(pk=rkId)
    contact=Contact.objects.get(pk=pkId)
    name=request.GET.get('name', deal.name)
    description=request.GET.get('description', deal.description)

    deal.name = name
    deal.description = description
    deal.contact = contact

    deal.save()

    return JsonResponse(deal.toDict())

def delete_deal(request:HttpRequest):
    rkId = int(request.GET.get('id'))
    deal = Deal.objects.get(id=rkId)
    deal.delete()
    return HttpResponse(f"Контакт {rkId} — удален",  headers={'Content-Type':'application/json'})