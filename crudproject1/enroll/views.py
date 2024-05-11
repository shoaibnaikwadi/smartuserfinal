from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import user






# his will add data and show data
def add_show(request):
    if request.method == 'POST':
        #below 3 line insert data into database this is short method
        #fm = StudentRegistration(request.POST)
        #if fm.is_valid():
        #    fm.save()



        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']

            reg = user(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration() 

    else:
        fm = StudentRegistration()
    
    
    stud = user.objects.all()      


    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud}) 
#this function will update and delete
def update_data(request,id):
    if request.method =='POST':
        pi = user.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        fm = StudentRegistration()

    else:
        pi = user.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)

    return render(request, 'enroll/updatestudent.html', {'form':fm, 'id':id})





#this fuction will delete data and you also have to define dynamic url for that and in html file instead a tag you have to create form

def delet_data(request, id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')