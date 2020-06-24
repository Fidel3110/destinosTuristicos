from django.http import HttpResponse
#VISTA
def saludo(request):
    return HttpResponse("Probando..")