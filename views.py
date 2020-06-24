from django.http import HttpResponse
from django.template import Template, Context
#VISTA
def destinos(request):
    doc_externo=open("C:/Users/admin/Desktop/pweb/test/proyecto/proyecto/plantillas/home.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)