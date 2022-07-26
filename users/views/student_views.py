from django.shortcuts import render
from ..models import Teacher
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect



def viewteacher(request):
        print(request.user)
        student = User.objects.get(email = request.user)
        print(student)
        if request.user == student:
            data=Teacher.objects.filter(student = request.user)
            print(data)
            if data is not None:
                context={'title':'viewteacher', 'data':data}
                return render(request,"user/viewteacher.html",context)
        return HttpResponseRedirect('core/dashboard')

