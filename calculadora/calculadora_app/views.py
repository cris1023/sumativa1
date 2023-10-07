from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    if request.POST:
        operador1 = int(request.POST['operador1'])
        operador2 = int(request.POST['operador2'])
        operacion = request.POST['operacion']
        context ={
            'operador1':operador1,
            'operador2':operador2,
            'operacion':operacion,
            'resultado':0
        }
        if operacion =='suma':
            context['resultado']=operador1+operador2,
        elif operacion =='resta':
            context['resultado']=operador1-operador2,
        elif operacion =='multiplicacion':
            context['resultado']=operador1*operador2,
        elif operacion =='division':
            context['resultado']=operador1/operador2
    return render(request,'index.html', context)