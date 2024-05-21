from django.http import HttpResponse

# REquest: para realizar peticiones
# HttpResponse: Para envia la respuesta usando el protocolo HTTP

def bienvenida(request):
    return HttpResponse("Bienvenido a este curso de Django")

def bienvenidaRojo(request):
    return HttpResponse("<p style='color:red;'>Bienvenido a este curso de Django</p>")
