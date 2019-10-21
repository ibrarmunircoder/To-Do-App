from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import List
from .forms import ListForm
# Create your views here.
def home(request):

	if request.method == 'POST':
		form = ListForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ('Item has been Added To List!'))
			all_items = List.objects.all()
			return render(request, 'home.html', {'all_items': all_items})
	else:

		all_items = List.objects.all()
		return render(request, 'home.html', {'all_items': all_items})


def about(request):
	return render(request, 'about.html', {'name': 'Ibrar Butt'})


def delete(request, id):
	item = get_object_or_404(List, pk=id)
	item.delete()
	messages.success(request, ('Item has been deleted From List!'))
	return redirect('todo-app:home')

def cross_off(request, id):
	item = get_object_or_404(List, pk=id)
	item.completed = True
	item.save()
	return redirect('todo-app:home')


def uncross(request, id):
	item = get_object_or_404(List, pk=id)
	item.completed = False
	item.save()
	return redirect('todo-app:home')



def edit(request, id):

	if request.method == 'POST':
		item = get_object_or_404(List, pk=id)
		form = ListForm(request.POST or None, instance=item)
		if form.is_valid():
			form.save()
			messages.success(request, ('Item has been Edited To List!'))
			
			return redirect('todo-app:home')
	else:

		item = get_object_or_404(List, pk=id)
		return render(request, 'edit.html', {'item': item})