from django.urls import path 
from django.views.generic import TemplateView 
from .views import OfferView,  OfferApplyView, ContactView


app_name = 'home'
urlpatterns = [
  path('', TemplateView.as_view(template_name="home/index.html"), name="index"),
  path('services', TemplateView.as_view(template_name="home/services.html"), name="services"),
  path('offers', OfferView.as_view(), name="offer"),
  path('offers/<str:slug>/apply', OfferApplyView.as_view(), name="apply"),
  path('about-us', TemplateView.as_view(template_name = "home/about-us.html"), name="about-us"),
  path('contact-us', ContactView.as_view(), name="contact-us"),
]