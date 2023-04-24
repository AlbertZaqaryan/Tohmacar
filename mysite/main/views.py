from django.shortcuts import render, redirect
from .forms import Child1Form, ParentForm, Child2Form, Child3Form
from .models import Parent, Child1, Child2, Child3
# Create your views here.


def index(request):
    return render(request, 'main/index.html', context={

    })


def parent(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            Parent.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = ParentForm()
    return render(request, 'main/parent.html', context={
        'form':form
    })


def child1(request):
    if request.method == 'POST':
        form = Child1Form(request.POST)
        if form.is_valid():
            Child1.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = Child1Form()
    return render(request, 'main/child1.html', context={
        'form':form
    })

def child2(request):
    if request.method == 'POST':
        form = Child2Form(request.POST)
        if form.is_valid():
            Child2.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = Child2Form()
    return render(request, 'main/child2.html', context={
        'form':form
    })


def child3(request):
    if request.method == 'POST':
        form = Child3Form(request.POST)
        if form.is_valid():
            Child3.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = Child3Form()
    return render(request, 'main/child3.html', context={
        'form':form
    })


def tree(request):
    parent_list = Parent.objects.all()
    child_list1 = Child1.objects.all()
    child_list2 = Child2.objects.all()
    child_list3 = Child3.objects.all()
    return render(request, 'main/tree.html', context={
        'parent_list':parent_list,
        'child_list1':child_list1,
        'child_list2':child_list2,
        'child_list3':child_list3,
    })