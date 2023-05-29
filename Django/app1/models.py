from email.headerregistry import Address
from tkinter import CASCADE
from tokenize import Number
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
import uuid
import datetime


class Message2WhatApp(models.Model):
    to_number = models.CharField(max_length=50)
    message = models.CharField(max_length=1024)
       
    def __str__(self):
        return self.to_number



############# chatbot table ##################

# class feedbackupdated(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     senderid = models.CharField(max_length=1500,blank=True)
#     DiagnosticAccuracy = models.CharField(max_length=150,blank=True)
#     UserExperience = models.CharField(max_length=150,blank=True)
#     Likelihoodtorecommend = models.CharField(max_length=150,blank=True)
#     dateandtime = models.DateTimeField(default=datetime.datetime.now(),blank=True)


#     def __str__(self):
#         return str(self.senderid)








########### Disease Explained tabel #######
class Disease_explaination(models.Model):
    diseasename = models.CharField(max_length=200,blank=True)
    explainations = models.CharField(max_length=1500,blank=True)
    def __str__(self):
        return str(self.diseasename)


############################ new database #############

# class ID_Dec(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     Unique_ID = models.CharField(max_length=150,blank=True)
#     sender_id = models.CharField(max_length=1500,blank=True)
#     DOB = models.CharField(max_length=150,blank=True)
#     Age = models.CharField(max_length=150,blank=True)
#     Sex =  models.CharField(max_length=150,blank=True)
#     Height =  models.CharField(max_length=5,blank=True)
#     Weight =  models.CharField(max_length=150,blank=True)
#     BMI =  models.CharField(max_length=150,blank=True)
#     Smoker= models.CharField(max_length=150,blank=True)
#     alcohal= models.CharField(max_length=150,blank=True)
#     phonenumber= models.CharField(max_length=50,blank=True)
#     Email = models.CharField(max_length=1500,blank=True)
#     Covid= models.CharField(max_length=150,blank=True)
#     Suffering_Duration = models.CharField(max_length=1500,blank=True)
#     dateandtime = models.DateTimeField(blank=True)


#     def __str__(self):
#         return str(self.sender_id)

class modules_details(models.Model):
    # user = models.ForeignKey(ID_Dec,on_delete=models.CASCADE)
    uniqueis =  models.CharField(max_length=1500,blank=True)
    user =  models.CharField(max_length=1500,blank=True,null=True)
    id = models.BigAutoField(primary_key=True)
    Qn = models.CharField(max_length=150,blank=True,null=True)
    Ans = models.CharField(max_length=150,blank=True,null=True)
    module_name = models.CharField(max_length=150,blank=True,null=True)
    dateandtime = models.DateTimeField(blank=True)
    

    def __str__(self):
        return str(self.user)

# class Medibot_modules_details(models.Model):
#     # user = models.ForeignKey(ID_Dec,on_delete=models.CASCADE)
#     uniqueis =  models.CharField(max_length=1500,blank=True)
#     user =  models.CharField(max_length=1500,blank=True,null=True)
#     id = models.BigAutoField(primary_key=True)
#     Qn = models.CharField(max_length=150,blank=True,null=True)
#     Ans = models.CharField(max_length=150,blank=True,null=True)
#     module_name = models.CharField(max_length=150,blank=True,null=True)
#     dateandtime = models.DateTimeField(blank=True)
    

#     def __str__(self):
#         return str(self.user)

class appointmentdataNew(models.Model):
    # user = models.ForeignKey(ID_Dec,on_delete=models.CASCADE)
    user =  models.CharField(max_length=1500,blank=True,null=True)
    fromwhichapplication =  models.CharField(max_length=1500,blank=True,null=True)
    fromwhichsite =  models.CharField(max_length=1500,blank=True,null=True)
    appointmentdetails = models.TextField(max_length=1500,blank=True,null=True)
    docname =  models.CharField(max_length=1500,blank=True,null=True)
    appointmenttime =  models.CharField(max_length=1500,blank=True,null=True)
    appointmentdate = models.DateField(blank=True)
    dateandtime = models.DateTimeField(blank=True)

    def __str__(self):
        return str(self.user)

class doctorbelongto(models.Model):
    # user = models.ForeignKey(ID_Dec,on_delete=models.CASCADE)
    docname =  models.CharField(max_length=1500,blank=True,null=True)
    belongto = models.CharField(max_length=1500,blank=True,null=True)

    def __str__(self):
        return str(self.docname)

class feedbackdata(models.Model):
    # user = models.ForeignKey(ID_Dec,on_delete=models.CASCADE)
    docname =  models.CharField(max_length=1500,blank=True,null=True)
    appointmentdata = models.CharField(max_length=1500,blank=True,null=True)
    fromwhichsite =  models.CharField(max_length=1500,blank=True,null=True)
    dateandtime = models.DateTimeField(blank=True)
    admin_staff = models.CharField(max_length=150,blank=True)
    nursing_staff = models.CharField(max_length=150,blank=True)
    medical_staff = models.CharField(max_length=150,blank=True)
    comments = models.CharField(max_length=150,blank=True)


    def __str__(self):
        return str(self.docname)


class Nutrient_Information(models.Model):
    PRODUCT = models.CharField(max_length=250)
    CATEGORY = models.CharField(max_length=250)
    CALORIE = models.FloatField()
    CARB = models.FloatField()
    PRO = models.FloatField()
    FAT = models.FloatField()
    Ex_Swim = models.FloatField()
    Ex_Jog = models.FloatField()
    Ex_Cycle  = models.FloatField()
    Ex_Walk = models.FloatField()
    def __str__(self):
        return str(self.PRODUCT)

