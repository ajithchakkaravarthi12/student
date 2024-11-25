from urllib import request
from django.shortcuts import render, redirect
from myapp.models import student


def index_page(request):
    if request.method == "POST":  # Fix request method check
        a = request.POST['name']
        b = request.POST['email']
        c = request.POST['mobile']
        d = request.POST['city']
        data = student(name=a, email=b, mobile=c, city=d)  # Fix typo in 'email'
        data.save()
        return redirect("/display")
    return render(request, 'index.html')


def display_page(request):
    data = student.objects.all()  # Retrieve all student objects
    return render(request, 'display.html', {"show_data": data})  # Fix context dictionary


def delete_data(request, id):
    data = student.objects.get(id=id)
    data.delete()
    return redirect("/display")


def update_data(request, id):  # Fix function signature to include `id`
    data = student.objects.get(id=id)
    if request.method == "POST":  # Fix request method check
        a = request.POST['name']
        b = request.POST['email']
        c = request.POST['mobile']
        d = request.POST['city']

        # Update the fields
        data.name = a
        data.email = b
        data.mobile = c
        data.city = d
        data.save()
        return redirect("/display")

    return render(request, 'update.html', {'data': data})  # Pass 'data' as context
from django.shortcuts import render





