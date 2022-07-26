from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import Teacher


def viewstudent(request):
        print(request.user)
        teacher = User.objects.get(email = request.user)
        print(teacher)
        if request.user == teacher:
            data=Teacher.objects.filter(teacher = request.user)
            print(data)
            if data is not None:
                context={'title':'viewstudent', 'data':data}
                return render(request,"user/viewstudent.html",context)
        return HttpResponseRedirect('core/dashboard')

