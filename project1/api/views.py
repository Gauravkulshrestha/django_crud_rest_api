from rest_framework.response import Response
from django.shortcuts import redirect, render
from api import serializers
from api.serializers import ItemSerializer
from .models import Item
from api.forms import ItemForm
from rest_framework.decorators import api_view

@api_view(['GET'])
def getRoutes(request):

    get_urls = {

        'Item List':'item-list/',
        'Create List':'create-item/',
        'Update List':'update-item/<int:id>/',                
        'Delete List':'delete-item/<int:id>/',                
    }
    return Response(get_urls)

@api_view(['GET'])
def all_Items(request):
    items = Item.objects.all()
    serializers = ItemSerializer(items,many=True)
    return Response(serializers.data)

@api_view(['POST'])
def create_Items(request):
    serializers = ItemSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)
    
@api_view(['POST'])
def update_Items(request,id):
    items = Item.objects.get(id=id)
    serializers = ItemSerializer(instance=items, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def delete_Items(request, id):
    items = Item.objects.get(id=id)
    items.delete()
    return Response("Item deleted successfully..!!")

def createItem(request):
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ItemForm()
    items = Item.objects.all()
    context = {"items":items, "form":form}
    return render(request, 'index.html', context)

def updateItem(request, id):
    items = Item.objects.get(id=id)
    form = ItemForm(instance=items)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=items)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm(instance=items)
    context = {"form":form, "items":items}
    return render(request, 'update.html', context)

def deleteItem(request, id):
    items = Item.objects.get(id=id)
    if request.method == "POST":
        items.delete()
        return redirect("home")
    context = {"items":items}
    return render(request, 'delete.html', context)