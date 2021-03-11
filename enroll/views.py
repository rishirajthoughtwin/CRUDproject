from django.shortcuts import render ,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User


# This Function can add DATA and show the DATA
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)

        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            
            reg = User(name=nm , email=em , password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', { 'form':fm ,'stu':stud })


# This Function will Update/Edit data present in database
def update_data(request ,id):
    if request.method == "POST":
        model_data = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=model_data)
        if fm.is_valid:
            fm.save()
    else:
        model_data = User.objects.get(pk=id)
        fm = StudentRegistration(instance = model_data)
    return render(request ,'enroll/updatestudent.html' , {'form':fm})
    


# This Function can DELETE data According to its PRIMARY-KEY
def delete_data(request ,id):
    if request.method == 'POST':
        model_data = User.objects.get(pk=id)
        model_data.delete()

    return HttpResponseRedirect('/')

    






