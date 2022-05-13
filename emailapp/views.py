from django.shortcuts import render
from . mail import sendmail
from . models import emaildata
from django.http import HttpResponse
def home(request):
    if(request.method=="POST"):
        username=request.POST.get("name")
        useremail=request.POST.get("email")
        emailpassword=request.POST.get("password")
        sheetid=request.POST.get("id")
        mailsubject=request.POST.get("subject")
        message=request.POST.get("message")
        file=request.FILES.get("attachment")
        try:
            atach=file.name
        except:
            atach="None"
        newmail=emaildata.objects.create(name=username,useremail=useremail,emailpassword=emailpassword,sheetid=sheetid,mailsubject=mailsubject,mailmessage=message,attachment=file)
        newmail.save()
        gomail=sendmail(useremail,emailpassword,sheetid,mailsubject,message,atach)
        if(gomail=="mail send sucessfully"):
            return render(request,"emailapp/success.html")
        else:
            return render(request,"emailapp/failed.html")
    return render(request,"emailapp/home.html")
