from django.db import models



class emaildata(models.Model):
    name=models.CharField(max_length=50)
    useremail=models.EmailField()
    emailpassword=models.CharField(max_length=100)
    sheetid=models.CharField(max_length=10000)
    mailsubject=models.CharField(max_length=500)
    mailmessage=models.CharField(max_length=10000)
    attachment=models.FileField(upload_to="mailattachment/")
    
