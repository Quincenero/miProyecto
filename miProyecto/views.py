from django.http import HttpResponse

# REquest: para realizar peticiones
# HttpResponse: Para envia la respuesta usando el protocolo HTTP

def bienvenida(request):
    return HttpResponse("Bienvenido a este curso de Django")

def bienvenidaRojo(request):
    return HttpResponse("<p style='color:red;'>Bienvenido a este curso de Django</p>")

def categoriaEdad(request,edad):
    if edad >= 18:
        if edad >= 60:
            categoria = "Tercera edad"
        else:
            categoria = "Adultez"
    else:
        if edad < 10:
            categoria = "Infancia"
        else:
            categoria = "Adolescencia"
    resultado = "<h1>Categoria de la edad: %s</h1>" %categoria
    return HttpResponse(resultado)
        