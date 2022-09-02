from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import GroceryItem

def index(request):
    incomplete_items = GroceryItem.objects.filter(complete=False).order_by('created_date')
    completed_items = GroceryItem.objects.filter(complete=True).order_by('-completed_date')
    context = {
        'incomplete_items': incomplete_items,
        'completed_items': completed_items
    }
    return render(request, 'grocery_list/index.html', context)

def add(request):
    description = request.POST['description']
    # new_item = GroceryItem(description=description, created_date=timezone.now(), complete=False)
    # new_item.save()
    GroceryItem.objects.create(description=description, created_date=timezone.now(), complete=False)
    return HttpResponseRedirect(reverse('grocery:index'))

def complete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    if item.complete:
        item.complete = False
        item.completed_date = None
        item.save()
    else:
        item.complete = True
        item.completed_date = timezone.now()
        item.save()
    return HttpResponseRedirect(reverse('grocery:index'))

def delete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocery:index'))