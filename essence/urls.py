from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('contact/add/', views.new_contact),
    path('contact/getall/', views.get_contacts),
    path('contact/get/', views.get_contact),
    path('contact/update/', views.update_contact),
    path('contact/delete/', views.delete_contact),
    path('deal/add/', views.new_deal),
    path('deal/getall/', views.get_deals),
    path('deal/get/', views.get_deal),
    path('deal/update/', views.update_deal),
    path('deal/delete/', views.delete_deal)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)