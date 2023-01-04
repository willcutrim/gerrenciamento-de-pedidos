from django.shortcuts import redirect, render, HttpResponse
from .forms import FormPedido
from .models import Pedidos


def index(request):
    pedido = Pedidos.objects.filter(status_de_pagamento='pendente').order_by('numero_da_mesa')
    
    return render(request, 'html/pedidos.html', {'pedidos': pedido})

def pedido_detalhe(request, id):
    pedido_detalhe = Pedidos.objects.get(id=id)
    pedidos = ", ".join([str(pe) for pe in pedido_detalhe.pedidos.all()])
    if request.method == "POST":
        form = FormPedido(request.POST, instance=pedido_detalhe)
        if form.is_valid():
            print(form.data)
            form.save()
            return redirect('/pedidos')
    else:
        form = FormPedido()
    return render(request, 'html/pedido-detalhe.html', {'pedidos': pedidos, 'pedido_detalhe': pedido_detalhe, 'form': form})
