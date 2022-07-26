
from django.shortcuts import render, redirect
from users.models import Profile, Teacher
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.http import HttpResponseRedirect

def register(request):
    if request.POST:
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        Email = request.POST.get('email')
        Password = request.POST.get('pword')
        user = User.objects.create_user(username=Email,
                                        email=Email,
                                        password=Password)

        user.first_name = first_name
        user.last_name = last_name
        user.save()
        pro = Profile.objects.create(user=user)
        pro.user = user
        pro.Gender = request.POST.get('gender')
        pro.DOB = request.POST.get('dob')
        pro.Address = request.POST.get('address')
        pro.Phone = request.POST.get('phone')
        pro.Usertype = request.POST.get('utype')
        pro.save()
        return HttpResponseRedirect('login')

    return render(request, 'core/register.html')

def addstudent(request):
    data = Profile.objects.filter(Usertype = 'teacher')
    context={'title':'assignteacher', 'data':data}
    if request.POST:
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        Email = request.POST.get('email')
        Password = request.POST.get('pword')
        user = User.objects.create_user(username=Email,
                                        email=Email,
                                        password=Password)

        user.first_name = first_name
        user.last_name = last_name
        user.save()
        pro = Profile(user=user)
        # obj = Teacher()
        # teacher = request.POST.get('teacher')
        pro.user = user
        pro.Gender = request.POST.get('gender')
        pro.DOB = request.POST.get('dob')
        pro.Address = request.POST.get('address')
        pro.Phone = request.POST.get('phone')
        pro.Usertype = 'student'
        pro.save()
        # teacher_obj = User.objects.get(email = teacher)
        # if teacher_obj.email == teacher:
        #     obj.teacher = teacher_obj
        #     obj.student = user
        #     obj.save()
        return HttpResponseRedirect('dashboard')
    return render(request, 'core/addstudent.html',context)


def addteacher(request):
    if request.POST:
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        Email = request.POST.get('email')
        Password = request.POST.get('pword')
        user = User.objects.create_user(username=Email,
                                        email=Email,
                                        password=Password)

        user.first_name = first_name
        user.last_name = last_name
        user.save()
        pro = Profile(user=user)
        pro.user = user
        pro.Gender = request.POST.get('gender')
        pro.DOB = request.POST.get('dob')
        pro.Address = request.POST.get('address')
        pro.Phone = request.POST.get('phone')
        pro.Usertype = 'teacher'
        pro.save()
        return HttpResponseRedirect('dashboard')
    return render(request, 'core/addteacher.html')


def viewstudent(request):
        data = Profile.objects.filter(Usertype = 'student')
        if data is not None:
            context={'title':'viewstudent', 'data':data}
            return render(request,"core/viewstudent.html",context)


def assignteacher(request):
        teacher = Profile.objects.filter(Usertype = 'teacher')
        student = Profile.objects.filter(Usertype = 'student')
        context={'title':'assignteacher', 'student':student, 'teacher':teacher}
        obj = Teacher()
        if request.method == 'POST':
            
            tcr = request.POST.get("teacher")
            std = request.POST.get("student")
            tcr_obj = User.objects.get(email = tcr)
            std_obj = User.objects.get(email = std)
            print(tcr_obj, std_obj)
            obj.teacher = tcr_obj
            obj.student = std_obj
            obj.save()
            return HttpResponseRedirect('core/dashboard')
        return render(request, 'core/assignteacher.html',context)



def xlogin(request):
    msg=None
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pword')
        user = authenticate(username=username, password=password)
        print(username)
        print(password)
        if user is not None:
            print('inside if ')
            login(request, user)
            return redirect("dashboard")
        else :
            msg={'error': "something wrong"}
    context={'msg':msg}
    return render(request, "core/login.html", context)

def dashboard(request):
    template='core/dashboard.html'
    profile = Profile.objects.get(user=request.user)
    return render(request,template , {'profile': profile, 'title': 'dashboard'})


def xlogout(request):
    logout(request)
    return redirect("login")


# def assignteacher(request): 
#     obj = Teacher()
#     if request.method == 'POST':
#         student = request.POST.get("student")
#         teacher = request.POST.get("teacher")
#         obj.student = student
#         obj.teacher = teacher
#         obj.save()
#         return HttpResponseRedirect('core/dashboard')
#     return render(request, 'core/assignteacher.html')

