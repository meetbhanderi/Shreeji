from django.shortcuts import render
from .functions import get_ip

# Create your views here.
def ContactUs(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        ip,lat,lng = get_ip(request)

        context = {'lat':lat, 'lng':lng}
        return render(request, "Contact/contact.html",context)
    else:
        ip, lat, lng = get_ip(request)
        context = {'lat': lat, 'lng': lng}
        return render(request, "Contact/contact.html",context)
