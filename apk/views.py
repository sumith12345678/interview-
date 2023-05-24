from django.shortcuts import render, redirect
from .forms import NodeForm
from .models import Node





def create_node(request):
    form = NodeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('node_list')

    return render(request, 'create_node.html', {'form': form})





def node_list(request):
    nodes = Node.objects.all()
    return render(request, 'node_list.html', {'nodes': nodes})


def search_node(request):
    nodes=Node.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')
        if search:
            nodes=nodes.filter(node_id=search)
        
    return render(request, 'search_result.html', {'nodes': nodes})

  