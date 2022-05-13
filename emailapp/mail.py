import smtplib
from email.message import EmailMessage
import pandas as pd

def sendmail(useremail,emailpassword,sheetid,mailsubject,message,atach):
    if(atach=="None"):
        link="https://docs.google.com/spreadsheets/d/{}/export?format=csv".format(sheetid)
        data=pd.read_csv(link)
        mails=data.mailid
        for i in mails:
            msg=EmailMessage()
            msg['from']=useremail
            msg['subject']=mailsubject
            msg.set_content(message)
            msg['to']=str(i)
            with smtplib.SMTP_SSL("smtp.gmail.com",465) as main:
                main.login(useremail,emailpassword)
                main.send_message(msg)
        reply="mail send sucessfully"
        return reply
    elif(atach!="None"):
        link1="https://docs.google.com/spreadsheets/d/{}/export?format=csv".format(sheetid)
        data1=pd.read_csv(link1)
        mails1=data1.mailid
        for i in mails1:
            msg=EmailMessage()
            msg['from']=useremail
            msg['subject']=mailsubject
            msg.set_content(message)
            msg['to']=str(i)
            file="D:/Dev projects/projecthub/Scripts/emailautomation/media/mailattachment/{}".format(atach)
            with open(file,"rb") as fs:
                file_data=fs.read()
                file_name=atach
                msg.add_attachment(file_data,maintype="application",subtype="octed-stream",filename=file_name)
            with smtplib.SMTP_SSL("smtp.gmail.com",465) as main:
                main.login(useremail,emailpassword)
                main.send_message(msg)
        reply="mail send sucessfully"
        return reply
    else:
        return "Enter valid Details"

    
