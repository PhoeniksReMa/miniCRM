from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name='home'),
    path('contact/', views.contacts_page, name='contact'),
    path('contact/add/', views.new_contact),
    path('contact/getall/', views.get_contacts),
    path('contact/get/', views.get_contact),
    path('deals/', views.deals_page, name='deals')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)