################## disease details 
class Diagnosis_Dec(models.Model):
    # user = models.ForeignKey(ID_Dec,on_delete=models.CASCADE)
    user = models.CharField(max_length=1500,blank=True,null=True)
    # sender_id = models.CharField(max_length=150,blank=True,null=True)
    id = models.BigAutoField(primary_key=True)
    disease = models.CharField(max_length=1500,blank=True,null=True)
    module_name = models.CharField(max_length=150,blank=True,null=True)
    dateandtime = models.DateTimeField(blank=True)
    

    def __str__(self):
        return str(self.user)

# class Medibot_Diagnosis_Dec(models.Model):
#     # user = models.ForeignKey(ID_Dec,on_delete=models.CASCADE)
#     user = models.CharField(max_length=1500,blank=True,null=True)
#     # sender_id = models.CharField(max_length=150,blank=True,null=True)
#     id = models.BigAutoField(primary_key=True)
#     disease = models.CharField(max_length=1500,blank=True,null=True)
#     module_name = models.CharField(max_length=150,blank=True,null=True)
#     dateandtime = models.DateTimeField(blank=True)
    

#     def __str__(self):
#         return str(self.user)


    

# class Diet_Image(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     dateandtime = models.DateTimeField(blank=True)
#     Uploaded_image = models.ImageField(upload_to='images/')

#     def __str__(self):
#         return str(self.id)

# class Skin_Image(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     dateandtime = models.DateTimeField(blank=True)
#     Uploaded_image = models.ImageField(upload_to='images/')
    
#     def __str__(self):
#         return str(self.id)

# class SurgeryDta(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.CharField(max_length=1500,blank=True,null=True)

#     dateandtime = models.DateTimeField(blank=True)
#     Uploaded_image = models.ImageField(upload_to='images/')
    
#     def __str__(self):
#         return str(self.id)


# class AppointmentData(models.Model):
#     # user = models.ForeignKey(ID_Dec,on_delete=models.CASCADE)
#     email = models.CharField(max_length=1500,blank=True,null=True)
#     from_number = models.CharField(max_length=100,blank=True,null=True)
#     dob = models.CharField(max_length=100,blank=True,null=True)
#     appointment = models.CharField(max_length=1500,blank=True,null=True)
#     dateandtime = models.DateTimeField(blank=True)
    

#     def __str__(self):
#         return str(self.from_number)

    


class pdffile(models.Model):
    uniqueis =  models.CharField(max_length=1500,blank=True)
    user =  models.CharField(max_length=1500,blank=True,null=True)
    modulename =  models.CharField(max_length=1500,blank=True)
    filedata = models.FileField(upload_to='images/')
    dateandtime = models.DateTimeField(blank=True)

    def __str__(self):
        return self.uniqueis

class whatsappdata(models.Model):
    # user = models.ForeignKey(ID_Dec,on_delete=models.CASCADE)
    uniqueis =  models.CharField(max_length=1500,blank=True)
    
    email = models.CharField(max_length=1500,blank=True,null=True)
    diagnosis_detail = models.CharField(max_length=1500,blank=True,null=True)
    # sender_id = models.CharField(max_length=150,blank=True,null=True)
    
    from_number = models.CharField(max_length=100,blank=True,null=True)
    discussion_point = models.CharField(max_length=100,blank=True,null=True)
    bloodresult = models.CharField(max_length=1500,blank=True,null=True)
    otherresult = models.CharField(max_length=150,blank=True,null=True)
    healthinsurance = models.CharField(max_length=150,blank=True,null=True)
    dateandtime = models.DateTimeField(blank=True)
    

    def __str__(self):
        return str(self.email)


# class personaldetail(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)    
#     email = models.CharField(max_length=1500,blank=True,null=True)
#     name = models.CharField(max_length=1500,blank=True,null=True)
#     weight = models.CharField(max_length=1500,blank=True,null=True)
#     height = models.CharField(max_length=1500,blank=True,null=True)
#     gender = models.CharField(max_length=1500,blank=True,null=True)
#     verified = models.BooleanField(default=False)
#     number =  models.CharField(max_length=1500,blank=True,null=True)

    
#     def __str__(self):
#         return str(self.user)

# class whatsapp_medical_detail(models.Model):
    
#     user = models.ForeignKey(User,on_delete=models.CASCADE)    
    
#     chest_smoke =  models.CharField(max_length=1500,blank=True,null=True)
#     chest_alcohol =  models.CharField(max_length=1500,blank=True,null=True)
#     chest_recent_covid =  models.CharField(max_length=1500,blank=True,null=True)
#     chest_diagnose_diabetes =  models.CharField(max_length=1500,blank=True,null=True)
#     chest_diagnose_Hypertension =  models.CharField(max_length=1500,blank=True,null=True)
#     chest_diagnose_Asthma =  models.CharField(max_length=1500,blank=True,null=True)
#     chest_diagnose_High_Cholesterol =  models.CharField(max_length=1500,blank=True,null=True)
    
#     def __str__(self):
#         return str(self.user)

# class BMIData(models.Model):
    
#     user = models.ForeignKey(User,on_delete=models.CASCADE)    
    
#     Weight =  models.IntegerField(blank=True,null=True,default=0)
#     Height =  models.IntegerField(blank=True,null=True,default=0)
#     BMI =  models.CharField(max_length=1500,blank=True,null=True,default=0)
    
    
#     def __str__(self):
#         return str(self.user)


    