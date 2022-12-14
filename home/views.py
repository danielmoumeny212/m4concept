from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.http import JsonResponse
from .forms import ContactForm, ApplyingForm
from .models import Offers
from .utils import is_valid_extension
# Create your views here.



class OfferView(View):

    def get(self, request):
        offers = Offers.objects.all()
        return render(request, 'home/offers.html', context={'offers': offers})


class OfferApplyView(View):
    def get(self, request, slug):
        job_to_applying = get_object_or_404(Offers, slug=slug)
        return render(request, 'home/apply_job.html', context={'job': job_to_applying, 'form': ApplyingForm})

    def post(self, request, slug):
        allowed_extension = ('pdf')
        form = ApplyingForm(request.POST, request.FILES)
        if form.is_valid():
            offer = get_object_or_404(Offers, slug=slug)
            file = request.FILES.get('cv')
            is_valid_ext, extension = is_valid_extension(
                file.name, allowed_extension)
            if not is_valid_ext:
                status = "error"
                return JsonResponse({'message': f"L'extension de fichier {extension} n'est pas permise ", "status": status})

        status = form.send_email(file, offer.searching_for)

        if not status == "success":
            return JsonResponse({'message': "Envoie echoué, Veuillez Ressayer", "status": status})
        return JsonResponse({"message": "Mail Envoyé", "status": status})


class ContactView(View):
    def get(self, request):
        return render(request, 'home/contact-us.html', context={'form': ContactForm})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            status = form.send_email()
        if not status == "success":
            return JsonResponse({'message': "Envoie echoué, Veuillez Ressayer", "status": status})
        return JsonResponse({"message": "Mail Envoyé", "status": status})


