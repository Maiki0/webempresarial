import email
from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .fomrs import ContactForm

# Create your views here.
def contact (request):
    contact_form = ContactForm()
    
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            
            # Creamos el correo 
            email = EmailMessage(
                "La Sabrosa: Nuevo mensaje de conctato", # ASUNTO
                "DE {} {} \n\n Escribio: \n\n {}".format(name ,email, content),# Mensaje
                "Lasabrosa.com", # email del origen
                ["lasabrosa.oscarbrazoban@gmail.com"], # email del destino
                reply_to=[email]
            )
            
            #Lo enviamos y lo redireccionamos 
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a ok
                return redirect(reverse('contact')+'?ok')   
            except:
                #algo no ha ido bien, redireccionamos a FAIL
                 return redirect(reverse('contact')+'?Fail')
            
                

    return render(request, 'contact/contact.html', {'form': contact_form})