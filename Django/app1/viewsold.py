from glob import glob
from multiprocessing import context
import re
from urllib import request
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth import logout as django_logout
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app1.models import RiskID, ClientID, Basic, Cough,Feedback
import torch
from django.contrib.staticfiles import finders
from rest_framework.views import APIView
from django.core import serializers
import os
import datetime
import shutil
import requests
from django.contrib.auth.decorators import login_required
from datetime import date
from django.core.mail import EmailMessage
from django.contrib import messages
from exotel import Exotel
import operator
from urllib import request
import urllib.request



from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer




model_skin= torch.hub.load('yolov5', 'yolov5s', source='local', device='cpu')
model_cxr = torch.hub.load('yolov5', 'yolov5ss', source='local', device='cpu')
model_food = torch.hub.load('yolov5', 'yolov5food', source='local', device='cpu')

context = {}

# VB=0
# BP=0
# A=0
# CHF=0
# CLD=0
# LC=0
# PE=0
# covid=0

# Viral_Fever =0
# COVID=0
# Pneumonia=0
# Cholangitis=0
# Endocarditis=0
# Cellulitis=0
# UTI=0
# Osteomyelitis=0
# Meningitis=0

# Appendicitis= 0
# Cholecystitis= 0
# Cystitis= 0
# Pyelonephritis= 0
# Renal_Calculi= 0
# Diverticulitis= 0
# Inflammatory_Bowel= 0
# Irritable_Bowel= 0
# Pancreatitis= 0
# Endometriosis= 0
# Gastritis=0

# age=0

# Cardiac_Ischemia=0
# Pleurisy=0
# Costochondritis=0
# otp = 0
# otpnumber = 0
import ast
from django.template.loader import render_to_string

from twilio.rest import Client
import random

######### Feedback form ##############

@csrf_exempt
def feedbackForm(request):
    if request.method == 'POST':
        print('POST data is', request.POST)
        try:
            print ("In try")
            print ("In try data",request.body)
            form_data_str = str(request.body)
            form_data_str = form_data_str[2:-1]
            print(form_data_str)
            form_dict = json.loads(form_data_str)
            try :
                visit_type =  form_dict["visit_type"]
            except :
                pass
            try :
                visit_date =  form_dict["visit_date"]
            except :
                pass
            try :
                visit_time =  form_dict["visit_time"]
            except :
                pass
            try :
                medical =  form_dict["medical"]
            except :
                pass
            try :
                nursing =  form_dict["nursing"]
            except :
                pass
            try :
                admin =  form_dict["nursing"]
            except :
                pass
            try :
                practice_cleanliness =  form_dict["practice_cleanliness"]
            except :
                pass
            try :
                comment =  form_dict["comment"]
            except :
                pass

            feedback= Feedback.objects.create(Visit_Type=visit_type,Visit_Date=visit_date,Visit_Time=visit_time,Medical=medical,Nursing=nursing,Admin=admin,Practice_Cleanliness= practice_cleanliness,Comment=comment)
            feedback.save()
            return JsonResponse({"status":"done"})
        except Exception as e:
            print ("Erro is ",e)
            return JsonResponse({"status":e})





@csrf_exempt
def fever_rasa(request):
    print ("in the functionS")
    if request.method == 'POST':
        print('POST data is', request.POST)
        print('post BODY', request.body)
        
        ##################################
        Appendicitis = 0
        Cholecystitis = 0
        Gastritis = 0
        Cystitis = 0
        Pyelonephritis = 0
        Renal_Calculi = 0
        Diverticulitis = 0
        Interstinal_Obstruction = 0
        Inflammatory_Bowel_Disease= 0
        Irritable_Bowel_Disease = 0
        Pancreatitis = 0
        Endometriosis = 0
        Anxiety = 0
        Depression = 0
        Cardiac_Ischemia = 0
        Pulmonary_Embolism = 0
        Pleurisy = 0
        Costochondritis = 0
        Pneumonia = 0
        Viral_Bronchitis = 0
        Asthma = 0
        Chronic_Heart_Failure = 0
        Chronic_Lung_Disease = 0
        Lunc_Cancer = 0
        COVID = 0
        Diabetes = 0
        Viral_Fever = 0
        Cholangitis = 0
        Endocarditis = 0
        Cellulitis = 0
        Urinary_Tract_Infection = 0
        Osteomyelitis = 0
        Meningitis = 0
        depression = 0
        anxiety = 0

        try:
            print ("In try")
            print ("In try data",request.body)
            form_data_str = str(request.body)
            form_data_str = form_data_str[2:-1]
            print(form_data_str)
            form_dict = json.loads(form_data_str)
            
            try :
                if form_dict["1f"] == "Few days":
                    Viral_Fever += 3.33
                    Meningitis += 5
                    Cellulitis += 5
            except :
                pass

            try :
                if form_dict["1f"] == "Few days" or  form_dict["1f"] == "Few weeks":
                    Urinary_Tract_Infection += 5
                    Pneumonia += 5
                    Cholangitis += 2.5

            except :
                pass
            
            try :
                if form_dict["1f"] == "Few Months" or  form_dict["1f"] == "Few weeks":
                    Endocarditis += 5
                    Osteomyelitis += 5
            except :
                pass

            try :
                if form_dict["3A"] == "Yes":
                    Viral_Fever += 3.33
            except :
                pass
            
            
            try :
                if form_dict["3B"] == "Yes":
                    Cholangitis += 2.5
            except :
                pass


            try :
                if form_dict["3C"] == "Yes":
                    Viral_Fever += 3.33
                    Meningitis += 5
            except :
                pass

            try :
                if form_dict["3D"] == "Yes":
                    Urinary_Tract_Infection += 5
            except :
                pass
            
            try :
                if form_dict["3E"] == "Yes":
                    Cellulitis += 5
            except :
                pass
            
            try :
                if form_dict["3F"] == "Yes":
                    Endocarditis += 5
                    Osteomyelitis += 5
                    Cholangitis += 2.5
            except :
                pass
            
            try :
                if form_dict["3H"] == "Yes":
                    Cholangitis += 2.5
            except :
                pass

            try :
                if form_dict["3I"] == "Yes":
                    Pneumonia += 5
            except :
                pass

            try :
                if form_dict["1f"] == "Few days" and form_dict["3A"] == "Yes" :
                    Viral_Fever = True
            except :
                pass
            
            

            try :
                if (form_dict["1f"] == "Few days" or  form_dict["1f"] == "Few weeks") and form_dict["3D"] == "Yes":
                    Urinary_Tract_Infection = True
            except :
                pass
            try :
                if form_dict["1f"] == "Few days" and form_dict["3C"] == "Yes":
                    Meningitis = True
            except :
                pass

            try :
                if (form_dict["1f"] == "Few Months" or  form_dict["1f"] == "Few weeks") and form_dict["3F"] == "Yes":
                    Endocarditis = True
                    Osteomyelitis = True
            except :
                pass

            try :
                if (form_dict["1f"] == "Few days" or  form_dict["1f"] == "Few weeks") and form_dict["3I"] == "Yes":
                    Pneumonia = True
            except :
                pass

            try :
                if (form_dict["1f"] == "Few days" or  form_dict["1f"] == "Few weeks") and form_dict["3H"] == "Yes":
                    Cholangitis = True
            except :
                pass
            all_data = {
                "Appendicitis":Appendicitis,
                "Cholecystitis":Cholecystitis,
                "Gastritis":Gastritis,
                "Cystitis":Cystitis,
                "Pyelonephritis":Pyelonephritis,
                "Renal_Calculi":Renal_Calculi,
                "Diverticulitis":Diverticulitis,
                "Interstinal_Obstruction":Interstinal_Obstruction,
                "Inflammatory_Bowel_Disease":Inflammatory_Bowel_Disease,
                "Irritable_Bowel_Disease":Irritable_Bowel_Disease,
                "Pancreatitis":Pancreatitis,
                "Endometriosis":Endometriosis,
                "Anxiety":Anxiety,
                "Depression":Depression,
                "Cardiac_Ischemia":Cardiac_Ischemia,
                "Pulmonary_Embolism":Pulmonary_Embolism,
                "Pleurisy":Pleurisy,
                "Costochondritis":Costochondritis,
                "Pneumonia":Pneumonia,
                "Viral_Bronchitis":Viral_Bronchitis,
                "Asthma":Asthma,
                "Chronic_Heart_Failure":Chronic_Heart_Failure,
                "Chronic_Lung_Disease":Chronic_Lung_Disease,
                "Lunc_Cancer":Lunc_Cancer,
                "COVID":COVID,
                "Diabetes":Diabetes,
                "Viral_Fever":Viral_Fever,
                "Cholangitis":Cholangitis,
                "Endocarditis":Endocarditis,
                "Cellulitis":Cellulitis,
                "Urinary_Tract_Infection":Urinary_Tract_Infection,
                "Osteomyelitis":Osteomyelitis,
                "Meningitis":Meningitis

            }

            print ("all data",all_data)


            x = sorted(((v,k) for k,v in all_data.items() if v == True ))

            if len(x) == 0:
                try :
                    if form_dict["options"] == "Sure":

                        x = sorted(((v,k) for k,v in all_data.items() if v >= 0))
                        first_name = x[-1][1]
                        first_value = x[-1][0]
                        second_name = x[-2][1]
                        second_value = x[-2][0]
                        third_name = x[-3][1]
                        third_value = x[-3][0]
                        fourth_name = x[-4][1]
                        fourth_value = x[-4][0]
                        context2 = {
                            "diseases": first_name + " or " + second_name + " or " + third_name + " or " + fourth_name,
                            }
                        return JsonResponse({"status":context2})
                except:
                    context2 = {
                        "diseases": "Not_Confirnmed",

                        }
                    return JsonResponse({"status":context2})

            if len(x) == 1:
                first_name = x[-1][1]
                first_value = x[-1][0]

                context2 = {
                    "diseases": first_name

                    }

                return JsonResponse({"status":context2})

            if len(x) == 2:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]

                context2 = {
                    "diseases": first_name + " or " + second_name ,

                    }
                return JsonResponse({"status":context2})


            if len(x) == 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                context2 = {
                    "diseases": first_name + " or " + second_name + " or " + third_name ,
                    }
                return JsonResponse({"status":context2})


                # return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

            if len(x) > 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                fourth_name = x[-4][1]
                fourth_value = x[-4][0]
                context2 = {
                    "diseases": first_name + " or " + second_name + " or " + third_name + " or " + fourth_name,
                    }
                return JsonResponse({"status":context2})


        except Exception as e:
            print("Error Receiving Form Data", e)
            return render (request,"cough_fever_result.html",{'context1':"in except"})




@csrf_exempt
def basic_details_user(request):
    global age
    if request.method == 'POST':
        print('POST data is', request.POST)
        print('post BODY', request.body)
        try:
            print ("In try")
            print ("In try data",request.body)
            form_data_str = str(request.body)
            form_data_str = form_data_str[2:-1]
            print(form_data_str)
            form_dict = json.loads(form_data_str)
            try :
                gender =  form_dict["gender"]
            except :
                pass

            try :
                weight =  form_dict["weight"]
            except :
                pass
            
            try :
                height =  form_dict["height"]
            except :
                pass
            print("height is", height)
            print("weight is", weight)
            BMI = round((int(weight) / (int(height) * int(height))),2)
            
            print ("your bmi ",BMI)
            try :
                DOB =  form_dict["DOB"]
            except :
                pass
            try:
                x = DOB.split("-")
                print ("x",x)
                def ageCalculator(years, months, days,year,month,date):
                    global age
                    import datetime
                    today = datetime.date(years,months,days)
                    dob = datetime.date(year, month, date)
                    years= ((today-dob).total_seconds()/ (365.242*24*3600))
                    yearsInt=int(years)
                    months=(years-yearsInt)*12
                    monthsInt=int(months)
                    days=(months-monthsInt)*(365.242/12)
                    daysInt=int(days)
                    print('You are {0} years, {1} months, {2} days old.'.format(yearsInt,monthsInt,daysInt))
                    age = str(yearsInt) 
                    print ("age=",age)
                b_year = int(x[2])
                b_month = int(x[1])
                b_date = int(x[0])
                now = datetime.datetime.now()
                # get year from date
                c_year = int(now.strftime("%Y"))
                # get month from date
                c_month = int(now.strftime("%m"))
                # get day from date
                c_date =int( now.strftime("%d"))
                ageCalculator(c_year,c_month,c_date,b_year,b_month,b_date)
            except Exception as e:
                print ("Error is",e)
                pass
            print ("your date of birth is",DOB)

            try :
                email =  form_dict["email"]
                print("Your email is", email)
                email_updated= email[::2]
                print("Your updated email is", email_updated)
                DOB =  form_dict["DOB"]
                updated_date =DOB.replace("-","")
                print("Your updated date is", updated_date)
                updated_date=updated_date[1::2]
                print("Your updated date is", updated_date)

                uniques_id = email_updated + updated_date
            except Exception as e:
                print ("Error",e)

            try :
                smoking =  form_dict["smoking"]
            except :
                pass

            try :
                covid =  form_dict["covid"]
            except :
                pass

            try :
                unwell =  form_dict["Suffering_time"]
                print("Your unwell status is",unwell )
            except :
                pass

            basic_information = Basic.objects.create(Unique_ID=uniques_id, DOB=DOB,Weight=weight,Height=height,Age=age,BMI=BMI,Sex=gender,Email= email,Smoker=smoking, Covid=covid, Suffering_Duration=unwell)
            basic_information.save()
            return JsonResponse({"status":uniques_id})
        except Exception as e:
            print ("Erro is ",e)
            return JsonResponse({"status":e})


@csrf_exempt
def cough_rasa(request):
    if request.method == 'POST':
        print('POST data is', request.POST)
        print('post BODY', request.body)
        Appendicitis = 0
        Cholecystitis = 0
        Gastritis = 0
        Cystitis = 0
        Pyelonephritis = 0
        Renal_Calculi = 0
        Diverticulitis = 0
        Interstinal_Obstruction = 0
        Inflammatory_Bowel_Disease= 0
        Irritable_Bowel_Disease = 0
        Pancreatitis = 0
        Endometriosis = 0
        Anxiety = 0
        Depression = 0
        Cardiac_Ischemia = 0
        Pulmonary_Embolism = 0
        Pleurisy = 0
        Costochondritis = 0
        Pneumonia = 0
        Viral_Bronchitis = 0
        Asthma = 0
        Chronic_Heart_Failure = 0
        Chronic_Lung_Disease = 0
        Lunc_Cancer = 0
        COVID = 0
        Diabetes = 0
        Viral_Fever = 0
        Cholangitis = 0
        Endocarditis = 0
        Cellulitis = 0
        Urinary_Tract_Infection = 0
        Osteomyelitis = 0
        Meningitis = 0
        depression = 0
        anxiety = 0

        try:
            print ("In try")
            print ("In try data",request.body)
            form_data_str = str(request.body)
            form_data_str = form_data_str[2:-1]
            print(form_data_str)
            form_dict = json.loads(form_data_str)

            

            try :
                if form_dict["1d"] == "Yes":
                    Pneumonia += 2
                    Viral_Bronchitis += 2.5
                    Chronic_Lung_Disease += 1.66
                    Pleurisy += 2.5
                    Lunc_Cancer += 1.66
                    Asthma += 2
            except :
                pass        
            
            try :
                if form_dict["1e"] == "Yes": 
                    Chronic_Lung_Disease += 1.66
            except :
                pass  
            
            try :
                if form_dict["1f"] == "Few days" or  form_dict["1f"] == "Few weeks":
                    Pneumonia += 2
                    Pulmonary_Embolism += 2.5
                    Pleurisy += 2.5
                    Asthma += 2
                    Costochondritis += 2.5
            except :
                pass

            try :
                if form_dict["1f"] == "Few Months" or  form_dict["1f"] == "Few weeks":
                    Lunc_Cancer += 1.66
            except :
                pass
            
            try :
                if form_dict["1f"] == "Few Months" or  form_dict["1f"] == "Many months":
                    Chronic_Heart_Failure += 2
            except :
                pass

            try :
                if form_dict["1f"] == "Few days":
                   Viral_Bronchitis += 2.5
                   COVID += 2.5
            except :
                pass

            try :
                if form_dict["1f"] == "Many months":
                   Chronic_Lung_Disease += 1.66
            except :
                pass

            try :
                if form_dict["2A"] == "Yes":
                    Pneumonia += 2
                    Viral_Bronchitis += 2.5
                    Chronic_Lung_Disease += 1.66
                    COVID += 2.5
            except :
                pass 
            
            try :
                if form_dict["2B"] == "Yes":
                    Pneumonia += 2
                    Chronic_Lung_Disease += 1.66
                    Lunc_Cancer += 1.66
            except :
                pass 
            try :
                if form_dict["2C"] == "Yes":
                    Pneumonia += 2
                    Lunc_Cancer += 1.66
                    Chronic_Lung_Disease += 1.66
                    Pulmonary_Embolism += 2.5
                    Asthma += 2
                    Chronic_Heart_Failure += 2
            except :
                pass 
            
            try :
                if form_dict["2D"] == "Yes":
                    COVID += 2.5
            except :
                pass
          

            try :
                if form_dict["2E"] == "Yes":
                    Viral_Bronchitis += 2.5
                    COVID += 2.5
                    Pleurisy += 2.5
                    Costochondritis += 2.5
            except :
                pass

            try :
                if form_dict["2F"] == "Yes":
                    Pulmonary_Embolism += 2.5
                    Lunc_Cancer += 1.66
                    Chronic_Heart_Failure += 2
            except :
                pass

            try :
                if form_dict["2G"] == "Yes":
                    Pulmonary_Embolism += 2.5
                    Pleurisy += 2.5
                    Asthma += 2
                    Costochondritis += 2.5
            except :
                pass
                
            try :
                if form_dict["2H"] == "Yes":
                    Lunc_Cancer += 1.66
            except :
                pass
            
            try :
                if form_dict["2J"] == "Yes":
                    Asthma += 2
                    Chronic_Heart_Failure += 2
            except :
                pass

            try :
                if form_dict["2K"] == "Yes":
                    Chronic_Heart_Failure += 2
            except :
                pass

            try :
                if form_dict["2L"] == "Yes":
                    Costochondritis += 2.5
            except :
                pass

            try :
                if form_dict["2A"] == "Yes" and form_dict["2B"] == "Yes" and form_dict["2C"] == "Yes":
                    Pneumonia = True
            except :
                pass

            try :
                if form_dict["1f"] == "Few days" and form_dict["2A"] == "Yes" and form_dict["2E"] == "Yes":
                    Viral_Bronchitis = True
            except :
                pass

            try:
                if form_dict["1d"] == "Yes" and form_dict["1f"] == "Many Months" and form_dict["2B"] == "Yes" and form_dict["2C"] == "Yes":
                    Chronic_Lung_Disease = True
            except :
                pass

            try:
                if form_dict["1f"] == "Few days" and form_dict["2A"] == "Yes" and form_dict["2D"] == "Yes":
                    COVID = True
            except :
                pass
            #################
            try :
                if (form_dict["1f"] == "Few days" or form_dict["1f"] == "Few weeks") and form_dict["2G"] == "Yes" and form_dict["2F"] == "Yes" :
                    Pulmonary_Embolism = True
            except :
                pass


            try :
                if (form_dict["1f"] == "Few days" or form_dict["1f"] == "Few weeks") and form_dict["1d"] == "Yes" and form_dict["2G"] == "Yes" :
                    Pleurisy = True
            except :
                pass

            try :
                if (form_dict["1f"] == "Few Months" or form_dict["1f"] == "Few weeks") and  form_dict["2h"] == "Yes" and form_dict["2F"] == "Yes" and form_dict["1d"] == "Yes" :
                    Lunc_Cancer = True
            except :
                pass

            try :
                if (form_dict["1f"] == "Few days" or form_dict["1f"] == "Few weeks") and form_dict["2J"] == "Yes" and form_dict["2C"] == "Yes" :
                    Asthma = True
            except :
                pass

            try :
                if (form_dict["1f"] == "Few Months" or  form_dict["1f"] == "Many months") and form_dict["2C"] == "Yes" and form_dict["2K"] == "Yes" :
                    Chronic_Heart_Failure = True
            except :
                pass

            try :
                if (form_dict["1f"] == "Few days" or  form_dict["1f"] == "Few weeks") and form_dict["2G"] == "Yes" and form_dict["2L"] == "Yes"  :
                    Costochondritis = True
            except :
                pass

            all_data = {
                "Appendicitis":Appendicitis,
                "Cholecystitis":Cholecystitis,
                "Gastritis":Gastritis,
                "Cystitis":Cystitis,
                "Pyelonephritis":Pyelonephritis,
                "Renal_Calculi":Renal_Calculi,
                "Diverticulitis":Diverticulitis,
                "Interstinal_Obstruction":Interstinal_Obstruction,
                "Inflammatory_Bowel_Disease":Inflammatory_Bowel_Disease,
                "Irritable_Bowel_Disease":Irritable_Bowel_Disease,
                "Pancreatitis":Pancreatitis,
                "Endometriosis":Endometriosis,
                "Anxiety":Anxiety,
                "Depression":Depression,
                "Cardiac_Ischemia":Cardiac_Ischemia,
                "Pulmonary_Embolism":Pulmonary_Embolism,
                "Pleurisy":Pleurisy,
                "Costochondritis":Costochondritis,
                "Pneumonia":Pneumonia,
                "Viral_Bronchitis":Viral_Bronchitis,
                "Asthma":Asthma,
                "Chronic_Heart_Failure":Chronic_Heart_Failure,
                "Chronic_Lung_Disease":Chronic_Lung_Disease,
                "Lunc_Cancer":Lunc_Cancer,
                "COVID":COVID,
                "Diabetes":Diabetes,
                "Viral_Fever":Viral_Fever,
                "Cholangitis":Cholangitis,
                "Endocarditis":Endocarditis,
                "Cellulitis":Cellulitis,
                "Urinary_Tract_Infection":Urinary_Tract_Infection,
                "Osteomyelitis":Osteomyelitis,
                "Meningitis":Meningitis

            }

            print ("all data",all_data)


            x = sorted(((v,k) for k,v in all_data.items() if v == True ))

            if len(x) == 0:
                try :
                    if form_dict["options"] == "Sure":
                        x = sorted(((v,k) for k,v in all_data.items() if v > 0))
                        first_name = x[-1][1]
                        first_value = x[-1][0]
                        second_name = x[-2][1]
                        second_value = x[-2][0]
                        third_name = x[-3][1]
                        third_value = x[-3][0]
                        fourth_name = x[-4][1]
                        fourth_value = x[-4][0]
                        context2 = {
                            "diseases": first_name + " or " + second_name + " or " + third_name + " or " + fourth_name,
                            }

                        # Cough_Response = Cough.objects.create(Qn2A=form_dict["2A"], Qn2B=form_dict["2B"], Qn2C=form_dict["2C"], Qn2D=form_dict["2D"], Qn2E=form_dict["2E"], Qn2F=form_dict["2F"], Qn2G=form_dict["2G"],Qn2H=form_dict["2H"], Qn2I=form_dict["2I"])
                        # Cough_Response.save()
                        return JsonResponse({"status":context2})
                except:
                    context2 = {
                        "diseases": "Not_Confirnmed",

                        }
                    # Cough_Response = Cough.objects.create(Qn2A=form_dict["2A"], Qn2B=form_dict["2B"], Qn2C=form_dict["2C"], Qn2D=form_dict["2D"], Qn2E=form_dict["2E"], Qn2F=form_dict["2F"], Qn2G=form_dict["2G"],Qn2H=form_dict["2H"], Qn2I=form_dict["2I"])
                    # Cough_Response.save()
                    return JsonResponse({"status":context2})

            if len(x) == 1:
                first_name = x[-1][1]
                first_value = x[-1][0]

                context2 = {
                    "diseases": first_name

                    }

                # Cough_Response = Cough.objects.create(Qn2A=form_dict["2A"], Qn2B=form_dict["2B"], Qn2C=form_dict["2C"], Qn2D=form_dict["2D"], Qn2E=form_dict["2E"], Qn2F=form_dict["2F"], Qn2G=form_dict["2G"],Qn2H=form_dict["2H"], Qn2I=form_dict["2I"])
                # Cough_Response.save()

                return JsonResponse({"status":context2})

            if len(x) == 2:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]

                context2 = {
                    "diseases": first_name + " or " + second_name ,

                    }

                # Cough_Response = Cough.objects.create(Qn2A=form_dict["2A"], Qn2B=form_dict["2B"], Qn2C=form_dict["2C"], Qn2D=form_dict["2D"], Qn2E=form_dict["2E"], Qn2F=form_dict["2F"], Qn2G=form_dict["2G"],Qn2H=form_dict["2H"], Qn2I=form_dict["2I"])
                # Cough_Response.save()
                return JsonResponse({"status":context2})


            if len(x) == 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                context2 = {
                    "diseases": first_name + " or " + second_name + " or " + third_name ,
                    }

                # Cough_Response = Cough.objects.create(Qn2A=form_dict["2A"], Qn2B=form_dict["2B"], Qn2C=form_dict["2C"], Qn2D=form_dict["2D"], Qn2E=form_dict["2E"], Qn2F=form_dict["2F"], Qn2G=form_dict["2G"],Qn2H=form_dict["2H"], Qn2I=form_dict["2I"])
                # Cough_Response.save()
                return JsonResponse({"status":context2})


                # return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

            if len(x) > 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                fourth_name = x[-4][1]
                fourth_value = x[-4][0]
                context2 = {
                    "diseases": first_name + " or " + second_name + " or " + third_name + " or " + fourth_name,
                    }

                # Cough_Response = Cough.objects.create(Qn2A=form_dict["2A"], Qn2B=form_dict["2B"], Qn2C=form_dict["2C"], Qn2D=form_dict["2D"], Qn2E=form_dict["2E"], Qn2F=form_dict["2F"], Qn2G=form_dict["2G"],Qn2H=form_dict["2H"], Qn2I=form_dict["2I"])
                # Cough_Response.save()
                return JsonResponse({"status":context2})

                
        except Exception as e:
            print("Error Receiving Form Data", e)
            return render (request,"cough_fever_result.html",{'context1':"in except"})



@csrf_exempt
def rasachatbot(request):
    if request.method == 'POST':
        print('POST data is', request.POST)
        print('post BODY', request.body)
        form_data_str = str(request.body)
        form_dict = json.loads(form_data_str)
        print(" form_dict is " , form_dict)
        Appendicitis = 0
        Cholecystitis = 0
        Gastritis = 0
        Cystitis = 0
        Pyelonephritis = 0
        Renal_Calculi = 0
        Diverticulitis = 0
        Interstinal_Obstruction = 0
        Inflammatory_Bowel_Disease= 0
        Irritable_Bowel_Disease = 0
        Pancreatitis = 0
        Endometriosis = 0
        Anxiety = 0
        Depression = 0
        Cardiac_Ischemia = 0
        Pulmonary_Embolism = 0
        Pleurisy = 0
        Costochondritis = 0
        Pneumonia = 0
        Viral_Bronchitis = 0
        Asthma = 0
        Chronic_Heart_Failure = 0
        Chronic_Lung_Disease = 0
        Lunc_Cancer = 0
        COVID = 0
        Diabetes = 0
        Viral_Fever = 0
        Cholangitis = 0
        Endocarditis = 0
        Cellulitis = 0
        Urinary_Tract_Infection = 0
        Osteomyelitis = 0
        Meningitis = 0
        depression = 0
        anxiety = 0


        try:
            print ("In try")
            print ("In try data",request.body)
            form_data_str = str(request.body)
            form_data_str = form_data_str[2:-1]
            print(form_data_str)
            form_dict = json.loads(form_data_str)
            def ageCalculator(years, months, days,year,month,date):
                    global age
                    global ageyear

                    import datetime
                    today = datetime.date(years,months,days)
                    dob = datetime.date(year, month, date)
                    years= ((today-dob).total_seconds()/ (365.242*24*3600))
                    yearsInt=int(years)
                    months=(years-yearsInt)*12
                    monthsInt=int(months)
                    days=(months-monthsInt)*(365.242/12)
                    daysInt=int(days)
                    print('You are {0} years, {1} months, {2} days old.'.format(yearsInt,monthsInt,daysInt))
                    age = str(yearsInt) + " years " + str(monthsInt) + " Months " + str(daysInt) + " Days"
                    ageyear = yearsInt
                    print ("ageyear",ageyear)
                    print ("age=",age)



            try :
                if form_dict["Qn1"] == "Yes":
                    Viral_Bronchitis+=1.67
                    Pleurisy +=3.33
                    Costochondritis +=3.33
                    COVID += 1.43
                    Viral_Fever += 1.67
            except :
                pass

            try :
                if form_dict["Qn2"] == "Yes":
                    Pneumonia+=1.11
                    Pulmonary_Embolism +=1.25
                    Viral_Bronchitis+= 1.67
                    COVID += 1.43
                    Viral_Fever += 1.67
            except :
                pass

            try :
                if form_dict["Qn3"] == "Yes":
                    COVID += 1.43
            except :
                pass

            try :
                if form_dict["Qn4"] == "Yes":
                    Pneumonia+=1.11
                    Viral_Bronchitis+=1.67
                    COVID += 1.43
            except :
                pass

            try :
                if form_dict["Qn5"] == "Yes":
                    Pneumonia+=1.11
                    Chronic_Lung_Disease += 1.43
                    Lunc_Cancer += 1.67
                    Viral_Fever += 1.67
            except :
                pass

            try :
                if form_dict["Qn6"] == "Yes":
                    Pneumonia+=1.11
                    Pulmonary_Embolism +=1.25
                    Chronic_Heart_Failure += 1
                    Chronic_Lung_Disease += 1.43
                    Lunc_Cancer += 1.67
            except :
                pass

            try :
                if form_dict["Qn7"] == "Yes":
                    Pulmonary_Embolism +=1.25
                    Asthma+=2
                    Chronic_Heart_Failure += 1
                    Chronic_Lung_Disease += 1.43
            except :
                pass

            try :
                if form_dict["Qn8"] == "Yes":
                    Pneumonia+=1.11
                    Cardiac_Ischemia+=1.11
                    Asthma+=2
                    Chronic_Heart_Failure += 1
                    Chronic_Lung_Disease += 1.43
                    Lunc_Cancer += 1.67
                    COVID += 1.43
            except :
                pass

            try :
                if form_dict["Qn9"] == "Yes":
                    Chronic_Heart_Failure += 1
            except :
                pass


            context2 = {
                "Appendicitis":Appendicitis,
                "Cholecystitis":Cholecystitis,
                "Gastritis":Gastritis,
                "Cystitis":Cystitis,
                "Pyelonephritis":Pyelonephritis,
                "Renal_Calculi":Renal_Calculi,
                "Diverticulitis":Diverticulitis,
                "Interstinal_Obstruction":Interstinal_Obstruction,
                "Inflammatory_Bowel_Disease":Inflammatory_Bowel_Disease,
                "Irritable_Bowel_Disease":Irritable_Bowel_Disease,
                "Pancreatitis":Pancreatitis,
                "Endometriosis":Endometriosis,
                "Anxiety":Anxiety,
                "Depression":Depression,
                "Cardiac_Ischemia":Cardiac_Ischemia,
                "Pulmonary_Embolism":Pulmonary_Embolism,
                "Pleurisy":Pleurisy,
                "Costochondritis":Costochondritis,
                "Pneumonia":Pneumonia,
                "Viral_Bronchitis":Viral_Bronchitis,
                "Asthma":Asthma,
                "Chronic_Heart_Failure":Chronic_Heart_Failure,
                "Chronic_Lung_Disease":Chronic_Lung_Disease,
                "Lunc_Cancer":Lunc_Cancer,
                "COVID":COVID,
                "Diabetes":Diabetes,
                "Viral_Fever":Viral_Fever,
                "Cholangitis":Cholangitis,
                "Endocarditis":Endocarditis,
                "Cellulitis":Cellulitis,
                "Urinary_Tract_Infection":Urinary_Tract_Infection,
                "Osteomyelitis":Osteomyelitis,
                "Meningitis":Meningitis

            }

            print ("all data",context2)


            x = sorted(((v,k) for k,v in context2.items() ))

        
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            third_name = x[-3][1]
            third_value = x[-3][0]
            fourth_name = x[-4][1]
            fourth_value = x[-4][0]

            print("first_value",first_value)
            print("second_value",second_value)
            print("third_value",third_value)
            print("fourth_value",fourth_value)
            context3 = {
                first_name: first_value,
                second_name :second_value,
                third_name :third_value,
                fourth_name : fourth_value,

            }

            print("Context3" , context3 )

            return JsonResponse({"status":context3})
        except Exception as e:
            print("Error Receiving Form Data", e)
            return render (request,"cough_fever_result.html",{'context1':"in except"})
                    


@csrf_exempt
def api_survey(request):
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    survey_api= "https://api.surveysparrow.com/v3/responses"
    response = requests.get(api_url)
    response1 = requests.get(survey_api)
    response.json()
    response1.json()
    print("response from api is",response.json())
    print("response from survey_api is",response1.json())
    return render(request,"combined module.html" )

@csrf_exempt
def fever_abd_updated(request):
    if request.method == 'GET':
        return render(request,"fever_abd_frontend_updated.html" )


@csrf_exempt
def fever_abd_updated_result(request):
    if request.method == 'POST':
        print('POST data is', request.POST)
        print('post BODY', request.body)
        global Appendicitis
        global Cholecystitis
        global Gastritis
        global Cystitis
        global Pyelonephritis
        global Renal_Calculi
        global Diverticulitis
        global Intestinal_Obstruction
        global Inflammatory_Bowel_Disease
        global Irritable_Bowel_Disease
        global Pancreatitis
        global Endometriosis
        global Low_Mood
        global Cardiac_Ischemia
        global Pulmonary_Embolism
        global Pleurisy
        global Costochondritis
        global Pneumonia
        global Viral_Bronchitis
        global Asthma
        global Chronic_Heart_Failure
        global Chronic_Lung_Disease
        global Lung_Cancer
        global COVID
        global Diabetes
        global Viral_Fever
        global Cholangitis
        global Endocarditis
        global Cellulitis
        global Urinary_Tract_Infection
        global Osteomyelitis
        global Meningitis





        Appendicitis=0
        Cholecystitis=0
        Gastritis=0
        Cystitis=0
        Pyelonephritis=0
        Renal_Calculi=0
        Diverticulitis=0
        Intestinal_Obstruction=0
        Inflammatory_Bowel_Disease=0
        Irritable_Bowel_Disease=0
        Pancreatitis=0
        Endometriosis=0
        Low_Mood=0
        Cardiac_Ischemia=0
        Pulmonary_Embolism=0
        Pleurisy=0
        Costochondritis=0
        Pneumonia=0
        Viral_Bronchitis=0
        Asthma=0
        Chronic_Heart_Failure=0
        Chronic_Lung_Disease=0
        Lung_Cancer=0
        COVID=0
        Diabetes=0
        Viral_Fever=0
        Cholangitis=0
        Endocarditis=0
        Cellulitis=0
        Urinary_Tract_Infection=0
        Osteomyelitis=0
        Meningitis=0

        context1 ={

                        "Appendicitis": Appendicitis,            
                        "Cholecystitis" : Cholecystitis,
                        "Gastritis" : Gastritis,
                        "Cystitis" : Cystitis,
                        "Pyelonephritis" : Pyelonephritis,
                        "Renal_Calculi" :  Renal_Calculi,
                        "Diverticulitis" : Diverticulitis,
                        "Intestinal Obstruction" : Intestinal_Obstruction,
                        "Inflammatory Bowel Disease" : Inflammatory_Bowel_Disease,
                        "Irritable Bowel Disease" : Irritable_Bowel_Disease,
                        "Pancreatitis" : Pancreatitis, 
                        "Endometriosis" :  Endometriosis,
                        "Low Mood" : Low_Mood,
                        "Cardiac Ischemia":Cardiac_Ischemia,
                        "Pulmonary Embolism":Pulmonary_Embolism,
                        "Pleurisy":Pleurisy,
                        "Costochondritis":Costochondritis,
                        "Pneumonia":Pneumonia,
                        "Viral Bronchitis":Viral_Bronchitis,
                        "Asthma":Asthma,
                        "Chronic Heart Failure":Chronic_Heart_Failure,
                        "Chronic Lung Disease" :Chronic_Lung_Disease,
                        "Lung Cancer":Lung_Cancer,
                        "COVID_":COVID,
                        "Diabetes" : Diabetes,
                        "Viral Fever":Viral_Fever,
                        "Cholangitis" : Cholangitis,
                        "Endocarditis" : Endocarditis,
                        "Cellulitis" : Cellulitis,
                        "Urinary Tract Infection" : Urinary_Tract_Infection,
                        "Osteomyelitis" : Osteomyelitis,
                        "Meningitis": Meningitis
                               
                            }

        print("context1",context1 )

    

        updated_data= dict(request.POST.lists())

        try:
            an1=request.POST['fa1']
            print("Your an1 is", an1)
        except:
            an1 =" "
            pass

        try:
            an2=request.POST['fa2']
            print("Your an2 is", an2)
        except:
            an2 =" "
            pass

        try:
            an3=request.POST['fa3']
            print("Your an3 is", an3)
        except:
            an3 =" "
            pass

        try:
            an4=request.POST['fa4']
            print("Your an4 is", an4)
        except:
            an4 =" "
            pass

        try:
            an5=request.POST['fa5']
            print("Your an5 is", an5)
        except:
            an5 =" "
            pass

    
        if an1== 'Yes':
            Viral_Bronchitis +=1
            COVID +=1
      

        if an2== 'Yes':
            Pneumonia +=1


        if an3== 'Yes':
            Viral_Bronchitis +=1
            Pneumonia +=1
            

        if an4== 'Yes':
            Viral_Bronchitis +=1
            COVID +=1
            Pneumonia +=1
      

        if an5== 'Yes':
            COVID +=1
           


        context2 ={

                    "Appendicitis": Appendicitis,            
                    "Cholecystitis" : Cholecystitis,
                    "Gastritis" : Gastritis,
                    "Cystitis" : Cystitis,
                    "Pyelonephritis" : Pyelonephritis,
                    "Renal_Calculi" :  Renal_Calculi,
                    "Diverticulitis" : Diverticulitis,
                    "Intestinal Obstruction" : Intestinal_Obstruction,
                    "Inflammatory Bowel Disease" : Inflammatory_Bowel_Disease,
                    "Irritable Bowel Disease" : Irritable_Bowel_Disease,
                    "Pancreatitis" : Pancreatitis, 
                    "Endometriosis" :  Endometriosis,
                    "Low Mood" : Low_Mood,
                    "Cardiac Ischemia":Cardiac_Ischemia,
                    "Pulmonary Embolism":Pulmonary_Embolism,
                    "Pleurisy":Pleurisy,
                    "Costochondritis":Costochondritis,
                    "Pneumonia":Pneumonia,
                    "Viral Bronchitis":Viral_Bronchitis,
                    "Asthma":Asthma,
                    "Chronic Heart Failure":Chronic_Heart_Failure,
                    "Chronic Lung Disease" :Chronic_Lung_Disease,
                    "Lung Cancer":Lung_Cancer,
                    "COVID_":COVID,
                    "Diabetes" : Diabetes,
                    "Viral Fever":Viral_Fever,
                    "Cholangitis" : Cholangitis,
                    "Endocarditis" : Endocarditis,
                    "Cellulitis" : Cellulitis,
                    "Urinary Tract Infection" : Urinary_Tract_Infection,
                    "Osteomyelitis" : Osteomyelitis,
                    "Meningitis": Meningitis
                            
                            }

        print("context2",context2 )

        x = sorted(((v,k) for k,v in context2.items() ))
        print ("len of x",len(x))

    
        first_name = x[-1][1]
        first_value = x[-1][0]
        second_name = x[-2][1]
        second_value = x[-2][0]
        third_name = x[-3][1]
        third_value = x[-3][0]
        fourth_name = x[-4][1]
        fourth_value = x[-4][0]
        
        print("first_name",first_name)
        print("first_value",first_value)
        print("second_value",second_value)
        print("third_value",third_value)
        print("fourth_value",fourth_value)
        sorted_context2 = {
            first_name: first_value,
            second_name :second_value,
            third_name :third_value,
            fourth_name : fourth_value,

        }

        print("top 4 from context2 : " , sorted_context2 )

        return render(request,"FA_overall_result_display.html",{'context':sorted_context2  })

        # if first_name == 'Pneumonia': 
        # # if an7== 'Yes':
        #     print("if condition is executed")
        #     return render(request,"pnemonia_qns.html" )
        # # if first_name== 'Viral_Bronchitis': 
        # #     return render(request,"fever_abd_frontend_4.html" )

    return render(request,"fever_abd_frontend_updated.html" )


@csrf_exempt
def pnemonia_VB_qns(request):
    global Appendicitis
    global Cholecystitis
    global Gastritis
    global Cystitis
    global Pyelonephritis
    global Renal_Calculi
    global Diverticulitis
    global Intestinal_Obstruction
    global Inflammatory_Bowel_Disease
    global Irritable_Bowel_Disease
    global Pancreatitis
    global Endometriosis
    global Low_Mood
    global Cardiac_Ischemia
    global Pulmonary_Embolism
    global Pleurisy
    global Costochondritis
    global Pneumonia
    global Viral_Bronchitis
    global Asthma
    global Chronic_Heart_Failure
    global Chronic_Lung_Disease
    global Lung_Cancer
    global COVID
    global Diabetes
    global Viral_Fever
    global Cholangitis
    global Endocarditis
    global Cellulitis
    global Urinary_Tract_Infection
    global Osteomyelitis
    global Meningitis

    


    context3 ={

                    "Appendicitis": Appendicitis,            
                    "Cholecystitis" : Cholecystitis,
                    "Gastritis" : Gastritis,
                    "Cystitis" : Cystitis,
                    "Pyelonephritis" : Pyelonephritis,
                    "Renal_Calculi" :  Renal_Calculi,
                    "Diverticulitis" : Diverticulitis,
                    "Intestinal Obstruction" : Intestinal_Obstruction,
                    "Inflammatory Bowel Disease" : Inflammatory_Bowel_Disease,
                    "Irritable Bowel Disease" : Irritable_Bowel_Disease,
                    "Pancreatitis" : Pancreatitis, 
                    "Endometriosis" :  Endometriosis,
                    "Low Mood" : Low_Mood,
                    "Cardiac Ischemia":Cardiac_Ischemia,
                    "Pulmonary Embolism":Pulmonary_Embolism,
                    "Pleurisy":Pleurisy,
                    "Costochondritis":Costochondritis,
                    "Pneumonia":Pneumonia,
                    "Viral Bronchitis":Viral_Bronchitis,
                    "Asthma":Asthma,
                    "Chronic Heart Failure":Chronic_Heart_Failure,
                    "Chronic Lung Disease" :Chronic_Lung_Disease,
                    "Lung Cancer":Lung_Cancer,
                    "COVID_":COVID,
                    "Diabetes" : Diabetes,
                    "Viral Fever":Viral_Fever,
                    "Cholangitis" : Cholangitis,
                    "Endocarditis" : Endocarditis,
                    "Cellulitis" : Cellulitis,
                    "Urinary Tract Infection" : Urinary_Tract_Infection,
                    "Osteomyelitis" : Osteomyelitis,
                    "Meningitis": Meningitis
                            
                            }

    print("context3",context3 )

    x = sorted(((v,k) for k,v in context3.items() ))
    print ("len of x",len(x))


    first_name = x[-1][1]
    first_value = x[-1][0]
    second_name = x[-2][1]
    second_value = x[-2][0]
    third_name = x[-3][1]
    third_value = x[-3][0]
    fourth_name = x[-4][1]
    fourth_value = x[-4][0]
    
    print("first_name",first_name)
    print("first_value",first_value)
    print("second_value",second_value)
    print("third_value",third_value)
    print("fourth_value",fourth_value)
    sorted_context3 = {
        first_name: first_value,
        second_name :second_value,
        third_name :third_value,
        fourth_name : fourth_value,

    }

    print("top 4 from context3 : " , sorted_context3 )

    if first_name == 'Pneumonia': 
        # if an7== 'Yes':
        print("if condition is executed")
        return render(request,"pnemonia_qns.html" )
    if first_name== 'Viral Bronchitis': 
        return render(request,"VB_qns.html" )

    return render(request, "FA_overall_result_display.html")





@csrf_exempt
def pnemonia_VB_qns_result(request):
    if request.method == 'POST':
        print('POST data is', request.POST)
        print('post BODY', request.body)
        global Appendicitis
        global Cholecystitis
        global Gastritis
        global Cystitis
        global Pyelonephritis
        global Renal_Calculi
        global Diverticulitis
        global Intestinal_Obstruction
        global Inflammatory_Bowel_Disease
        global Irritable_Bowel_Disease
        global Pancreatitis
        global Endometriosis
        global Low_Mood
        global Cardiac_Ischemia
        global Pulmonary_Embolism
        global Pleurisy
        global Costochondritis
        global Pneumonia
        global Viral_Bronchitis
        global Asthma
        global Chronic_Heart_Failure
        global Chronic_Lung_Disease
        global Lung_Cancer
        global COVID
        global Diabetes
        global Viral_Fever
        global Cholangitis
        global Endocarditis
        global Cellulitis
        global Urinary_Tract_Infection
        global Osteomyelitis
        global Meningitis

        Appendicitis=0
        Cholecystitis=0
        Gastritis=0
        Cystitis=0
        Pyelonephritis=0
        Renal_Calculi=0
        Diverticulitis=0
        Intestinal_Obstruction=0
        Inflammatory_Bowel_Disease=0
        Irritable_Bowel_Disease=0
        Pancreatitis=0
        Endometriosis=0
        Low_Mood=0
        Cardiac_Ischemia=0
        Pulmonary_Embolism=0
        Pleurisy=0
        Costochondritis=0
        Pneumonia=0
        Viral_Bronchitis=0
        Asthma=0
        Chronic_Heart_Failure=0
        Chronic_Lung_Disease=0
        Lung_Cancer=0
        COVID=0
        Diabetes=0
        Viral_Fever=0
        Cholangitis=0
        Endocarditis=0
        Cellulitis=0
        Urinary_Tract_Infection=0
        Osteomyelitis=0
        Meningitis=0


        try:
            P_an1=request.POST['pn1']
            print("Your P_an1 is", P_an1)
        except:
            P_an1 =" "
            pass

        try:
            P_an2=request.POST['pn2']
            print("Your P_an2 is", P_an2)
        except:
            P_an2 =" "
            pass

        try:
            P_an3=request.POST['pn3']
            print("Your P_an3 is", P_an3)
        except:
            P_an3 =" "
            pass

        try:
            P_an4=request.POST['pn4']
            print("Your P_an4 is", P_an4)
        except:
            P_an4 =" "
            pass

        try:
            VB_an1=request.POST['vb1']
            print("Your VB_an1 is", VB_an1)
        except:
            VB_an1 =" "
            pass

        try:
            VB_an2=request.POST['vb2']
            print("Your VB_an2 is", VB_an2)
        except:
            VB_an2 =" "
            pass


        if P_an1== 'Yes':
            Pleurisy +=1
           
      

        if P_an2== 'Yes':
            Lung_Cancer +=1
            Pulmonary_Embolism +=1
            


        if P_an3== 'Yes':
            Lung_Cancer +=1
            

        if P_an4== 'Yes':
            Pleurisy +=1
            Pulmonary_Embolism +=1


        if VB_an1== 'Yes':
            Asthma +=1
        
        if VB_an2== 'Yes':
            Asthma +=1

        context4 ={

                    "Appendicitis": Appendicitis,            
                    "Cholecystitis" : Cholecystitis,
                    "Gastritis" : Gastritis,
                    "Cystitis" : Cystitis,
                    "Pyelonephritis" : Pyelonephritis,
                    "Renal_Calculi" :  Renal_Calculi,
                    "Diverticulitis" : Diverticulitis,
                    "Intestinal Obstruction" : Intestinal_Obstruction,
                    "Inflammatory Bowel Disease" : Inflammatory_Bowel_Disease,
                    "Irritable Bowel Disease" : Irritable_Bowel_Disease,
                    "Pancreatitis" : Pancreatitis, 
                    "Endometriosis" :  Endometriosis,
                    "Low Mood" : Low_Mood,
                    "Cardiac Ischemia":Cardiac_Ischemia,
                    "Pulmonary Embolism":Pulmonary_Embolism,
                    "Pleurisy":Pleurisy,
                    "Costochondritis":Costochondritis,
                    "Pneumonia":Pneumonia,
                    "Viral Bronchitis":Viral_Bronchitis,
                    "Asthma":Asthma,
                    "Chronic Heart Failure":Chronic_Heart_Failure,
                    "Chronic Lung Disease" :Chronic_Lung_Disease,
                    "Lung Cancer":Lung_Cancer,
                    "COVID_":COVID,
                    "Diabetes" : Diabetes,
                    "Viral Fever":Viral_Fever,
                    "Cholangitis" : Cholangitis,
                    "Endocarditis" : Endocarditis,
                    "Cellulitis" : Cellulitis,
                    "Urinary Tract Infection" : Urinary_Tract_Infection,
                    "Osteomyelitis" : Osteomyelitis,
                    "Meningitis": Meningitis
                            
                            }

        print("context4",context4 )

        x = sorted(((v,k) for k,v in context4.items() ))
        print ("len of x",len(x))

    
        first_name = x[-1][1]
        first_value = x[-1][0]
        second_name = x[-2][1]
        second_value = x[-2][0]
        third_name = x[-3][1]
        third_value = x[-3][0]
        fourth_name = x[-4][1]
        fourth_value = x[-4][0]
        
        print("first_name",first_name)
        print("first_value",first_value)
        print("second_value",second_value)
        print("third_value",third_value)
        print("fourth_value",fourth_value)
        sorted_context4 = {
            first_name: first_value,
            second_name :second_value,
            third_name :third_value,
            fourth_name : fourth_value,

        }

        print("top 4 from context4 : " , sorted_context4 )
            
    return render(request,"Pnemonia_result_display.html",{'context':sorted_context4  })








@csrf_exempt
def fever_abd_part1(request):
    if request.method == 'GET':
        return render(request,"fever_abd_frontend_1.html" )



@csrf_exempt
def fever_abd_part1_result(request):
    if request.method == 'POST':
        print('POST data is', request.POST)
        print('post BODY', request.body)
        global Appendicitis
        global Cholecystitis
        global Gastritis
        global Cystitis
        global Pyelonephritis
        global Renal_Calculi
        global Diverticulitis
        global Intestinal_Obstruction
        global Inflammatory_Bowel_Disease
        global Irritable_Bowel_Disease
        global Pancreatitis
        global Endometriosis
        global Low_Mood
        global Cardiac_Ischemia
        global Pulmonary_Embolism
        global Pleurisy
        global Costochondritis
        global Pneumonia
        global Viral_Bronchitis
        global Asthma
        global Chronic_Heart_Failure
        global Chronic_Lung_Disease
        global Lung_Cancer
        global COVID
        global Diabetes
        global Viral_Fever
        global Cholangitis
        global Endocarditis
        global Cellulitis
        global Urinary_Tract_Infection
        global Osteomyelitis
        global Meningitis





        Appendicitis=0
        Cholecystitis=0
        Gastritis=0
        Cystitis=0
        Pyelonephritis=0
        Renal_Calculi=0
        Diverticulitis=0
        Intestinal_Obstruction=0
        Inflammatory_Bowel_Disease=0
        Irritable_Bowel_Disease=0
        Pancreatitis=0
        Endometriosis=0
        Low_Mood=0
        Cardiac_Ischemia=0
        Pulmonary_Embolism=0
        Pleurisy=0
        Costochondritis=0
        Pneumonia=0
        Viral_Bronchitis=0
        Asthma=0
        Chronic_Heart_Failure=0
        Chronic_Lung_Disease=0
        Lung_Cancer=0
        COVID=0
        Diabetes=0
        Viral_Fever=0
        Cholangitis=0
        Endocarditis=0
        Cellulitis=0
        Urinary_Tract_Infection=0
        Osteomyelitis=0
        Meningitis=0

        context1 ={

                        "Appendicitis": Appendicitis,            
                        "Cholecystitis" : Cholecystitis,
                        "Gastritis" : Gastritis,
                        "Cystitis" : Cystitis,
                        "Pyelonephritis" : Pyelonephritis,
                        "Renal_Calculi" :  Renal_Calculi,
                        "Diverticulitis" : Diverticulitis,
                        "Intestinal Obstruction" : Intestinal_Obstruction,
                        "Inflammatory Bowel Disease" : Inflammatory_Bowel_Disease,
                        "Irritable Bowel Disease" : Irritable_Bowel_Disease,
                        "Pancreatitis" : Pancreatitis, 
                        "Endometriosis" :  Endometriosis,
                        "Low Mood" : Low_Mood,
                        "Cardiac Ischemia":Cardiac_Ischemia,
                        "Pulmonary Embolism":Pulmonary_Embolism,
                        "Pleurisy":Pleurisy,
                        "Costochondritis":Costochondritis,
                        "Pneumonia":Pneumonia,
                        "Viral Bronchitis":Viral_Bronchitis,
                        "Asthma":Asthma,
                        "Chronic Heart Failure":Chronic_Heart_Failure,
                        "Chronic Lung Disease" :Chronic_Lung_Disease,
                        "Lung Cancer":Lung_Cancer,
                        "COVID_":COVID,
                        "Diabetes" : Diabetes,
                        "Viral Fever":Viral_Fever,
                        "Cholangitis" : Cholangitis,
                        "Endocarditis" : Endocarditis,
                        "Cellulitis" : Cellulitis,
                        "Urinary Tract Infection" : Urinary_Tract_Infection,
                        "Osteomyelitis" : Osteomyelitis,
                        "Meningitis": Meningitis
                               
                            }

        print("context1",context1 )

    

        updated_data= dict(request.POST.lists())

        try:
            an1=request.POST['fev_abd1']
            print("Your an1 is", an1)
        except:
            an1 =" "
            pass

        try:
            an2=request.POST['fev_abd2']
            print("Your an2 is", an2)
        except:
            an2 =" "
            pass

        try:
            an3=request.POST['fev_abd3']
            print("Your an3 is", an3)
        except:
            an3 =" "
            pass

        try:
            an4=request.POST['fev_abd4']
            print("Your an4 is", an4)
        except:
            an4 =" "
            pass

        try:
            an5=request.POST['fev_abd5']
            print("Your an5 is", an5)
        except:
            an5 =" "
            pass

        try:
            an6=request.POST['fev_abd6']
            print("Your an6 is", an6)
        except:
            an6 =" "
            pass

        try:
            an7=request.POST['fev_abd7']
            print("Your an7 is", an7)
        except:
            an7 =" "
            pass

      

        if an2== 'Yes':
            Cystitis +=2
            Pyelonephritis +=2.5
            Renal_Calculi +=2.5
            Urinary_Tract_Infection +=1.43


        if an7== 'Yes':
            Cystitis+=2
            Pyelonephritis+=2.5
            Diverticulitis+=1.25
            Appendicitis += 2.5 
            Inflammatory_Bowel_Disease += 1.25
            Irritable_Bowel_Disease += 3.33
            Endometriosis += 2
            Urinary_Tract_Infection += 1.43

        context2 ={

                    "Appendicitis": Appendicitis,            
                    "Cholecystitis" : Cholecystitis,
                    "Gastritis" : Gastritis,
                    "Cystitis" : Cystitis,
                    "Pyelonephritis" : Pyelonephritis,
                    "Renal_Calculi" :  Renal_Calculi,
                    "Diverticulitis" : Diverticulitis,
                    "Intestinal Obstruction" : Intestinal_Obstruction,
                    "Inflammatory Bowel Disease" : Inflammatory_Bowel_Disease,
                    "Irritable Bowel Disease" : Irritable_Bowel_Disease,
                    "Pancreatitis" : Pancreatitis, 
                    "Endometriosis" :  Endometriosis,
                    "Low Mood" : Low_Mood,
                    "Cardiac Ischemia":Cardiac_Ischemia,
                    "Pulmonary Embolism":Pulmonary_Embolism,
                    "Pleurisy":Pleurisy,
                    "Costochondritis":Costochondritis,
                    "Pneumonia":Pneumonia,
                    "Viral Bronchitis":Viral_Bronchitis,
                    "Asthma":Asthma,
                    "Chronic Heart Failure":Chronic_Heart_Failure,
                    "Chronic Lung Disease" :Chronic_Lung_Disease,
                    "Lung Cancer":Lung_Cancer,
                    "COVID_":COVID,
                    "Diabetes" : Diabetes,
                    "Viral Fever":Viral_Fever,
                    "Cholangitis" : Cholangitis,
                    "Endocarditis" : Endocarditis,
                    "Cellulitis" : Cellulitis,
                    "Urinary Tract Infection" : Urinary_Tract_Infection,
                    "Osteomyelitis" : Osteomyelitis,
                    "Meningitis": Meningitis
                            
                            }

        print("context2",context2 )

        x = sorted(((v,k) for k,v in context2.items() ))
        print ("len of x",len(x))

    
        first_name = x[-1][1]
        first_value = x[-1][0]
        second_name = x[-2][1]
        second_value = x[-2][0]
        third_name = x[-3][1]
        third_value = x[-3][0]
        fourth_name = x[-4][1]
        fourth_value = x[-4][0]
        
        print("first_name",first_name)
        print("first_value",first_value)
        print("second_value",second_value)
        print("third_value",third_value)
        print("fourth_value",fourth_value)
        sorted_context2 = {
            first_name: first_value,
            second_name :second_value,
            third_name :third_value,
            fourth_name : fourth_value,

        }

        print("top 4 from context2 : " , sorted_context2 )

        if first_name == 'Pyelonephritis': 
        # if an7== 'Yes':
            print("if condition is executed")
            return render(request,"fever_abd_frontend_3.html" )
        if first_name== 'Renal_Calculi': 
            return render(request,"fever_abd_frontend_4.html" )


    return render(request,"fever_abd_frontend_2.html" )




@csrf_exempt
def fever_abd_final_set(request):
    global Appendicitis
    global Cholecystitis
    global Gastritis
    global Cystitis
    global Pyelonephritis
    global Renal_Calculi
    global Diverticulitis
    global Intestinal_Obstruction
    global Inflammatory_Bowel_Disease
    global Irritable_Bowel_Disease
    global Pancreatitis
    global Endometriosis
    global Low_Mood
    global Cardiac_Ischemia
    global Pulmonary_Embolism
    global Pleurisy
    global Costochondritis
    global Pneumonia
    global Viral_Bronchitis
    global Asthma
    global Chronic_Heart_Failure
    global Chronic_Lung_Disease
    global Lung_Cancer
    global COVID
    global Diabetes
    global Viral_Fever
    global Cholangitis
    global Endocarditis
    global Cellulitis
    global Urinary_Tract_Infection
    global Osteomyelitis
    global Meningitis

    context3 ={

                    "Appendicitis": Appendicitis,            
                    "Cholecystitis" : Cholecystitis,
                    "Gastritis" : Gastritis,
                    "Cystitis" : Cystitis,
                    "Pyelonephritis" : Pyelonephritis,
                    "Renal_Calculi" :  Renal_Calculi,
                    "Diverticulitis" : Diverticulitis,
                    "Intestinal Obstruction" : Intestinal_Obstruction,
                    "Inflammatory Bowel Disease" : Inflammatory_Bowel_Disease,
                    "Irritable Bowel Disease" : Irritable_Bowel_Disease,
                    "Pancreatitis" : Pancreatitis, 
                    "Endometriosis" :  Endometriosis,
                    "Low Mood" : Low_Mood,
                    "Cardiac Ischemia":Cardiac_Ischemia,
                    "Pulmonary Embolism":Pulmonary_Embolism,
                    "Pleurisy":Pleurisy,
                    "Costochondritis":Costochondritis,
                    "Pneumonia":Pneumonia,
                    "Viral Bronchitis":Viral_Bronchitis,
                    "Asthma":Asthma,
                    "Chronic Heart Failure":Chronic_Heart_Failure,
                    "Chronic Lung Disease" :Chronic_Lung_Disease,
                    "Lung Cancer":Lung_Cancer,
                    "COVID_":COVID,
                    "Diabetes" : Diabetes,
                    "Viral Fever":Viral_Fever,
                    "Cholangitis" : Cholangitis,
                    "Endocarditis" : Endocarditis,
                    "Cellulitis" : Cellulitis,
                    "Urinary Tract Infection" : Urinary_Tract_Infection,
                    "Osteomyelitis" : Osteomyelitis,
                    "Meningitis": Meningitis
                            
                            }

        
    print("context3",context3 )



    if request.method == 'POST':
        

        try:
            an1=request.POST['fev_abd8']
            print("Your an1 is", an1)
        except:
            an1 =" "
            pass

        try:
            an2=request.POST['fev_abd9']
            print("Your an2 is", an2)
        except:
            an2 =" "
            pass

        try:
            an3=request.POST['fev_abd10']
            print("Your an3 is", an3)
        except:
            an3 =" "
            pass


       



        if an1=='Yes':
            Urinary_Tract_Infection += 1.43

        if an2=='Yes' :
            Endometriosis += 2

        if an3=='Yes' :
            Cholecystitis+=1.25
            Diverticulitis+=1.25
            Appendicitis += 2.5
            Inflammatory_Bowel_Disease += 1.25
            Urinary_Tract_Infection += 1.43


        context4 ={

                        "Appendicitis": Appendicitis,            
                        "Cholecystitis" : Cholecystitis,
                        "Gastritis" : Gastritis,
                        "Cystitis" : Cystitis,
                        "Pyelonephritis" : Pyelonephritis,
                        "Renal_Calculi" :  Renal_Calculi,
                        "Diverticulitis" : Diverticulitis,
                        "Intestinal Obstruction" : Intestinal_Obstruction,
                        "Inflammatory Bowel Disease" : Inflammatory_Bowel_Disease,
                        "Irritable Bowel Disease" : Irritable_Bowel_Disease,
                        "Pancreatitis" : Pancreatitis, 
                        "Endometriosis" :  Endometriosis,
                        "Low Mood" : Low_Mood,
                        "Cardiac Ischemia":Cardiac_Ischemia,
                        "Pulmonary Embolism":Pulmonary_Embolism,
                        "Pleurisy":Pleurisy,
                        "Costochondritis":Costochondritis,
                        "Pneumonia":Pneumonia,
                        "Viral Bronchitis":Viral_Bronchitis,
                        "Asthma":Asthma,
                        "Chronic Heart Failure":Chronic_Heart_Failure,
                        "Chronic Lung Disease" :Chronic_Lung_Disease,
                        "Lung Cancer":Lung_Cancer,
                        "COVID_":COVID,
                        "Diabetes" : Diabetes,
                        "Viral Fever":Viral_Fever,
                        "Cholangitis" : Cholangitis,
                        "Endocarditis" : Endocarditis,
                        "Cellulitis" : Cellulitis,
                        "Urinary Tract Infection" : Urinary_Tract_Infection,
                        "Osteomyelitis" : Osteomyelitis,
                        "Meningitis": Meningitis
                               
                            }

        print("context4",context4 )

        x = sorted(((v,k) for k,v in context4.items() ))
        print ("len of x",len(x))

    
        first_name = x[-1][1]
        first_value = x[-1][0]
        second_name = x[-2][1]
        second_value = x[-2][0]
        third_name = x[-3][1]
        third_value = x[-3][0]
        fourth_name = x[-4][1]
        fourth_value = x[-4][0]
        

        print("first_value",first_value)
        print("second_value",second_value)
        print("third_value",third_value)
        print("fourth_value",fourth_value)
        sorted_context4 = {
            first_name: first_value,
            second_name :second_value,
            third_name :third_value,
            fourth_name : fourth_value,

        }

        print("top 4 from context4 : " , sorted_context4 )

    return render(request,"fever_abd_frontend_2.html" )


   
   




@csrf_exempt
def combined_Low_mood_frontend(request):
    if request.method == 'GET':
        return render(request,"combined_low_mood.html" )

@csrf_exempt
def combined_low_mood_result(request):
    if request.method == 'POST':
        print('POST data is', request.POST)
        print('post BODY', request.body)
        Appendicitis=0
        Cholecystitis=0
        Gastritis=0
        Cystitis=0
        Pyelonephritis=0
        Renal_Calculi=0
        Diverticulitis=0
        Intestinal_Obstruction=0
        Inflammatory_Bowel_Disease=0
        Irritable_Bowel_Disease=0
        Pancreatitis=0
        Endometriosis=0
        Low_Mood=0
        Cardiac_Ischemia=0
        Pulmonary_Embolism=0
        Pleurisy=0
        Costochondritis=0
        Pneumonia=0
        Viral_Bronchitis=0
        Asthma=0
        Chronic_Heart_Failure=0
        Chronic_Lung_Disease=0
        Lung_Cancer=0
        COVID=0
        Diabetes=0
        Viral_Fever=0
        Cholangitis=0
        Endocarditis=0
        Cellulitis=0
        Urinary_Tract_Infection=0
        Osteomyelitis=0
        Meningitis=0

        context1 ={

                        "Appendicitis": Appendicitis,            
                        "Cholecystitis" : Cholecystitis,
                        "Gastritis" : Gastritis,
                        "Cystitis" : Cystitis,
                        "Pyelonephritis" : Pyelonephritis,
                        "Renal_Calculi" :  Renal_Calculi,
                        "Diverticulitis" : Diverticulitis,
                        "Intestinal Obstruction" : Intestinal_Obstruction,
                        "Inflammatory Bowel Disease" : Inflammatory_Bowel_Disease,
                        "Irritable Bowel Disease" : Irritable_Bowel_Disease,
                        "Pancreatitis" : Pancreatitis, 
                        "Endometriosis" :  Endometriosis,
                        "Low Mood" : Low_Mood,
                        "Cardiac Ischemia":Cardiac_Ischemia,
                        "Pulmonary Embolism":Pulmonary_Embolism,
                        "Pleurisy":Pleurisy,
                        "Costochondritis":Costochondritis,
                        "Pneumonia":Pneumonia,
                        "Viral Bronchitis":Viral_Bronchitis,
                        "Asthma":Asthma,
                        "Chronic Heart Failure":Chronic_Heart_Failure,
                        "Chronic Lung Disease" :Chronic_Lung_Disease,
                        "Lung Cancer":Lung_Cancer,
                        "COVID_":COVID,
                        "Diabetes" : Diabetes,
                        "Viral Fever":Viral_Fever,
                        "Cholangitis" : Cholangitis,
                        "Endocarditis" : Endocarditis,
                        "Cellulitis" : Cellulitis,
                        "Urinary Tract Infection" : Urinary_Tract_Infection,
                        "Osteomyelitis" : Osteomyelitis,
                        "Meningitis": Meningitis
                               
                            }

        print("context1",context1 )

    

        updated_data= dict(request.POST.lists())

        try:
            an1=request.POST['local_clm1']
            print("Your an1 is", an1)
        except:
            an1 =" "
            pass

        try:
            diagnosis=updated_data['local_clm2[0]']
            print("Your diagnosis is", diagnosis)
            print("Your cough diagnosis is", diagnosis[0])
            print("Your chest pain diagnosis is", diagnosis[1])
        except:
            diagnosis =" "
            pass

       
        try:
            age = int (request.POST['local_clm3[field_1]'])
            print("Your are age", age)
        except:
            age = 0
            pass

        try:
            gender=request.POST['local_clm3[field_2]']
            print("Your are gender", gender)
        except:
            gender =" "
            pass

        try:
            weight=request.POST['local_clm3[field_3]']
            print("Your are weight", weight)
        except Exception as e:
            print("Error is", e)
            
            weight =" "
            pass

        try:
            height=request.POST['local_clm3[field_4]']
            print("Your are height", height)
        except Exception as e:
            print("Error is", e)

            height =" "
            pass

        # weight= request.POST['comb_data[field_3]'] 
        print("Your weight is ", weight )
        print ("height",height)
        # height= request.POST['comb_data[field_4]']
        height_in_meter = round((int(height)/100),2)
       
        BMI = round((int(weight) / (height_in_meter * height_in_meter)),2)
        print("Your calculated BMI is", BMI)


        try:
            email=request.POST['local_clm3[field_5]']
            print("Your are email", email)
        except:
            email =" "
            pass

        try:
            daibetes=request.POST['local_clm4[0]']
            print("Your are daibetes", daibetes)

        except:
            daibetes =" "
            pass

        try:
            Hypertension=request.POST['local_clm4[1]']
            print("Your are Hypertension", Hypertension)

        except:
            Hypertension =" "
            pass

        try:
            Heart_disease=request.POST['local_clm4[2]']
            print("Your are Heart_disease", Heart_disease)

        except:
            Heart_disease =" "
            pass

        try:
            Strokes=request.POST['local_clm4[3]']
            print("Your are Strokes", Strokes)

        except:
            Strokes =" "
            pass

        try:
            all_above=request.POST['local_clm4[4]']
            print("Your are all_above", all_above)

        except:
            all_above =" "
            pass

        try:
            smoke=request.POST['local_clm5[0]']
            print("Your are smoke", smoke)

        except:
            smoke =" "
            pass

        try:
            alcohol=request.POST['local_clm5[1]']
            print("Your are alcohol", alcohol)

        except:
            alcohol =" "
            pass

        try:
            exercise=request.POST['local_clm5[2]']
            print("Your are exercise", exercise)

        except:
            exercise =" "
            pass

        try:
            calories=request.POST['local_clm5[3]']
            print("Your are calories", calories)

        except:
            calories =" "
            pass

        try:
            covid=request.POST['local_clm5[4]']
            print("Your are covid", covid)

        except:
            covid =" "
            pass

        try:
            life=request.POST['local_clm5[5]']
            print("Your are life", life)

        except:
            life =" "
            pass


       

        try:
            an6=request.POST['local_clm6']
            print("Your are an6", an6)
        except:
            an6 =" "
            pass

        try:
            cough_qn1=request.POST['local_clm7[0]']
            print("Your are cough_qn1", cough_qn1)
        except:
            cough_qn1 =" "
            pass

        try:
            cough_qn2=request.POST['local_clm7[1]']
            print("Your are cough_qn2", cough_qn2)
        except:
            cough_qn2 =" "
            pass

        try:
            cough_qn3=request.POST['local_clm7[2]']
            print("Your are cough_qn3", cough_qn3)
        except:
            cough_qn3 =" "
            pass

        try:
            cough_qn4=request.POST['local_clm7[3]']
            print("Your are cough_qn4", cough_qn4)
        except:
            cough_qn4 =" "
            pass

        try:
            cough_qn5=request.POST['local_clm7[4]']
            print("Your are cough_qn5", cough_qn5)
        except:
            cough_qn5 =" "
            pass

        try:
            cough_qn6=request.POST['local_clm7[5]']
            print("Your are cough_qn6", cough_qn6)
        except:
            cough_qn6 =" "
            pass

        try:
            cough_qn7=request.POST['local_clm7[6]']
            print("Your are cough_qn7", cough_qn7)
        except:
            cough_qn7 =" "
            pass

        try:
            cough_qn8=request.POST['local_clm7[7]']
            print("Your are cough_qn8", cough_qn8)
        except:
            cough_qn8 =" "
            pass

        try:
            cough_qn9=request.POST['local_clm7[8]']
            print("Your are cough_qn9", cough_qn9)
        except:
            cough_qn9 =" "
            pass

        try:
            cough_qn10=request.POST['local_clm7[9]']
            print("Your are cough_qn10", cough_qn10)
        except:
            cough_qn10 =" "
            pass


        try:
            chest_qn1=request.POST['local_clm8[0]']
            print("Your are chest_qn1", chest_qn1)
        except:
            chest_qn1 =" "
            pass

        try:
            chest_qn2=request.POST['local_clm8[1]']
            print("Your are chest_qn2", chest_qn2)
        except:
            chest_qn2 =" "
            pass

        try:
            chest_qn3=request.POST['local_clm8[2]']
            print("Your are chest_qn3", chest_qn3)
        except:
            chest_qn3 =" "
            pass

        try:
            chest_qn4=request.POST['local_clm8[3]']
            print("Your are chest_qn4", chest_qn4)
        except:
            chest_qn4 =" "
            pass

        try:
            chest_qn5=request.POST['local_clm8[4]']
            print("Your are chest_qn5", chest_qn5)
        except:
            chest_qn5 =" "
            pass

        try:
            chest_qn6=request.POST['local_clm8[5]']
            print("Your are chest_qn4", chest_qn6)
        except:
            chest_qn6 =" "
            pass

        try:
            fever_qn1=request.POST['local_clm9[0]']
            print("Your are fever_qn1", fever_qn1)
        except:
            fever_qn1 =" "
            pass

        try:
            fever_qn2=request.POST['local_clm9[1]']
            print("Your are fever_qn2", fever_qn2)
        except:
            fever_qn2 =" "
            pass

        try:
            fever_qn3=request.POST['local_clm9[2]']
            print("Your are fever_qn3", fever_qn3)
        except:
            fever_qn3 =" "
            pass

        try:
            fever_qn4=request.POST['local_clm9[3]']
            print("Your are fever_qn4", fever_qn4)
        except:
            fever_qn4 =" "
            pass

        try:
            fever_qn5=request.POST['local_clm9[4]']
            print("Your are fever_qn5", fever_qn5)
        except:
            fever_qn5 =" "
            pass

        try:
            fever_qn6=request.POST['local_clm9[5]']
            print("Your are fever_qn6", fever_qn6)
        except:
            fever_qn6 =" "
            pass

        try:
            fever_qn7=request.POST['local_clm9[6]']
            print("Your are fever_qn7", fever_qn7)
        except:
            fever_qn7 =" "
            pass

        try:
            fever_qn8=request.POST['local_clm9[7]']
            print("Your are fever_qn8", fever_qn8)
        except:
            fever_qn8 =" "
            pass


        try:
            abd_qn1=request.POST['local_clm10[0]']
            print("Your are abd_qn1", abd_qn1)
        except:
            abd_qn1 =" "
            pass

        try:
            abd_qn2=request.POST['local_clm10[1]']
            print("Your are abd_qn2", abd_qn2)
        except:
            abd_qn2 =" "
            pass

        try:
            abd_qn3=request.POST['local_clm10[2]']
            print("Your are abd_qn3", abd_qn3)
        except:
            abd_qn3 =" "
            pass

        try:
            abd_qn4=request.POST['local_clm10[3]']
            print("Your are abd_qn4", abd_qn4)
        except:
            abd_qn4 =" "
            pass

        try:
            abd_qn5=request.POST['local_clm10[4]']
            print("Your are abd_qn5", abd_qn5)
        except:
            abd_qn5 =" "
            pass

        try:
            abd_qn6=request.POST['local_clm10[5]']
            print("Your are abd_qn6", abd_qn6)
        except:
            abd_qn6 =" "
            pass

        try:
            abd_qn7=request.POST['local_clm10[6]']
            print("Your are abd_qn7", abd_qn7)
        except:
            abd_qn7 =" "
            pass

        try:
            abd_qn8=request.POST['local_clm10[7]']
            print("Your are abd_qn8", abd_qn8)
        except:
            abd_qn8 =" "
            pass

        try:
            abd_qn9=request.POST['local_clm10[8]']
            print("Your are abd_qn9", abd_qn9)
        except:
            abd_qn9 =" "
            pass

        try:
            abd_qn10=request.POST['local_clm10[9]']
            print("Your are abd_qn10", abd_qn10)
        except:
            abd_qn10 =" "
            pass

        try:
            abd_qn11=request.POST['local_clm10[10]']
            print("Your are abd_qn11", abd_qn11)
        except:
            abd_qn11 =" "
            pass

        try:
            Lm_qn1=request.POST['local_clm11[0]']
            print("Your are Lm_qn1", Lm_qn1)
        except:
            Lm_qn1 =" "
            pass

        try:
            Lm_qn2=request.POST['local_clm11[1]']
            print("Your are Lm_qn2", Lm_qn2)
        except:
            Lm_qn2 =" "
            pass

        try:
            Lm_qn3=request.POST['local_clm11[2]']
            print("Your are Lm_qn3", Lm_qn3)
        except:
            Lm_qn3 =" "
            pass

        try:
            Lm_qn4=request.POST['local_clm11[3]']
            print("Your are Lm_qn4", Lm_qn4)
        except:
            Lm_qn4 =" "
            pass

        try:
            Lm_qn5=request.POST['local_clm11[4]']
            print("Your are Lm_qn5", Lm_qn5)
        except:
            Lm_qn5 =" "
            pass

        try:
            Lm_qn6=request.POST['local_clm11[5]']
            print("Your are Lm_qn6", Lm_qn6)
        except:
            Lm_qn6 =" "
            pass

        try:
            Lm_qn7=request.POST['local_clm11[6]']
            print("Your are Lm_qn7", Lm_qn7)
        except:
            Lm_qn7 =" "
            pass

        try:
            Lm_qn8=request.POST['local_clm11[7]']
            print("Your are Lm_qn8", Lm_qn8)
        except:
            Lm_qn8 =" "
            pass

        try:
            Lm_qn9=request.POST['local_clm11[8]']
            print("Your are Lm_qn9", Lm_qn9)
        except:
            Lm_qn9 =" "
            pass

        try:
            Lm_qn10=request.POST['local_clm11[9]']
            print("Your are Lm_qn10", Lm_qn10)
        except:
            Lm_qn10 =" "
            pass

        try:
            I_cough_qn1=request.POST['local_clm12[0]']
            print("Your are I_cough_qn1", I_cough_qn1)
        except:
            I_cough_qn1 =" "
            pass

        try:
            I_cough_qn2=request.POST['local_clm12[1]']
            print("Your are I_cough_qn2", I_cough_qn2)
        except:
            I_cough_qn2 =" "
            pass

        try:
            I_cough_qn3=request.POST['local_clm12[2]']
            print("Your are I_cough_qn3", I_cough_qn3)
        except:
            I_cough_qn3 =" "
            pass

        try:
            I_cough_qn4=request.POST['local_clm12[3]']
            print("Your are I_cough_qn4", I_cough_qn4)
        except:
            I_cough_qn4 =" "
            pass

        try:
            I_cough_qn5=request.POST['local_clm12[4]']
            print("Your are I_cough_qn5", I_cough_qn5)
        except:
            I_cough_qn5 =" "
            pass


        try:
            I_fever_qn1=request.POST['local_clm13[0]']
            print("Your are I_fever_qn1", I_fever_qn1)
        except:
            I_fever_qn1 =" "
            pass

        try:
            I_fever_qn2=request.POST['local_clm13[1]']
            print("Your are I_fever_qn2", I_fever_qn2)
        except:
            I_fever_qn2 =" "
            pass

        try:
            I_fever_qn3=request.POST['local_clm13[2]']
            print("Your are I_fever_qn3", I_fever_qn3)
        except:
            I_fever_qn3 =" "
            pass

        try:
            I_fever_qn4=request.POST['local_clm13[3]']
            print("Your are I_fever_qn4", I_fever_qn4)
        except:
            I_fever_qn4 =" "
            pass

        try:
            I_fever_qn5=request.POST['local_clm13[4]']
            print("Your are I_fever_qn5", I_fever_qn5)
        except:
            I_fever_qn5 =" "
            pass

        try:
            I_fever_qn6=request.POST['local_clm13[5]']
            print("Your are I_fever_qn6", I_fever_qn6)
        except:
            I_fever_qn6 =" "
            pass

        try:
            I_fever_qn7=request.POST['local_clm13[6]']
            print("Your are I_fever_qn7", I_fever_qn7)
        except:
            I_fever_qn7 =" "
            pass

        try:
            I_fever_qn8=request.POST['local_clm13[7]']
            print("Your are I_fever_qn8", I_fever_qn8)
        except:
            I_fever_qn8 =" "
            pass

        try:
            I_chest_qn1=request.POST['local_clm14[0]']
            print("Your are I_chest_qn1", I_chest_qn1)
        except:
            I_chest_qn1 =" "
            pass


        try:
            I_abd_qn1=request.POST['local_clm15[0]']
            print("Your are I_abd_qn1", I_abd_qn1)
        except:
            I_abd_qn1 =" "
            pass

        try:
            I_abd_qn2=request.POST['local_clm15[1]']
            print("Your are I_abd_qn2", I_abd_qn2)
        except:
            I_abd_qn2 =" "
            pass

        try:
            I_abd_qn3=request.POST['local_clm15[2]']
            print("Your are I_abd_qn3", I_abd_qn3)
        except:
            I_abd_qn3 =" "
            pass

        try:
            I_abd_qn4=request.POST['local_clm15[3]']
            print("Your are I_abd_qn4", I_abd_qn4)
        except:
            I_abd_qn4 =" "
            pass

        try:
            I_abd_qn5=request.POST['local_clm15[4]']
            print("Your are I_abd_qn5", I_abd_qn5)
        except:
            I_abd_qn5 =" "
            pass

        try:
            I_abd_qn6=request.POST['local_clm15[5]']
            print("Your are I_abd_qn6", I_abd_qn6)
        except:
            I_abd_qn6 =" "
            pass


        ####################Low mood#################################

        if Lm_qn1=="Several days":
            Low_Mood +=1
            print("Low_Mood score in first condition is ", Low_Mood)
        if Lm_qn1=="More than the half days":
            Low_Mood+=2
            # print("Anxiety score in first condition is ", Anxiety)
        if Lm_qn1=="Nearly every day":
            Low_Mood+=3
            # print("Anxiety score in first condition is ", Anxiety)

        if Lm_qn2=="Several days":
            Low_Mood+=1
            print("Low_Mood score in second condition is ", Low_Mood)
        if Lm_qn2=="More than the half days":
            Low_Mood+=2
            # print("Anxiety score in second condition is ", Anxiety)
        if Lm_qn2=="Nearly every day":
            Low_Mood+=3
            # print("Anxiety score in second condition is ", Anxiety)

        if Lm_qn3=="Several days":
            Low_Mood+=1
            print("Low_Mood score in third condition is ", Low_Mood)
        if Lm_qn3=="More than the half days":
            Low_Mood+=2
            # print("Anxiety score in third condition is ", Anxiety)
        if Lm_qn3=="Nearly every day":
            Low_Mood+=3
            # print("Anxiety score in third condition is ", Anxiety)

        if Lm_qn4=="Several days":
            Low_Mood+=1
            print("Low_Mood score in fourth condition is ", Low_Mood)
        if Lm_qn4=="More than the half days":
            Low_Mood+=2
            print("Low_Mood score in fourth condition is ", Low_Mood)
        if Lm_qn4=="Nearly every day":
            Low_Mood+=3
            # print("Anxiety score in fourth condition is ", Anxiety)

        if Lm_qn5=="Several days":
            Low_Mood+=1
            # print("Anxiety score in fifth condition is ", Anxiety)
        if Lm_qn5=="More than the half days":
            Low_Mood+=2
            print("Low_Mood score in fifth condition is ", Low_Mood)
        if Lm_qn5=="Nearly every day":
            Low_Mood+=3
            # print("Anxiety score in fifth condition is ", Anxiety)

        if Lm_qn6=="Several days":
            Low_Mood+=1
            print("Low_Mood score in six condition is ", Low_Mood)
        if Lm_qn6=="More than the half days":
            Low_Mood+=2
            print("Low_Mood score in six condition is ", Low_Mood)
        if Lm_qn6=="Nearly every day":
            Low_Mood+=3
            # print("Anxiety score in six condition is ", Anxiety)

        if Lm_qn7=="Several days":
            Low_Mood+=1
            print("Low_Mood score in seven condition is ", Low_Mood)
        if Lm_qn7=="More than the half days":
            Low_Mood+=2
            print("Low_Mood score in seven condition is ", Low_Mood)
        if Lm_qn7=="Nearly every day":
            Low_Mood+=3
            # print("Anxiety score in seven condition is ", Anxiety)

        if Lm_qn8=="Several days":
            Low_Mood+=1
            # print("Anxiety score in seven condition is ", Anxiety)
        if Lm_qn8=="More than the half days":
            Low_Mood+=2
            print("Low_Mood score in seven condition is ", Low_Mood)
        if Lm_qn8=="Nearly every day":
            Low_Mood+=3
            # print("Anxiety score in seven condition is ", Anxiety)

        if Lm_qn9=="Several days":
            Low_Mood+=1
            # print("Anxiety score in seven condition is ", Anxiety)
        if Lm_qn9=="More than the half days":
            Low_Mood+=2
            print("Low_Mood score in seven condition is ", Low_Mood)
        if Lm_qn9=="Nearly every day":
            Low_Mood+=3
            # print("Anxiety score in seven condition is ", Anxiety)

        if Lm_qn10=="Several days":
            Low_Mood+=1
            # print("Anxiety score in seven condition is ", Anxiety)
        if Lm_qn10=="More than the half days":
            Low_Mood+=2
            # print("Anxiety score in seven condition is ", Anxiety)
        if Lm_qn10=="Nearly every day":
            Low_Mood+=3
            # print("Anxiety score in seven condition is ", Anxiety)



        if age > 40 :
            Cholecystitis+=1.25
            Cardiac_Ischemia+=1.11
            Irritable_Bowel_Disease += 3.33
            Pancreatitis += 1.43
            Chronic_Lung_Disease += 1.43
            Lung_Cancer += 1.67
            print("Cholecystitis score in first condition is ", Cholecystitis)
            print("Cardiac_Ischemia score in first condition is ", Cardiac_Ischemia)

        if age < 40 and age > 0 :
            Pulmonary_Embolism +=1.25
            Inflammatory_Bowel_Disease += 1.25

        if age > 50 :
            Diverticulitis+=1.25
            Chronic_Heart_Failure += 1
            Urinary_Tract_Infection += 1.43
        
        if age > 75 :
            Osteomyelitis += 2

        if age < 50 and age > 0 :
            Asthma+=2

    
    ####### Endometriosis condition ###########

        if gender == 'Female' and abd_qn2== 'Yes' and abd_qn11== 'Yes' :
            Endometriosis = 8
            if age > 20 : 
                Endometriosis += 0
            if an6== 'Few days' or an6== 'Few weeks' : 
                Endometriosis += 0

        else: 
            if age > 20 :
                Endometriosis += 2 
            if gender == 'Female':
                Endometriosis += 2
            if an6== 'Few days' or an6== 'Few weeks' : 
                Endometriosis += 2
            if abd_qn2== 'Yes': 
                Endometriosis += 2
            if abd_qn11== 'Yes': 
                Endometriosis += 2

     
        
        if gender == 'Female':
            Cholecystitis+=1.25
            Cystitis+=2
            
            print("Cholecystitis score in second condition is ", Cholecystitis)
        
        if gender == 'Male':
            Renal_Calculi+=2.5
            Cardiac_Ischemia+=1.11
            Pancreatitis += 1.43
            print("Renal_Calculi score in first condition is ", Renal_Calculi)
            print("Cardiac_Ischemia score in second condition is ", Cardiac_Ischemia)

        if BMI > 25 :
            Cellulitis += 2

        if BMI > 30 :
            Cholecystitis+=1.25
            Gastritis+=1.25
            Diverticulitis+=1.25
            Cardiac_Ischemia+=1.11
            Pulmonary_Embolism +=1.25
            print("Cholecystitis score in third condition is ", Cholecystitis)
            print("Gastritis score in first condition is ", Gastritis)
            print("Cardiac_Ischemia score in third condition is ", Cardiac_Ischemia)

        if BMI < 20 :
            Inflammatory_Bowel_Disease += 1.25

        if daibetes== 'Yes':
            Cholecystitis+=1.25
            Gastritis+=1.25
            Cystitis+=2
            Pyelonephritis+=2.5
            Renal_Calculi+=2.5
            Diverticulitis+=1.25
            Pancreatitis += 1.43
            Chronic_Heart_Failure += 1
            Cellulitis += 2
            Urinary_Tract_Infection += 1.43
            Osteomyelitis += 2
            print("Cholecystitis score in fourth condition is ", Cholecystitis)
            print("Gastritis score in second condition is ", Gastritis)
            print("Renal_Calculi score in second condition is ", Renal_Calculi)
         

        if Hypertension== 'Yes':
            Chronic_Heart_Failure += 1

        if Heart_disease== 'Yes':
            Chronic_Heart_Failure += 1




        if daibetes== 'Yes' or  Hypertension == 'Yes' or Heart_disease == 'Yes' or Strokes == 'Yes' or all_above == 'Yes'  :
            Cardiac_Ischemia+=1.11
            print("Cardiac_Ischemia score in fourth condition is ", Cardiac_Ischemia)

        if alcohol== 'Yes':
            Cholecystitis+=1.25
            Gastritis+=1.25
            Pulmonary_Embolism +=1.25
            Pancreatitis += 1.43
            print("Cholecystitis score in fifth condition is ", Cholecystitis)
            print("Gastritis score in third condition is ", Gastritis)

        if smoke== 'Yes':
            Pneumonia+=1.11
            Gastritis +=1.25
            Cardiac_Ischemia+=1.11
            Viral_Bronchitis+=1.67
            Pleurisy +=3.33
            Costochondritis +=3.33
            Chronic_Heart_Failure += 1
            Chronic_Lung_Disease += 1.43
            Lung_Cancer += 1.67
            COVID += 1.43
            Viral_Fever += 1.67
            Cellulitis += 2
            print("Gastritis score in fourth condition is ", Gastritis)
            print("Cardiac_Ischemia score in fifth condition is ", Cardiac_Ischemia)

        if an6== 'Few days' or an6== 'Few weeks' :
            Pneumonia+=1.11
            Cholecystitis+=1.25
            Cystitis+=2
            Cardiac_Ischemia+=1.11
            Pulmonary_Embolism +=1.25
            
            COVID += 1.43
            Urinary_Tract_Infection += 1.43
            print("Cholecystitis score in six condition is ", Cholecystitis)
            print("Cardiac_Ischemia score in six condition is ", Cardiac_Ischemia)

        if an6== 'Few days': 
            Pyelonephritis+=2.5
            Renal_Calculi+=2.5
            Viral_Bronchitis+=1.67
            Appendicitis += 2.5
            Viral_Fever += 1.67
            Meningitis += 3.33
            print("Renal_Calculi score in third condition is ", Renal_Calculi)

        if an6== 'Few weeks': 
            Cellulitis += 2

        if an6== 'Few weeks' or an6== 'Few Months' or an6== 'Many months' :
            Gastritis+=1.25
            Asthma+=2
            print("Gastritis score in fifth condition is ", Gastritis)

        if an6== 'Few weeks' or an6== 'Few Months' :
            Inflammatory_Bowel_Disease += 1.25
            Pancreatitis += 1.43
            Osteomyelitis += 2
            

        if an6== 'Few Months' or an6== 'Many months' :
            Diverticulitis+=1.25
            Chronic_Heart_Failure += 1
            Chronic_Lung_Disease += 1.43

        if cough_qn1== 'Yes':
           Viral_Bronchitis+=1.67
           Pleurisy +=3.33
           Costochondritis +=3.33
           COVID += 1.43
           Viral_Fever += 1.67

        if I_cough_qn1== 'Yes':
           Viral_Bronchitis+=1.67
           Pleurisy +=3.33
           Costochondritis +=3.33
           COVID += 1.43
           Viral_Fever += 1.67
            
        if cough_qn2== 'Yes':
            Pneumonia+=1.11
            Pulmonary_Embolism +=1.25
            Viral_Bronchitis+= 1.67
            COVID += 1.43
            Viral_Fever += 1.67

        if I_cough_qn2== 'Yes':
            Pneumonia+=1.11
            Pulmonary_Embolism +=1.25
            Viral_Bronchitis+= 1.67
            COVID += 1.43
            Viral_Fever += 1.67

        if cough_qn3== 'Yes':
            COVID += 1.43

        if cough_qn4== 'Yes':
            Pneumonia+=1.11
            Viral_Bronchitis+=1.67
            COVID += 1.43

        if I_cough_qn3== 'Yes':
            Pneumonia+=1.11
            Viral_Bronchitis+=1.67
            COVID += 1.43

        if cough_qn5== 'Yes':
            Pneumonia+=1.11
            Chronic_Lung_Disease += 1.43
            Lung_Cancer += 1.67
            Viral_Fever += 1.67

        if I_cough_qn4== 'Yes':
            Pneumonia+=1.11
            Chronic_Lung_Disease += 1.43
            Lung_Cancer += 1.67
            Viral_Fever += 1.67

        if cough_qn6== 'Yes':
            Pneumonia+=1.11
            Pulmonary_Embolism +=1.25
            Chronic_Heart_Failure += 1
            Chronic_Lung_Disease += 1.43
            Lung_Cancer += 1.67


        if cough_qn7== 'Yes':
            Pulmonary_Embolism +=1.25
            Asthma+=2
            Chronic_Heart_Failure += 1
            Chronic_Lung_Disease += 1.43

        if cough_qn8== 'Yes':
            Pneumonia+=1.11
            Cardiac_Ischemia+=1.11
            Asthma+=2
            Chronic_Heart_Failure += 1
            Chronic_Lung_Disease += 1.43
            Lung_Cancer += 1.67
            COVID += 1.43
            print("Cardiac_Ischemia score in seven condition is ", Cardiac_Ischemia)

        if cough_qn9== 'Yes':
            Chronic_Heart_Failure += 1

        if I_cough_qn5== 'Yes':
            Chronic_Heart_Failure += 1

        if chest_qn1== 'Yes':
            Pneumonia+=1.11
            Pulmonary_Embolism +=1.25
            Pleurisy +=3.33
            Costochondritis +=3.33
            

        if chest_qn2== 'Yes':
            Cardiac_Ischemia+=1.11
            print("Cardiac_Ischemia score in eight condition is ", Cardiac_Ischemia)

        if I_chest_qn1== 'Yes':
            Cardiac_Ischemia+=1.11
            print("Cardiac_Ischemia score in eight condition is ", Cardiac_Ischemia)

        if chest_qn3== 'Yes':
            Cardiac_Ischemia+=1.11
            print("Cardiac_Ischemia score in nine condition is ", Cardiac_Ischemia)

        if chest_qn4== 'Yes':
            Asthma+=2

        if chest_qn5== 'Yes':
            Chronic_Heart_Failure += 1.11

        if chest_qn6== 'Yes':
            Chronic_Lung_Disease += 1.43

        if fever_qn2== 'Yes':          ##(no increament for fever qn1 and I fever qn1)
            Diverticulitis+=1.25
            Appendicitis += 2.5 
            Inflammatory_Bowel_Disease += 1.25

        if I_fever_qn2== 'Yes':
            Diverticulitis+=1.25
            Appendicitis += 2.5 
            Inflammatory_Bowel_Disease += 1.25

        if fever_qn3== 'Yes':
            Osteomyelitis += 2

        if I_fever_qn6== 'Yes':
            Osteomyelitis += 2
        
        if fever_qn4== 'Yes':
            Cellulitis += 2
            Osteomyelitis += 2

        if I_fever_qn7== 'Yes':
            Cellulitis += 2
            Osteomyelitis += 2

        if fever_qn5== 'Yes':
            Cystitis+=2
            Pyelonephritis+=2.5
            Renal_Calculi+=2.5
            Urinary_Tract_Infection += 1.43

        if I_fever_qn3== 'Yes':
            Cystitis+=2
            Pyelonephritis+=2.5
            Renal_Calculi+=2.5
            Urinary_Tract_Infection += 1.43

        if fever_qn6== 'Yes':
            Viral_Bronchitis+=1.67
            Meningitis += 3.33
            Viral_Fever += 1.67

        if I_fever_qn4== 'Yes':
            Viral_Bronchitis+=1.67
            Meningitis += 3.33
            Viral_Fever += 1.67

        if fever_qn7== 'Yes':
            Meningitis += 3.33

        if I_fever_qn5== 'Yes':
            Meningitis += 3.33

        if fever_qn8== 'Yes':
            Pneumonia+=1.11

        if I_fever_qn8== 'Yes':
            Pneumonia+=1.11

        
        if abd_qn1 == 'Yes': 
            Cholecystitis+=1.25
            Gastritis+=1.25
            Pancreatitis += 1.43
            print("Cholecystitis score in seven condition is ", Cholecystitis)
            print("Gastritis score in six condition is ", Gastritis)

        if I_abd_qn1 == 'Yes':
            Cholecystitis+=1.25
            Gastritis+=1.25
            Pancreatitis += 1.43
            print("Cholecystitis score in seven condition is ", Cholecystitis)
            print("Gastritis score in six condition is ", Gastritis)


        if abd_qn2 == 'Yes':
            Cystitis+=2
            Pyelonephritis+=2.5
            Diverticulitis+=1.25
            Appendicitis += 2.5 
            Inflammatory_Bowel_Disease += 1.25
            Irritable_Bowel_Disease += 3.33
        
            Urinary_Tract_Infection += 1.43
           
        if I_abd_qn2 == 'Yes':
            Cystitis+=2
            Pyelonephritis+=2.5
            Diverticulitis+=1.25
            Appendicitis += 2.5 
            Inflammatory_Bowel_Disease += 1.25
            Irritable_Bowel_Disease += 3.33
            
            Urinary_Tract_Infection += 1.43

        if abd_qn1 == 'Yes': 
            if abd_qn3 == 'Yes':
                Cholecystitis += 1.25

        if abd_qn2 == 'Yes': 
            if abd_qn3 == 'Yes':
                Appendicitis += 2.5


        if I_abd_qn1 == 'Yes': 
            if I_abd_qn3 == 'Yes':
                Cholecystitis += 1.25

        if I_abd_qn2 == 'Yes': 
            if I_abd_qn3 == 'Yes':
                Appendicitis += 2.5

        
            ##( Scoring system is not updated for abd qn4 and I abd qn4)
           

        if abd_qn5 == 'Yes':
            Cholecystitis+=1.25
            Diverticulitis+=1.25
            Appendicitis += 2.5
            Inflammatory_Bowel_Disease += 1.25
            Urinary_Tract_Infection += 1.43
           
            print("Cholecystitis score in eight condition is ", Cholecystitis)

        if I_abd_qn5 == 'Yes':
            Cholecystitis+=1.25
            Diverticulitis+=1.25
            Appendicitis += 2.5
            Inflammatory_Bowel_Disease += 1.25
            Urinary_Tract_Infection += 1.43
           
         

        if abd_qn6 == 'Yes':
            Gastritis+=1.25
            print("Gastritis score in seven condition is ", Gastritis)

        
        if abd_qn7 == 'Yes':
            Urinary_Tract_Infection += 1.43

        if I_abd_qn6 == 'Yes':
            Urinary_Tract_Infection += 1.43

        if abd_qn8 == 'Yes':
            Diverticulitis+=1.25
            Inflammatory_Bowel_Disease += 1.25
             
             ##

        if abd_qn9 == 'Yes':
            Gastritis+=1.25
            Irritable_Bowel_Disease += 3.33
            print("Gastritis score in eight condition is ", Gastritis)

        if abd_qn10 == 'Yes':
            Inflammatory_Bowel_Disease += 1.25
            Pancreatitis += 1.43
            Lung_Cancer += 1.67

      


        print("Total score for pneumonia is", Pneumonia)

        context2 ={

                        "Appendicitis": Appendicitis,            
                        "Cholecystitis" : Cholecystitis,
                        "Gastritis" : Gastritis,
                        "Cystitis" : Cystitis,
                        "Pyelonephritis" : Pyelonephritis,
                        "Renal_Calculi" :  Renal_Calculi,
                        "Diverticulitis" : Diverticulitis,
                        "Intestinal Obstruction" : Intestinal_Obstruction,
                        "Inflammatory Bowel Disease" : Inflammatory_Bowel_Disease,
                        "Irritable Bowel Disease" : Irritable_Bowel_Disease,
                        "Pancreatitis" : Pancreatitis, 
                        "Endometriosis" :  Endometriosis,
                       
                        "Cardiac Ischemia":Cardiac_Ischemia,
                        "Pulmonary Embolism":Pulmonary_Embolism,
                        "Pleurisy":Pleurisy,
                        "Costochondritis":Costochondritis,
                        "Pneumonia":Pneumonia,
                        "Viral Bronchitis":Viral_Bronchitis,
                        "Asthma":Asthma,
                        "Chronic Heart Failure":Chronic_Heart_Failure,
                        "Chronic Lung Disease" :Chronic_Lung_Disease,
                        "Lung Cancer":Lung_Cancer,
                        "COVID_":COVID,
                        "Diabetes" : Diabetes,
                        "Viral Fever":Viral_Fever,
                        "Cholangitis" : Cholangitis,
                        "Endocarditis" : Endocarditis,
                        "Cellulitis" : Cellulitis,
                        "Urinary Tract Infection" : Urinary_Tract_Infection,
                        "Osteomyelitis" : Osteomyelitis,
                        "Meningitis": Meningitis
                               
                            }

    

        print("Context2" , context2 )

    

        Personal_Information1 =  ClientID.objects.create(Age=age, Email=email, created_Date= datetime.datetime.now() )
        Personal_Information1.save()
        Personal_Information2 =  RiskID.objects.create(Unique_ID=Personal_Information1, Height=height, Weight=weight, BMI=BMI ,Sex=gender, Diabetes=daibetes , Hypertension= Hypertension , Heart_disease= Heart_disease , Strokes= Strokes , History_of_4= all_above , Smoke=smoke , Alcohol= alcohol,Exercise= exercise , Calories_count= calories , Age_90_years= life , Covid_history = covid)
        Personal_Information2.save()

        # sorted_context2 = sorted(context2.items(), key=operator.itemgetter(1))
        # sorted_context2 = dict( sorted(context2.items(), key=operator.itemgetter(1),reverse=True))
        # print("sorted_context2" , sorted_context2)
        x = sorted(((v,k) for k,v in context2.items() ))
        print ("len of x",len(x))

    
        first_name = x[-1][1]
        first_value = x[-1][0]
        second_name = x[-2][1]
        second_value = x[-2][0]
        third_name = x[-3][1]
        third_value = x[-3][0]
        fourth_name = x[-4][1]
        fourth_value = x[-4][0]
        

        print("first_value",first_value)
        print("second_value",second_value)
        print("third_value",third_value)
        print("fourth_value",fourth_value)
        context3 = {
            first_name: first_value,
            second_name :second_value,
            third_name :third_value,
            fourth_name : fourth_value,

        }

        print("Context3" , context3 )
        
        
        

        if Low_Mood<6:
            Low_Mood_risk= "Your overall risk assessment for Low mood is Normal"
            #  print("Your overall risk assessment for Depression is Normal")
            #  return render(request,"CombinedModule_result_display.html",{'context':context2 , 'Risk_Assessment1' : "Your overall risk assessment for Depression is Normal" })

        if Low_Mood>=7 and Low_Mood<=11:
            Low_Mood_risk= "Your overall risk assessment for Low mood is Mild"
            # print("Your overall risk assessment for Depression is Mild")
            # return render(request,"CombinedModule_result_display.html",{'context':context2 , 'Risk_Assessment1' : "Your overall risk assessment for Depression is Mild" })

        if Low_Mood>=12 and Low_Mood<=16:
            Low_Mood_risk= "Your overall risk assessment for Low mood is Moderate"
            # print("Your overall risk assessment for Depression is Moderate")
            # return render(request,"CombinedModule_result_display.html",{'context':context2 , 'Risk_Assessment1' : "Your overall risk assessment for Depression is Moderate" })

        if Low_Mood>=17 and Low_Mood<=21:
            Low_Mood_risk= "Your overall risk assessment for Low mood is Moderately severe"
            # print("Your overall risk assessment for Depression is Moderately severe")
            # return render(request,"CombinedModule_result_display.html",{'context':context2 , 'Risk_Assessment1' : "Your overall risk assessment for Depression is Moderately severe" })

        if Low_Mood>=22 and Low_Mood<=30:
            Low_Mood_risk= "Your overall risk assessment for Low mood is severe"
            # print("Your overall risk assessment for Depression is severe")
            # return render(request,"CombinedModule_result_display.html",{'context':context2 , 'Risk_Assessment1' : "Your overall risk assessment for Depression is severe" })
        if Low_Mood>0:
            Low_Mood_risk= {
                "Low_Mood_module" : Low_Mood_risk, 
        
            }

        return render(request,"combined_low_mood_result_display.html",{'context':context3 , 'Risk_Assessment' : Low_Mood_risk })
        
    return render(request,"combined_low_mood.html")


   

@csrf_exempt
def combined_module(request):
    if request.method == 'GET':
        return render(request,"combined module.html" )

    if request.method == 'POST':
        print('POST data is', request.POST)
        print('post BODY', request.body)
        
        Appendicitis=0
        Cholecystitis=0
        Gastritis=0
        Cystitis=0
        Pyelonephritis=0
        Renal_Calculi=0
        Diverticulitis=0
        Intestinal_Obstruction=0
        Inflammatory_Bowel_Disease=0
        Irritable_Bowel_Disease=0
        Pancreatitis=0
        Endometriosis=0
        Anxiety=0
        Depression=0
        Cardiac_Ischemia=0
        Pulmonary_Embolism=0
        Pleurisy=0
        Costochondritis=0
        Pneumonia=0
        Viral_Bronchitis=0
        Asthma=0
        Chronic_Heart_Failure=0
        Chronic_Lung_Disease=0
        Lung_Cancer=0
        COVID=0
        Diabetes=0
        Viral_Fever=0
        Cholangitis=0
        Endocarditis=0
        Cellulitis=0
        Urinary_Tract_Infection=0
        Osteomyelitis=0
        Meningitis=0

        context1 ={

                        "Appendicitis": Appendicitis,            
                        "Cholecystitis" : Cholecystitis,
                        "Gastritis" : Gastritis,
                        "Cystitis" : Cystitis,
                        "Pyelonephritis" : Pyelonephritis,
                        "Renal_Calculi" :  Renal_Calculi,
                        "Diverticulitis" : Diverticulitis,
                        "Intestinal Obstruction" : Intestinal_Obstruction,
                        "Inflammatory Bowel Disease" : Inflammatory_Bowel_Disease,
                        "Irritable Bowel Disease" : Irritable_Bowel_Disease,
                        "Pancreatitis" : Pancreatitis, 
                        "Endometriosis" :  Endometriosis,
                        
                        "Cardiac Ischemia":Cardiac_Ischemia,
                        "Pulmonary Embolism":Pulmonary_Embolism,
                        "Pleurisy":Pleurisy,
                        "Costochondritis":Costochondritis,
                        "Pneumonia":Pneumonia,
                        "Viral Bronchitis":Viral_Bronchitis,
                        "Asthma":Asthma,
                        "Chronic Heart Failure":Chronic_Heart_Failure,
                        "Chronic Lung Disease" :Chronic_Lung_Disease,
                        "Lung Cancer":Lung_Cancer,
                        "COVID_":COVID,
                        "Diabetes" : Diabetes,
                        "Viral Fever":Viral_Fever,
                        "Cholangitis" : Cholangitis,
                        "Endocarditis" : Endocarditis,
                        "Cellulitis" : Cellulitis,
                        "Urinary Tract Infection" : Urinary_Tract_Infection,
                        "Osteomyelitis" : Osteomyelitis,
                        "Meningitis": Meningitis
                               
                            }

        print("context1",context1 )

        anx_depr= {
            "Anxiety":Anxiety,
            "Depression":Depression,
        }

        updated_data= dict(request.POST.lists())

        try:
            an1=request.POST['all1']
            print("Your an1 is", an1)
        except:
            an1 =" "
            pass

        try:
            diagnosis=updated_data['all2[0]']
            print("Your diagnosis is", diagnosis)
            print("Your cough diagnosis is", diagnosis[0])
            print("Your chest pain diagnosis is", diagnosis[1])
        except:
            diagnosis =" "
            pass

       
        try:
            age = int (request.POST['comb_data[field_1]'])
            print("Your are age", age)
        except:
            age = 0
            pass

        try:
            gender=request.POST['comb_data[field_2]']
            print("Your are gender", gender)
        except:
            gender =" "
            pass

        try:
            weight=request.POST['comb_data[field_3]']
            print("Your are weight", weight)
        except Exception as e:
            print("Error is", e)
            
            weight =" "
            pass

        try:
            height=request.POST['comb_data[field_4]']
            print("Your are height", height)
        except Exception as e:
            print("Error is", e)

            height =" "
            pass

        # weight= request.POST['comb_data[field_3]'] 
        # print("Your weight is ", weight )
        # height= request.POST['comb_data[field_4]']
        height_in_meter = round((int(height)/100),2)
        # print ("height_in_meter",height_in_meter)
        BMI = round((int(weight) / (height_in_meter * height_in_meter)),2)
        print("Your calculated BMI is", BMI)


        try:
            email=request.POST['comb_data[field_5]']
            print("Your are email", email)
        except:
            email =" "
            pass

        try:
            daibetes=request.POST['all4[0]']
            print("Your are daibetes", daibetes)

        except:
            daibetes =" "
            pass

        try:
            Hypertension=request.POST['all4[1]']
            print("Your are Hypertension", Hypertension)

        except:
            Hypertension =" "
            pass

        try:
            Heart_disease=request.POST['all4[2]']
            print("Your are Heart_disease", Heart_disease)

        except:
            Heart_disease =" "
            pass

        try:
            Strokes=request.POST['all4[3]']
            print("Your are Strokes", Strokes)

        except:
            Strokes =" "
            pass

        try:
            all_above=request.POST['all4[4]']
            print("Your are all_above", all_above)

        except:
            all_above =" "
            pass

        try:
            smoke=request.POST['all5[0]']
            print("Your are smoke", smoke)

        except:
            smoke =" "
            pass

        try:
            alcohol=request.POST['all5[1]']
            print("Your are alcohol", alcohol)

        except:
            alcohol =" "
            pass

        try:
            exercise=request.POST['all5[2]']
            print("Your are exercise", exercise)

        except:
            exercise =" "
            pass

        try:
            calories=request.POST['all5[3]']
            print("Your are calories", calories)

        except:
            calories =" "
            pass

        try:
            life=request.POST['all5[4]']
            print("Your are life", life)

        except:
            life =" "
            pass


       

        try:
            an6=request.POST['all6']
            print("Your are an6", an6)
        except:
            an6 =" "
            pass

        try:
            cough_qn1=request.POST['all7[0]']
            print("Your are cough_qn1", cough_qn1)
        except:
            cough_qn1 =" "
            pass

        try:
            cough_qn2=request.POST['all7[1]']
            print("Your are cough_qn2", cough_qn2)
        except:
            cough_qn2 =" "
            pass

        try:
            cough_qn3=request.POST['all7[2]']
            print("Your are cough_qn3", cough_qn3)
        except:
            cough_qn3 =" "
            pass

        try:
            cough_qn4=request.POST['all7[3]']
            print("Your are cough_qn4", cough_qn4)
        except:
            cough_qn4 =" "
            pass

        try:
            cough_qn5=request.POST['all7[4]']
            print("Your are cough_qn5", cough_qn5)
        except:
            cough_qn5 =" "
            pass

        try:
            cough_qn6=request.POST['all7[5]']
            print("Your are cough_qn6", cough_qn6)
        except:
            cough_qn6 =" "
            pass

        try:
            cough_qn7=request.POST['all7[6]']
            print("Your are cough_qn7", cough_qn7)
        except:
            cough_qn7 =" "
            pass

        try:
            cough_qn8=request.POST['all7[7]']
            print("Your are cough_qn8", cough_qn8)
        except:
            cough_qn8 =" "
            pass

        try:
            cough_qn9=request.POST['all7[8]']
            print("Your are cough_qn9", cough_qn9)
        except:
            cough_qn9 =" "
            pass


        try:
            chest_qn1=request.POST['all8[0]']
            print("Your are chest_qn1", chest_qn1)
        except:
            chest_qn1 =" "
            pass

        try:
            chest_qn2=request.POST['all8[1]']
            print("Your are chest_qn2", chest_qn2)
        except:
            chest_qn2 =" "
            pass

        try:
            chest_qn3=request.POST['all8[2]']
            print("Your are chest_qn3", chest_qn3)
        except:
            chest_qn3 =" "
            pass

        try:
            chest_qn4=request.POST['all8[3]']
            print("Your are chest_qn4", chest_qn4)
        except:
            chest_qn4 =" "
            pass

        try:
            fever_qn1=request.POST['all9[0]']
            print("Your are fever_qn1", fever_qn1)
        except:
            fever_qn1 =" "
            pass

        try:
            fever_qn2=request.POST['all9[1]']
            print("Your are fever_qn2", fever_qn2)
        except:
            fever_qn2 =" "
            pass

        try:
            fever_qn3=request.POST['all9[2]']
            print("Your are fever_qn3", fever_qn3)
        except:
            fever_qn3 =" "
            pass

        try:
            fever_qn4=request.POST['all9[3]']
            print("Your are fever_qn4", fever_qn4)
        except:
            fever_qn4 =" "
            pass

        try:
            fever_qn5=request.POST['all9[4]']
            print("Your are fever_qn5", fever_qn5)
        except:
            fever_qn5 =" "
            pass

        try:
            fever_qn6=request.POST['all9[5]']
            print("Your are fever_qn6", fever_qn6)
        except:
            fever_qn6 =" "
            pass

        try:
            fever_qn7=request.POST['all9[6]']
            print("Your are fever_qn7", fever_qn7)
        except:
            fever_qn7 =" "
            pass

        try:
            fever_qn8=request.POST['all9[7]']
            print("Your are fever_qn8", fever_qn8)
        except:
            fever_qn8 =" "
            pass


        try:
            abd_qn1=request.POST['all10[0]']
            print("Your are abd_qn1", abd_qn1)
        except:
            abd_qn1 =" "
            pass

        try:
            abd_qn2=request.POST['all10[1]']
            print("Your are abd_qn2", abd_qn2)
        except:
            abd_qn2 =" "
            pass

        try:
            abd_qn3=request.POST['all10[2]']
            print("Your are abd_qn3", abd_qn3)
        except:
            abd_qn3 =" "
            pass

        try:
            abd_qn4=request.POST['all10[3]']
            print("Your are abd_qn4", abd_qn4)
        except:
            abd_qn4 =" "
            pass

        try:
            abd_qn5=request.POST['all10[4]']
            print("Your are abd_qn5", abd_qn5)
        except:
            abd_qn5 =" "
            pass

        try:
            abd_qn6=request.POST['all10[5]']
            print("Your are abd_qn6", abd_qn6)
        except:
            abd_qn6 =" "
            pass

        try:
            abd_qn7=request.POST['all10[6]']
            print("Your are abd_qn7", abd_qn7)
        except:
            abd_qn7 =" "
            pass

        try:
            abd_qn8=request.POST['all10[7]']
            print("Your are abd_qn8", abd_qn8)
        except:
            abd_qn8 =" "
            pass

        try:
            abd_qn9=request.POST['all10[8]']
            print("Your are abd_qn8", abd_qn8)
        except:
            abd_qn9 =" "
            pass

        try:
            anx_qn1=request.POST['all11[0]']
            print("Your are anx_qn1", anx_qn1)
        except:
            anx_qn1 =" "
            pass

        try:
            anx_qn2=request.POST['all11[1]']
            print("Your are anx_qn2", anx_qn2)
        except:
            anx_qn2 =" "
            pass

        try:
            anx_qn3=request.POST['all11[2]']
            print("Your are anx_qn3", anx_qn3)
        except:
            anx_qn3 =" "
            pass

        try:
            anx_qn4=request.POST['all11[3]']
            print("Your are anx_qn4", anx_qn4)
        except:
            anx_qn4 =" "
            pass

        try:
            anx_qn5=request.POST['all11[4]']
            print("Your are anx_qn5", anx_qn5)
        except:
            anx_qn5 =" "
            pass

        try:
            anx_qn6=request.POST['all11[5]']
            print("Your are anx_qn6", anx_qn6)
        except:
            anx_qn6 =" "
            pass

        try:
            anx_qn7=request.POST['all11[6]']
            print("Your are anx_qn7", anx_qn7)
        except:
            anx_qn7 =" "
            pass

        try:
            dep_qn1=request.POST['all12[0]']
            print("Your are dep_qn1", dep_qn1)
        except:
            dep_qn1 =" "
            pass

        try:
            dep_qn2=request.POST['all12[1]']
            print("Your are dep_qn2", dep_qn2)
        except:
            dep_qn2 =" "
            pass

        try:
            dep_qn3=request.POST['all12[2]']
            print("Your are dep_qn3", dep_qn3)
        except:
            dep_qn3 =" "
            pass

        try:
            dep_qn4=request.POST['all12[3]']
            print("Your are dep_qn4", dep_qn4)
        except:
            dep_qn4 =" "
            pass

        try:
            dep_qn5=request.POST['all12[4]']
            print("Your are dep_qn5", dep_qn5)
        except:
            dep_qn5 =" "
            pass

        try:
            dep_qn6=request.POST['all12[5]']
            print("Your are dep_qn6", dep_qn6)
        except:
            dep_qn6 =" "
            pass

        try:
            dep_qn7=request.POST['all12[6]']
            print("Your are dep_qn7", dep_qn7)
        except:
            dep_qn7 =" "
            pass

        try:
            dep_qn8=request.POST['all12[7]']
            print("Your are dep_qn8", dep_qn8)
        except:
            dep_qn8 =" "
            pass

        try:
            dep_qn9=request.POST['all12[8]']
            print("Your are dep_qn9", dep_qn9)
        except:
            dep_qn9 =" "
            pass

####################anxiety#################################

        if anx_qn1=="Several days":
            Anxiety +=1
            print("Anxiety score in first condition is ", Anxiety)
        if anx_qn1=="More than half the days":
            Anxiety+=2
            print("Anxiety score in first condition is ", Anxiety)
        if anx_qn1=="Nearly every day":
            Anxiety+=3
            print("Anxiety score in first condition is ", Anxiety)

        if anx_qn2=="Several days":
            Anxiety+=1
            print("Anxiety score in second condition is ", Anxiety)
        if anx_qn2=="More than half the days":
            Anxiety+=2
            print("Anxiety score in second condition is ", Anxiety)
        if anx_qn2=="Nearly every day":
            Anxiety+=3
            print("Anxiety score in second condition is ", Anxiety)

        if anx_qn3=="Several days":
            Anxiety+=1
            print("Anxiety score in third condition is ", Anxiety)
        if anx_qn3=="More than half the days":
            Anxiety+=2
            print("Anxiety score in third condition is ", Anxiety)
        if anx_qn3=="Nearly every day":
            Anxiety+=3
            print("Anxiety score in third condition is ", Anxiety)

        if anx_qn4=="Several days":
            Anxiety+=1
            print("Anxiety score in fourth condition is ", Anxiety)
        if anx_qn4=="More than half the days":
            Anxiety+=2
            print("Anxiety score in fourth condition is ", Anxiety)
        if anx_qn4=="Nearly every day":
            Anxiety+=3
            print("Anxiety score in fourth condition is ", Anxiety)

        if anx_qn5=="Several days":
            Anxiety+=1
            print("Anxiety score in fifth condition is ", Anxiety)
        if anx_qn5=="More than half the days":
            Anxiety+=2
            print("Anxiety score in fifth condition is ", Anxiety)
        if anx_qn5=="Nearly every day":
            Anxiety+=3
            print("Anxiety score in fifth condition is ", Anxiety)

        if anx_qn6=="Several days":
            Anxiety+=1
            print("Anxiety score in six condition is ", Anxiety)
        if anx_qn6=="More than half the days":
            Anxiety+=2
            print("Anxiety score in six condition is ", Anxiety)
        if anx_qn6=="Nearly every day":
            Anxiety+=3
            print("Anxiety score in six condition is ", Anxiety)

        if anx_qn7=="Several days":
            Anxiety+=1
            print("Anxiety score in seven condition is ", Anxiety)
        if anx_qn7=="More than half the days":
            Anxiety+=2
            print("Anxiety score in seven condition is ", Anxiety)
        if anx_qn7=="Nearly every day":
            Anxiety+=3
            print("Anxiety score in seven condition is ", Anxiety)

 #########################################Depression module################

        if dep_qn1=="Several days":
            Depression+=1
            print("Depression score in first condition is ", Anxiety)
        if dep_qn1=="More than half the days":
            Depression+=2
            print("Depression score in first condition is ", Anxiety)
        if dep_qn1=="Nearly every day":
            Depression+=3
            print("Depression score in first condition is ", Anxiety)

        if dep_qn2=="Several days":
            Depression+=1
        if dep_qn2=="More than half the days":
            Depression+=2
        if dep_qn2=="Nearly every day":
            Depression+=3

        if dep_qn3=="Several days":
            Depression+=1
        if dep_qn3=="More than half the days":
            Depression+=2
        if dep_qn3=="Nearly every day":
            Depression+=3

        if dep_qn4=="Several days":
            Depression+=1
        if dep_qn4=="More than half the days":
            Depression+=2
        if dep_qn4=="Nearly every day":
            Depression+=3

        if dep_qn5=="Several days":
            Depression+=1
        if dep_qn5=="More than half the days":
            Depression+=2
        if dep_qn5=="Nearly every day":
            Depression+=3

        if dep_qn6=="Several days":
            Depression+=1
        if dep_qn6=="More than half the days":
            Depression+=2
        if dep_qn6=="Nearly every day":
            Depression+=3

        if dep_qn7=="Several days":
            Depression+=1
        if dep_qn7=="More than half the days":
            Depression+=2
        if dep_qn7=="Nearly every day":
            Depression+=3

        if dep_qn8=="Several days":
            Depression+=1
        if dep_qn8=="More than half the days":
            Depression+=2
        if dep_qn8=="Nearly every day":
            Depression+=3

        if dep_qn9=="Several days":
            Depression+=1
        if dep_qn9=="More than half the days":
            Depression+=2
        if dep_qn9=="Nearly every day":
            Depression+=3
    




        if age > 40 :
            Cholecystitis+=1.25
            Cardiac_Ischemia+=1.11
            Irritable_Bowel_Disease += 3.33
            Pancreatitis += 1.43
            Chronic_Lung_Disease += 1.43
            Lung_Cancer += 1.67
            print("Cholecystitis score in first condition is ", Cholecystitis)
            print("Cardiac_Ischemia score in first condition is ", Cardiac_Ischemia)

        if age < 40 and age > 0 :
            Pulmonary_Embolism +=1.25
            Inflammatory_Bowel_Disease += 1.25

        if age > 50 :
            Diverticulitis+=1.25
            Chronic_Heart_Failure += 1
            Urinary_Tract_Infection += 1.43
        
        if age > 75 :
            Osteomyelitis += 2

        if age < 50 and age > 0 :
            Asthma+=2

        if age > 20 :
            Endometriosis += 2

        if gender == 'Female':
            Cholecystitis+=1.25
            Cystitis+=2
            Endometriosis += 2
            print("Cholecystitis score in second condition is ", Cholecystitis)
        
        if gender == 'Male':
            Renal_Calculi+=2.5
            Cardiac_Ischemia+=1.11
            Pancreatitis += 1.43
            print("Renal_Calculi score in first condition is ", Renal_Calculi)
            print("Cardiac_Ischemia score in second condition is ", Cardiac_Ischemia)

        if BMI > 25 :
            Cellulitis += 2

        if BMI > 30 :
            Cholecystitis+=1.25
            Gastritis+=1.25
            Diverticulitis+=1.25
            Cardiac_Ischemia+=1.11
            Pulmonary_Embolism +=1.25
            print("Cholecystitis score in third condition is ", Cholecystitis)
            print("Gastritis score in first condition is ", Gastritis)
            print("Cardiac_Ischemia score in third condition is ", Cardiac_Ischemia)

        if BMI < 20 :
            Inflammatory_Bowel_Disease += 1.25

        if daibetes== 'Yes':
            Cholecystitis+=1.25
            Gastritis+=1.25
            Cystitis+=2
            Pyelonephritis+=2.5
            Renal_Calculi+=2.5
            Diverticulitis+=1.25
            Pancreatitis += 1.43
            Chronic_Heart_Failure += 1
            Cellulitis += 2
            Urinary_Tract_Infection += 1.43
            Osteomyelitis += 2
            print("Cholecystitis score in fourth condition is ", Cholecystitis)
            print("Gastritis score in second condition is ", Gastritis)
            print("Renal_Calculi score in second condition is ", Renal_Calculi)
         

        if Hypertension== 'Yes':
            Chronic_Heart_Failure += 1

        if Heart_disease== 'Yes':
            Chronic_Heart_Failure += 1




        if daibetes== 'Yes' or  Hypertension == 'Yes' or Heart_disease == 'Yes' or Strokes == 'Yes' or all_above == 'Yes'  :
            Cardiac_Ischemia+=1.11
            print("Cardiac_Ischemia score in fourth condition is ", Cardiac_Ischemia)

        if alcohol== 'Yes':
            Cholecystitis+=1.25
            Gastritis+=1.25
            Pulmonary_Embolism +=1.25
            Pancreatitis += 1.43
            print("Cholecystitis score in fifth condition is ", Cholecystitis)
            print("Gastritis score in third condition is ", Gastritis)

        if smoke== 'Yes':
            Pneumonia+=1.11
            Gastritis +=1.25
            Cardiac_Ischemia+=1.11
            Viral_Bronchitis+=1.67
            Pleurisy +=3.33
            Costochondritis +=3.33
            Chronic_Heart_Failure += 1
            Chronic_Lung_Disease += 1.43
            Lung_Cancer += 1.67
            COVID += 1.43
            Viral_Fever += 1.67
            Cellulitis += 2
            print("Gastritis score in fourth condition is ", Gastritis)
            print("Cardiac_Ischemia score in fifth condition is ", Cardiac_Ischemia)

        if an6== 'Few days' or an6== 'Few weeks' :
            Pneumonia+=1.11
            Cholecystitis+=1.25
            Cystitis+=2
            Cardiac_Ischemia+=1.11
            Pulmonary_Embolism +=1.25
            Endometriosis += 2
            COVID += 1.43
            Urinary_Tract_Infection += 1.43
            print("Cholecystitis score in six condition is ", Cholecystitis)
            print("Cardiac_Ischemia score in six condition is ", Cardiac_Ischemia)

        if an6== 'Few days': 
            Pyelonephritis+=2.5
            Renal_Calculi+=2.5
            Viral_Bronchitis+=1.67
            Appendicitis += 2.5
            Viral_Fever += 1.67
            Meningitis += 3.33
            print("Renal_Calculi score in third condition is ", Renal_Calculi)

        if an6== 'Few weeks': 
            Cellulitis += 2

        if an6== 'Few weeks' or an6== 'Few Months' or an6== 'Many months' :
            Gastritis+=1.25
            Asthma+=2
            print("Gastritis score in fifth condition is ", Gastritis)

        if an6== 'Few weeks' or an6== 'Few Months' :
            Inflammatory_Bowel_Disease += 1.25
            Pancreatitis += 1.43
            Osteomyelitis += 2
            

        if an6== 'Few Months' or an6== 'Many months' :
            Diverticulitis+=1.25
            Chronic_Heart_Failure += 1
            Chronic_Lung_Disease += 1.43

        if cough_qn1== 'Yes':
           Viral_Bronchitis+=1.67
           Pleurisy +=3.33
           Costochondritis +=3.33
           COVID += 1.43
           Viral_Fever += 1.67
            
        if cough_qn2== 'Yes':
            Pneumonia+=1.11
            Pulmonary_Embolism +=1.25
            Viral_Bronchitis+= 1.67
            COVID += 1.43
            Viral_Fever += 1.67

        if cough_qn3== 'Yes':
            COVID += 1.43

        if cough_qn4== 'Yes':
            Pneumonia+=1.11
            Viral_Bronchitis+=1.67
            COVID += 1.43

        if cough_qn5== 'Yes':
            Pneumonia+=1.11
            Chronic_Lung_Disease += 1.43
            Lung_Cancer += 1.67
            Viral_Fever += 1.67

        if cough_qn6== 'Yes':
            Pneumonia+=1.11
            Pulmonary_Embolism +=1.25
            Chronic_Heart_Failure += 1
            Chronic_Lung_Disease += 1.43
            Lung_Cancer += 1.67
            

        if cough_qn7== 'Yes':
            Pulmonary_Embolism +=1.25
            Asthma+=2
            Chronic_Heart_Failure += 1
            Chronic_Lung_Disease += 1.43

        if cough_qn8== 'Yes':
            Pneumonia+=1.11
            Cardiac_Ischemia+=1.11
            Asthma+=2
            Chronic_Heart_Failure += 1
            Chronic_Lung_Disease += 1.43
            Lung_Cancer += 1.67
            COVID += 1.43
            print("Cardiac_Ischemia score in seven condition is ", Cardiac_Ischemia)

        if cough_qn9== 'Yes':
            Chronic_Heart_Failure += 1

        if chest_qn1== 'Yes':
            Pneumonia+=1.11
            Pulmonary_Embolism +=1.25
            Pleurisy +=3.33
            Costochondritis +=3.33
            

        if chest_qn2== 'Yes':
            Cardiac_Ischemia+=1.11
            print("Cardiac_Ischemia score in eight condition is ", Cardiac_Ischemia)

        if chest_qn3== 'Yes':
            Cardiac_Ischemia+=1.11
            print("Cardiac_Ischemia score in nine condition is ", Cardiac_Ischemia)

        if chest_qn4== 'Yes':
            Asthma+=2

        if fever_qn2== 'Yes':
            Diverticulitis+=1.25
            Appendicitis += 2.5 
            Inflammatory_Bowel_Disease += 1.25

        if fever_qn3== 'Yes':
            Osteomyelitis += 2
        
        if fever_qn4== 'Yes':
            Cellulitis += 2
            Osteomyelitis += 2

        if fever_qn5== 'Yes':
            Cystitis+=2
            Pyelonephritis+=2.5
            Renal_Calculi+=2.5
            Urinary_Tract_Infection += 1.43

        if fever_qn6== 'Yes':
            Viral_Bronchitis+=1.67
            Meningitis += 3.33
            Viral_Fever += 1.67

        if fever_qn7== 'Yes':
            Meningitis += 3.33

        if fever_qn8== 'Yes':
            Pneumonia+=1.11

        
        if abd_qn1 == 'Yes':
            Cholecystitis+=1.25
            Gastritis+=1.25
            Pancreatitis += 1.43
            print("Cholecystitis score in seven condition is ", Cholecystitis)
            print("Gastritis score in six condition is ", Gastritis)

        if abd_qn2 == 'Yes':
            Cystitis+=2
            Pyelonephritis+=2.5
            Diverticulitis+=1.25
            Appendicitis += 2.5 
            Inflammatory_Bowel_Disease += 1.25
            Irritable_Bowel_Disease += 3.33
            Endometriosis += 2
            Urinary_Tract_Infection += 1.43
           

        if abd_qn3 == 'Yes':
            Cholecystitis+=1.25
            Diverticulitis+=1.25
            Appendicitis += 2.5
            Inflammatory_Bowel_Disease += 1.25
            Urinary_Tract_Infection += 1.43
           
            print("Cholecystitis score in eight condition is ", Cholecystitis)
         

        if abd_qn4 == 'Yes':
            Gastritis+=1.25
            print("Gastritis score in seven condition is ", Gastritis)

        
        if abd_qn5 == 'Yes':
            Urinary_Tract_Infection += 1.43

        if abd_qn6 == 'Yes':
            Diverticulitis+=1.25
            Inflammatory_Bowel_Disease += 1.25
            

        if abd_qn7 == 'Yes':
            Gastritis+=1.25
            Irritable_Bowel_Disease += 3.33
            print("Gastritis score in eight condition is ", Gastritis)

        if abd_qn8 == 'Yes':
            Inflammatory_Bowel_Disease += 1.25
            Pancreatitis += 1.43
            Lung_Cancer += 1.67

        if abd_qn9 == 'Yes':
            Endometriosis += 2


        print("Total score for pneumonia is", Pneumonia)

        context2 ={

                        "Appendicitis": Appendicitis,            
                        "Cholecystitis" : Cholecystitis,
                        "Gastritis" : Gastritis,
                        "Cystitis" : Cystitis,
                        "Pyelonephritis" : Pyelonephritis,
                        "Renal_Calculi" :  Renal_Calculi,
                        "Diverticulitis" : Diverticulitis,
                        "Intestinal Obstruction" : Intestinal_Obstruction,
                        "Inflammatory Bowel Disease" : Inflammatory_Bowel_Disease,
                        "Irritable Bowel Disease" : Irritable_Bowel_Disease,
                        "Pancreatitis" : Pancreatitis, 
                        "Endometriosis" :  Endometriosis,
                        "Cardiac Ischemia":Cardiac_Ischemia,
                        "Pulmonary Embolism":Pulmonary_Embolism,
                        "Pleurisy":Pleurisy,
                        "Costochondritis":Costochondritis,
                        "Pneumonia":Pneumonia,
                        "Viral Bronchitis":Viral_Bronchitis,
                        "Asthma":Asthma,
                        "Chronic Heart Failure":Chronic_Heart_Failure,
                        "Chronic Lung Disease" :Chronic_Lung_Disease,
                        "Lung Cancer":Lung_Cancer,
                        "COVID_":COVID,
                        "Diabetes" : Diabetes,
                        "Viral Fever":Viral_Fever,
                        "Cholangitis" : Cholangitis,
                        "Endocarditis" : Endocarditis,
                        "Cellulitis" : Cellulitis,
                        "Urinary Tract Infection" : Urinary_Tract_Infection,
                        "Osteomyelitis" : Osteomyelitis,
                        "Meningitis": Meningitis,
                        "Anxiety" : Anxiety,
                        "Depression":Depression
                               
                            }

    

        print("Context2" , context2 )

        anx_depr1= {
            "Anxiety":Anxiety,
            "Depression":Depression,
        }

        Personal_Information1 =  ClientID.objects.create(Age=age, Email=email, created_Date= datetime.datetime.now() )
        Personal_Information1.save()
        Personal_Information2 =  RiskID.objects.create(Unique_ID=Personal_Information1, Height=height, Weight=weight, BMI=BMI ,Sex=gender, Diabetes=daibetes , Hypertension= Hypertension , Heart_disease= Heart_disease , Strokes= Strokes , History_of_4= all_above , Smoke=smoke , Alcohol= alcohol,Exercise= exercise , Calories_count= calories , Age_90_years= life , Covid_history =cough_qn2)
        Personal_Information2.save()

        # sorted_context2 = sorted(context2.items(), key=operator.itemgetter(1))
        sorted_context2 = dict( sorted(context2.items(), key=operator.itemgetter(1),reverse=True))
        print("sorted_context2" , sorted_context2)
        x = sorted(((v,k) for k,v in context2.items() ))
        print ("len of x",len(x))

    
        first_name = x[-1][1]
        first_value = x[-1][0]
        second_name = x[-2][1]
        second_value = x[-2][0]
        third_name = x[-3][1]
        third_value = x[-3][0]
        fourth_name = x[-4][1]
        fourth_value = x[-4][0]
        

        print("first_value",first_value)
        print("second_value",second_value)
        print("third_value",third_value)
        print("fourth_value",fourth_value)
        context3 = {
            first_name: first_value,
            second_name :second_value,
            third_name :third_value,
            fourth_name : fourth_value,

        }

        print("Context3" , context3 )
        print("anx_depr1" , anx_depr1 )
        
        

        if Anxiety <5:
            anx_risk= "Your overall risk assessment for Anxiety is Normal"
            # print("Your overall risk assessment for Anxiety is Normal")
            # return render(request,"CombinedModule_result_display.html",{'context':context2 , 'Risk_Assessment' : "Your overall risk assessment for Anxiety is Normal" })

        if Anxiety>=5 and Anxiety<10:
            anx_risk= "Your overall risk assessment for Anxiety is Mild"
            # print("Your overall risk assessment for Anxiety is Mild")
            # return render(request,"CombinedModule_result_display.html",{'context':context2 , 'Risk_Assessment' : "Your overall risk assessment for Anxiety is Mild" })

        if Anxiety>=10 and Anxiety<15:
            anx_risk= "Your overall risk assessment for Anxiety is Moderate"
            # print("Your overall risk assessment for Anxiety is Moderate")
            # return render(request,"CombinedModule_result_display.html",{'context':context2 , 'Risk_Assessment' : "Your overall risk assessment for Anxiety is Moderate" })
            
        
        if Anxiety>=15:
            anx_risk= "Your overall risk assessment for Anxiety is severe"
            # print("Your overall risk assessment for Anxiety is severe ")
            # return render(request,"CombinedModule_result_display.html",{'context':context2 , 'Risk_Assessment' : "Your overall risk assessment for Anxiety is severe" })

        if Depression<4:
            dep_risk= "Your overall risk assessment for Depression is Normal"
            #  print("Your overall risk assessment for Depression is Normal")
            #  return render(request,"CombinedModule_result_display.html",{'context':context2 , 'Risk_Assessment1' : "Your overall risk assessment for Depression is Normal" })

        if Depression>=5 and Depression<=9:
            dep_risk= "Your overall risk assessment for Depression is Mild"
            # print("Your overall risk assessment for Depression is Mild")
            # return render(request,"CombinedModule_result_display.html",{'context':context2 , 'Risk_Assessment1' : "Your overall risk assessment for Depression is Mild" })

        if Depression>=10 and Depression<=14:
            dep_risk= "Your overall risk assessment for Depression is Moderate"
            # print("Your overall risk assessment for Depression is Moderate")
            # return render(request,"CombinedModule_result_display.html",{'context':context2 , 'Risk_Assessment1' : "Your overall risk assessment for Depression is Moderate" })

        if Depression>=15 and Depression<=19:
            dep_risk= "Your overall risk assessment for Depression is Moderately severe"
            # print("Your overall risk assessment for Depression is Moderately severe")
            # return render(request,"CombinedModule_result_display.html",{'context':context2 , 'Risk_Assessment1' : "Your overall risk assessment for Depression is Moderately severe" })

        if Depression>=20 and Depression<=27:
            dep_risk= "Your overall risk assessment for Depression is severe"
            # print("Your overall risk assessment for Depression is severe")
            # return render(request,"CombinedModule_result_display.html",{'context':context2 , 'Risk_Assessment1' : "Your overall risk assessment for Depression is severe" })

        anx_dep_risk= {
            "anx_module" : anx_risk, 
            "dep_module" : dep_risk

        }

        return render(request,"CombinedModule_result_display.html",{'context':sorted_context2 , 'Risk_Assessment' : anx_dep_risk })


    return render(request,"combined module.html" )






@csrf_exempt
def CCF_module(request):

    # global Appendicitis
    # global Cholecystitis
    # global Gastritis
    # global Cystitis
    # global Pyelonephritis
    # global Inflammatory_Bowel_Disease
    # global Irritable_Bowel_Disease
    # global Pancreatitis
    # global Endometriosis
    # global Anxiety
    # global Depression
    # global Cardiac_Ischemia
    # global Pulmonary_Embolism
    # global Pleurisy
    # global Costochondritis
    # global Pneumonia
    # global Viral_Bronchitis
    # global Asthma
    # global Chronic_Heart_Failure
    # global Chronic_Lung_Disease
    # global Lunc_Cancer
    # global COVID
    # global Diabetes
    # global Viral_Fever
    # global Cholangitis
    # global Endocarditis
    # global Cellulitis
    # global Urinary_Tract_Infection
    # global Osteomyelitis
    # global Meningitis
    
    if request.method == 'GET':
        return render(request, "CCFForm.html")

    if request.method == 'POST':
        Appendicitis=0
        Cholecystitis=0
        Gastritis=0
        Cystitis=0
        Pyelonephritis=0
        Inflammatory_Bowel_Disease=0
        Irritable_Bowel_Disease=0
        Pancreatitis=0
        Endometriosis=0
        Anxiety=0
        Depression=0
        Cardiac_Ischemia=0
        Pulmonary_Embolism=0
        Pleurisy=0
        Costochondritis=0
        Pneumonia=0
        Viral_Bronchitis=0
        Asthma=0
        Chronic_Heart_Failure=0
        Chronic_Lung_Disease=0
        Lunc_Cancer=0
        COVID=0
        Diabetes=0
        Viral_Fever=0
        Cholangitis=0
        Endocarditis=0
        Cellulitis=0
        Urinary_Tract_Infection=0
        Osteomyelitis=0
        Meningitis=0

        context1 ={

                        "Appendicitis": Appendicitis,
                        "Cholecystitis" : Cholecystitis,
                        "Gastritis" : Gastritis,
                        "Cystitis" : Cystitis,
                        "Pyelonephritis" : Pyelonephritis,
                        "Inflammatory Bowel Disease" : Inflammatory_Bowel_Disease,
                        "Irritable Bowel Disease" : Irritable_Bowel_Disease,
                        "Pancreatitis" : Pancreatitis, 
                        " Endometriosis" :  Endometriosis,
                        "Anxiety":Anxiety,
                        "Depression":Depression,
                        "Cardiac Ischemia":Cardiac_Ischemia,
                        "Pulmonary Embolism":Pulmonary_Embolism,
                        "Pleurisy":Pleurisy,
                        "Costochondritis":Costochondritis,
                        "Pneumonia":Pneumonia,
                        "Viral Bronchitis":Viral_Bronchitis,
                        "Asthma":Asthma,
                        "Chronic Heart Failure":Chronic_Heart_Failure,
                        "Chronic Lung Disease" :Chronic_Lung_Disease,
                        "Lung Cancer":Lunc_Cancer,
                        "COVID_":COVID,
                        "Diabetes" : Diabetes,
                        "Viral Fever":Viral_Fever,
                        "Cholangitis" : Cholangitis,
                        "Endocarditis" : Endocarditis,
                        "Cellulitis" : Cellulitis,
                        "Urinary Tract Infection" : Urinary_Tract_Infection,
                        "Osteomyelitis" : Osteomyelitis,
                        "Meningitis": Meningitis
                               
                            }

        print("context1",context1 )



        for question_id in request.POST:
            print(request.POST)
            print(question_id)
            answer_id = request.POST[question_id]
            if question_id == "ccf2[field_1]":
                print("2nd qn part1 is executed")
                print("answer ids are",answer_id )
                if answer_id <= "40" :
                    
                    Inflammatory_Bowel_Disease+=1
                    Chronic_Lung_Disease+=1
                    print("Inflammatory_Bowel_Disease", Inflammatory_Bowel_Disease)
                if  answer_id >= "60":
                    Chronic_Heart_Failure+=1

            if question_id == "ccf2[field_9]":
                print("2nd qn part2 is executed")
                if answer_id == "Female":
                    Endometriosis +=1

       
            weight= request.POST['ccf2[field_3]'] 
            # print("Your weight is ", weight )
            height= request.POST['ccf2[field_4]']
            height_in_meter = round((int(height)/100),2)
            # print ("height_in_meter",height_in_meter)
            BMI = round((int(weight) / (height_in_meter * height_in_meter)),2)
            print("Your calculated BMI is", BMI)

            if BMI >30:
                Diabetes+=1
                Cholangitis+=1

            if question_id == "ccf2[field_5]":
                print("2nd qn part5 is executed")
                if answer_id == "Yes":
                    Chronic_Heart_Failure+=1
                    Chronic_Lung_Disease+=1

            if question_id == "ccf2[field_6]":
                if answer_id == "Yes":
                    Pleurisy+=1
                    Costochondritis+=1
                    Pneumonia+=1
                    Viral_Bronchitis+=1
                    Asthma+=1
                    Lunc_Cancer+=1

            if question_id == "ccf2[field_7]":
                if answer_id == "Yes":
                    COVID+=1
                    Viral_Bronchitis+=1

            if question_id == "ccf2[field_8]":
                if answer_id == "Day":
                    Cardiac_Ischemia+=1
                    Pulmonary_Embolism+=1
                    Pleurisy+=1
                    Costochondritis+=1
                    Pneumonia+=1
                    Viral_Bronchitis+=1
                    Asthma+=1
                    COVID+=1
                    Viral_Fever+=1
        

                if answer_id == "Month":
                    Chronic_Heart_Failure+=1
                    Chronic_Lung_Disease+=1
                    Lunc_Cancer+=1

            if question_id == "ccf3[0]":
                if answer_id == "Yes":
                    Chronic_Heart_Failure+=1
                    Chronic_Lung_Disease+=1
            
            if question_id == "ccf3[1]":
                if answer_id == "No":
                    Diabetes+=1

            if question_id == "ccf3[2]":
                if answer_id == "Yes":
                    Diabetes+=1

            if question_id == "ccf3[3]":
                if answer_id == "No":
                    Cardiac_Ischemia+=1
                    print("Cardiac_Ischemia", Cardiac_Ischemia)

            if question_id == "ccf4":
                if answer_id == "Yes":
                    Costochondritis+=1
                    Viral_Bronchitis+=1
                    COVID+=1
                    Viral_Fever+=1

            if question_id == "ccf6":
                if answer_id == "Yes":
                    Pneumonia +=1
                    Lunc_Cancer +=1
                    Pulmonary_Embolism +=1

            if question_id == "ccf7":
                if answer_id == "Yes":
                    Pulmonary_Embolism +=1
                    Pleurisy +=1

            if question_id == "ccf9":
                if answer_id == "Yes":
                    Cardiac_Ischemia+=1

            if question_id == "ccf10":
                if answer_id == "Yes":
                    Chronic_Heart_Failure+=1

            if question_id == "ccf12":
                if answer_id == "Yes":
                    Cellulitis +=1
            
            if question_id == "ccf13":
                if answer_id == "Yes":
                    Meningitis +=1

            if question_id == "ccf14":
                if answer_id == "Yes":
                    Meningitis +=1

            if question_id == "ccf15":
                if answer_id == "Yes":
                    Meningitis +=1

            if question_id == "ccf16":
                if answer_id == "Yes":
                    Urinary_Tract_Infection +=1

            if question_id == "ccf17":
                if answer_id == "Yes":
                    Inflammatory_Bowel_Disease +=1

        context ={
                        "Appendicitis": Appendicitis,
                        "Cholecystitis" : Cholecystitis,
                        "Gastritis" : Gastritis,
                        "Cystitis" : Cystitis,
                        "Pyelonephritis" : Pyelonephritis,
                        "Inflammatory Bowel Disease" : Inflammatory_Bowel_Disease,
                        "Irritable Bowel Disease" : Irritable_Bowel_Disease,
                        "Pancreatitis" : Pancreatitis, 
                        " Endometriosis" :  Endometriosis,
                        "Anxiety":Anxiety,
                        "Depression":Depression,
                        "Cardiac Ischemia":Cardiac_Ischemia,
                        "Pulmonary Embolism":Pulmonary_Embolism,
                        "Pleurisy":Pleurisy,
                        "Costochondritis":Costochondritis,
                        "Pneumonia":Pneumonia,
                        "Viral Bronchitis":Viral_Bronchitis,
                        "Asthma":Asthma,
                        "Chronic Heart Failure":Chronic_Heart_Failure,
                        "Chronic Lung Disease" :Chronic_Lung_Disease,
                        "Lung Cancer":Lunc_Cancer,
                        "COVID_":COVID,
                        "Diabetes" : Diabetes,
                        "Viral Fever":Viral_Fever,
                        "Cholangitis" : Cholangitis,
                        "Endocarditis" : Endocarditis,
                        "Cellulitis" : Cellulitis,
                        "Urinary Tract Infection" : Urinary_Tract_Infection,
                        "Osteomyelitis" : Osteomyelitis,
                        "Meningitis": Meningitis

                    }

                         
        print ("context",context)

        x = sorted(((v,k) for k,v in context.items() ))
        print ("len of x",len(x))
        
        if len(x) == 0:
            context2 = {
                "Disease": "No disease found",

                }
            
            return render(request,"CCF_result_display.html",{'nodisease':"No Disease Found"})
        
        

        if len(x) == 1:
            first_name = x[-1][1]
            first_value = x[-1][0]
        

            context2 = {
                first_name: "Most Likely",

                }
          
            return render(request,"CCF_result_display.html",{'context':context2})

        
        if len(x) == 2:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
           
            context2 = {
                first_name: "Most Likely",
                second_name :"Possible",
                }
           
            return render(request,"CCF_result_display.html",{'context':context2})



        if len(x) == 3:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            third_name = x[-3][1]
            third_value = x[-3][0]
           
            context2 = {
                first_name: "Most Likely",
                second_name :"Likely",
                third_name : "Possible",
                }
          
            return render(request,"CCF_result_display.html",{'context':context2})


        if len(x) > 3:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            third_name = x[-3][1]
            third_value = x[-3][0]
            fourth_name = x[-4][1]
            fourth_value = x[-4][0]
           

            print("first_value",first_value)
            print("second_value",second_value)
            print("third_value",third_value)
            print("fourth_value",fourth_value)
            context2 = {
                first_name: first_value,
                second_name :second_value,
                third_name :third_value,
                fourth_name : fourth_value,

            }
           
            return render(request,"CCF_result_display.html",{'context':context2})

    # return render(request, "CCFForm.html")



@csrf_exempt
def all_modules(request):
    global Appendicitis
    global Cholecystitis
    global Cystitis
    global Pyelonephritis
    global Renal_Calculi
    global Diverticulitis
    global Inflammatory_Bowel
    global Irritable_Bowel

    global Pancreatitis
    global Endometriosis
    global Gastritis

    global Viral_Fever
    global COVID
    global Pneumonia
    global Cholangitis
    global Endocarditis
    global Cellulitis
    global UTI
    global Osteomyelitis
    global Meningitis

    # return render(request, "CCF_chatbot.html")
    if request.method == 'GET':
        return render(request,"newForm.html" )

    if request.method == 'POST':
        print('POST', request.POST)
        print('BODY', request.body)
        post_data = dict(request.POST.lists())
        VB=0
        BP=0
        A=0
        CHF=0
        CLD=0
        LC=0
        PE=0
        covid=0


        Appendicitis= 0
        Cholecystitis= 0
        Cystitis= 0
        Pyelonephritis= 0
        Renal_Calculi= 0
        Diverticulitis= 0
        Inflammatory_Bowel= 0
        Irritable_Bowel= 0

        Pancreatitis= 0
        Endometriosis= 0
        Gastritis = 0


        # ############# fever ###########

        # Viral_Fever =0
        # COVID=0
        # Pneumonia=0
        # Cholangitis=0
        # Endocarditis=0
        # Cellulitis=0
        # UTI=0
        # Osteomyelitis=0
        # Meningitis=0

        # # datae= user.user_detail.dob

        # # print ("user.user_detail.dob",datae.year)
        # def calculateAge(birthDate):
        #     global UTI

        #     days_in_year = 365.2425
        #     try :
        #         age = int((date.today() - birthDate).days / days_in_year)
        #         print ("age in try", age)
        #         if int(age) > 75:
        #             print ("value can be added")
        #             UTI+=1
        #     except Exception as e:
        #         pass
        #     return age

        # # print(calculateAge(date(datae.year,datae.month,datae.day)), "years")

        # # if user.user_detail.CurrentSmoker== "Yes" or user.user_detail.PastSmoker=="Yes":

        # #     Pneumonia+=1



        # for question_id in request.POST:
        #     print(request.POST)

        #     answer_id = request.POST[question_id]
        #     # print("answer_id", answer_id)
        #     # if question_id != "csrfmiddlewaretoken":
        #     #     print ("question_id",question_id)
        #     #     print ("answer_id",answer_id)
        #     #     question_answer_save = Fever_answer_details.objects.create(user=user,Question_id=question_id,Answer_id=answer_id,Diagnosis_name="Fever",last_date_of_analysis=datetime.datetime.now())
        #     #     question_answer_save.save()
        #     if question_id == "cg13":
        #         # print("answer_id1", answer_id)

        #         if answer_id == "Less than 1 week":
        #             Viral_Fever+=1
        #             COVID+=0.5
        #             Pneumonia+=0.25
        #             Cholangitis+=0.5
        #             Endocarditis-=1
        #             Cellulitis+=0
        #             UTI+=0
        #             Osteomyelitis-=1
        #             Meningitis+=1

        #         if answer_id == "More than 1 week":
        #             Viral_Fever+=0
        #             COVID+=0.5
        #             Pneumonia+=1
        #             Cholangitis+=0.5
        #             Endocarditis+=1
        #             Cellulitis+=1
        #             UTI+=1
        #             Osteomyelitis+=1
        #             Meningitis+=0.5
        #     if question_id == "cg14":
        #         # print("answer_id2", answer_id)
        #         if answer_id == "Yes":
        #             Viral_Fever+=1
        #             COVID+=0.5
        #             Pneumonia+=0
        #             Cholangitis-=1
        #             Endocarditis-=1
        #             Cellulitis-=1
        #             UTI-=1
        #             Osteomyelitis-=1
        #             Meningitis+=0

        #     if question_id =="cg15" :
        #         # print("answer_id3", answer_id)
        #         if answer_id == "Yes":
        #             Viral_Fever+=1
        #             COVID+=1
        #             Pneumonia+=1
        #             Cholangitis-=1
        #             Endocarditis-=1
        #             Cellulitis-=1
        #             UTI-=1
        #             Osteomyelitis-=1
        #             Meningitis+=0.5

        #     if question_id =="cg16":
        #         if answer_id == "Yes":
        #             Viral_Fever+=0
        #             COVID-=1
        #             Pneumonia+=0
        #             Cholangitis+=0
        #             Endocarditis+=0
        #             Cellulitis+=0
        #             UTI+=0
        #             Osteomyelitis+=0
        #             Meningitis+=0.75

        #     if question_id == "cg17":
        #         if answer_id == "Yes":
        #             Viral_Fever+=0.25
        #             COVID+=0.25
        #             Pneumonia+=1
        #             Cholangitis-=1
        #             Endocarditis-=1
        #             Cellulitis-=1
        #             UTI-=1
        #             Osteomyelitis-=1
        #             Meningitis+=0

        #     if question_id =="cg18":
        #         if answer_id == "Yes":
        #             Viral_Fever-=0.5
        #             COVID+=0.5
        #             Pneumonia+=1
        #             Cholangitis-=1
        #             Endocarditis+=0.25
        #             Cellulitis-=1
        #             UTI-=1
        #             Osteomyelitis-=1
        #             Meningitis+=0
        #     if question_id=="cg19":

        #         if answer_id == "Yes":
        #             Viral_Fever+=0.25
        #             COVID+=0.5
        #             Pneumonia+=0.5
        #             Cholangitis-=1
        #             Endocarditis+=0.5
        #             Cellulitis-=1
        #             UTI-=1
        #             Osteomyelitis-=1
        #             Meningitis-=1

        #     if question_id=="cg20":

        #         if answer_id == "Yes":
        #             Viral_Fever-=1
        #             COVID+=0
        #             Pneumonia+=0
        #             Cholangitis+=1
        #             Endocarditis-=1
        #             Cellulitis-=1
        #             UTI+=1
        #             Osteomyelitis-=1
        #             Meningitis-=1

        #     if question_id=="cg21":

        #         if answer_id == "Yes":
        #             Viral_Fever+=0.25
        #             COVID+=0
        #             Pneumonia+=0
        #             Cholangitis+=1
        #             Endocarditis+=0
        #             Cellulitis+=0
        #             UTI+=0
        #             Osteomyelitis-=1
        #             Meningitis-=1

        #     if question_id=="cg22":

        #         if answer_id == "Yes":
        #             Viral_Fever-=1
        #             COVID-=1
        #             Pneumonia-=1
        #             Cholangitis+=1
        #             Endocarditis-=0
        #             Cellulitis-=1
        #             UTI-=1
        #             Osteomyelitis-=1
        #             Meningitis-=1

        #     if question_id=="cg23":
        #         if answer_id == "Yes":
        #             Viral_Fever-=1
        #             COVID-=1
        #             Pneumonia-=0.5
        #             Cholangitis+=0.5
        #             Endocarditis+=1
        #             Cellulitis-=1
        #             UTI-=1
        #             Osteomyelitis+=1
        #             Meningitis-=1

        #     if question_id=="cg24":
        #         if answer_id == "Yes":
        #             Viral_Fever-=1
        #             COVID-=1
        #             Pneumonia-=1
        #             Cholangitis-=1
        #             Endocarditis+=0.5
        #             Cellulitis+=1
        #             UTI-=1
        #             Osteomyelitis+=1
        #             Meningitis-=1

        #     if question_id=="cg25":

        #         if answer_id == "Yes":
        #             Viral_Fever-=1
        #             COVID-=1
        #             Pneumonia-=1
        #             Cholangitis-=1
        #             Endocarditis-=1
        #             Cellulitis-=1
        #             UTI+=1
        #             Osteomyelitis-=1
        #             Meningitis+=0

        #     if question_id=="cg26":
        #         if answer_id == "Yes":
        #             Viral_Fever+=0.25
        #             COVID+=0.5
        #             Pneumonia+=0.5
        #             Cholangitis-=1
        #             Endocarditis+=0.5
        #             Cellulitis-=1
        #             UTI+=0
        #             Osteomyelitis+=0
        #             Meningitis+=1

        #     if question_id=="cg27":

        #         if answer_id == "Yes":
        #             Viral_Fever-=1
        #             COVID+=0.25
        #             Pneumonia+=0.25
        #             Cholangitis-=1
        #             Endocarditis+=0
        #             Cellulitis-=1
        #             UTI-=1
        #             Osteomyelitis-=1
        #             Meningitis+=1

        #     if question_id=="cg28":

        #         if answer_id == "Yes":
        #             Viral_Fever-=1
        #             COVID+=0
        #             Pneumonia+=0
        #             Cholangitis-=1
        #             Endocarditis+=0
        #             Cellulitis-=1
        #             UTI-=1
        #             Osteomyelitis-=1
        #             Meningitis+=1



    ######## Cough module ###########

        context1 ={

            "Viral_Bronchitis":VB,
            "Bacterial_Pneumonia":BP,
            "Asthma":A,
            "Chronic_Heart_Failure":CHF,
            "Chronic_Lung_Disease":CLD,
            "Lung_Cancer":LC,
            "Pleural_Embolism":PE,
            "covid":covid


        }

        print ("context1",context1)
        for question_id in post_data:
            print ("key",question_id)
            print ("value",post_data[question_id])
            answer_id = post_data[question_id]
            if question_id == "cg1[]":
                for answer_id in answer_id:
                    print ("answer_id",answer_id)
                    if answer_id=="Asthma":
                        VB+=0
                        BP+=0
                        A+=1
                        CHF+=0.25
                        CLD+=0.25
                        LC+=0
                        PE+=0
                    if answer_id=="Heart disease":
                        VB+=0
                        BP+=0
                        A+=0.5
                        CHF+=1
                        CLD+=0.5
                        LC+=0
                        PE+=0
                    if answer_id=="Lung disease":
                        VB+=0
                        BP+=0.5
                        A+=0.5
                        CHF+=0.5
                        CLD+=1
                        LC+=0
                        PE+=0
                    if answer_id=="Clots in the body":
                        VB+=0
                        BP+=0
                        A+=0
                        CHF+=0
                        CLD+=0
                        LC+=0
                        PE+=1
                    if answer_id=="Allergies":
                        VB+=0
                        BP+=0
                        A+=1
                        CHF+=0
                        CLD+=0
                        LC+=0
                        PE+=0
                    if answer_id=="Smoking":
                        VB+=0.5
                        BP+=0.5
                        A+=0.5
                        CHF+=0.5
                        CLD+=0.5
                        LC+=1
                        PE+=0
                    if answer_id=="COVID":
                        VB+=0.25
                        BP+=0.5
                        A+=0.5
                        CHF+=0.25
                        CLD+=1
                        LC+=0
                        PE+=0.5

            if question_id == "cg2":
                for answer_id in answer_id:
                    if answer_id == "Less than 1 week":
                        VB+=1
                        BP+=0.25
                        A+=0.25
                        CHF-=1
                        CLD-=1
                        LC-=1
                        PE+=1
                        covid+=1
                    if answer_id == "Less than 1 month":
                        VB-=0.5
                        BP+=1
                        A+=0.5
                        CHF+=0.25
                        CLD-=1
                        LC+=0.5
                        PE+=0.5
                        covid+=0.75
                    if answer_id == "More than 1 month":
                        VB-=1
                        BP+=0.25
                        A+=0.75
                        CHF+=1
                        CLD+=1
                        LC+=1
                        PE-=1
                        covid-=1

            if question_id =="cg3" :
                for answer_id in answer_id:
                    if answer_id == "Yes":
                        VB+=0.25
                        BP+=1
                        A+=0.25
                        CHF+=0.25
                        CLD+=0.5
                        LC+=0.5
                        PE+=0
                        covid+=0.5

            if question_id =="cg4":
                for answer_id in answer_id:
                    if answer_id == "Yes":
                        VB+=0.25
                        BP+=0.25
                        A+=0
                        CHF+=0.25
                        CLD+=0.5
                        LC+=1
                        PE+=1
                        covid+=0.5

            if question_id == "cg5":
                for answer_id in answer_id:
                    if answer_id == "Yes":
                        VB+=1
                        BP+=0.25
                        A+=0.25
                        CHF+=0
                        CLD+=0
                        LC+=0
                        PE+=0
                        covid+=1

            if question_id =="cg6":
                for answer_id in answer_id:
                    if answer_id == "Yes":
                        VB+=0
                        BP+=0.5
                        A+=0.5
                        CHF+=1
                        CLD+=1
                        LC+=0.5
                        PE+=1
                        covid+=0.5

            if question_id=="cg7":
                for answer_id in answer_id:
                    if answer_id == "Yes":
                        VB+=0.25
                        BP+=0.25
                        A+=0.25
                        CHF+=0.5
                        CLD+=0.25
                        LC+=0.5
                        PE+=1
                        covid+=0.5

            if question_id=="cg8":
                for answer_id in answer_id:
                    if answer_id == "Yes":
                        VB-=1
                        BP+=0.25
                        A+=0
                        CHF-=1
                        CLD+=0.75
                        LC+=1
                        PE-=1
                        covid-=1


            if question_id=="cg9":
                for answer_id in answer_id:
                    if answer_id == "Yes":
                        VB+=0.25
                        BP+=0.5
                        A+=0.5
                        CHF+=1
                        CLD+=1
                        LC+=1
                        PE+=1
                        covid-=0.5

            if question_id=="cg10":
                for answer_id in answer_id:
                    if answer_id == "Yes":
                        VB-=1
                        BP-=1
                        A-=1
                        CHF+=1
                        CLD-=1
                        LC-=1
                        PE-=1
                        covid-=1

            if question_id=="cg11":
                for answer_id in answer_id:
                    if answer_id == "Yes":
                        VB+=0.25
                        BP+=0.25
                        A-=1
                        CHF-=1
                        CLD-=1
                        LC-=1
                        PE-=1
                        covid+=1


        context ={

            "Viral_Bronchitis":VB,
            "Bacterial_Pneumonia":BP,
            "Asthma":A,
            "Chronic_Heart_Failure":CHF,
            "Chronic_Lung_Disease":CLD,
            "Lung_Cancer":LC,
            "Pleural_Embolism":PE,
            "covid":covid,

            # "Appendicitis":Appendicitis,
            # "Cholecystitis":Cholecystitis,
            # "Cystitis":Cystitis,
            # "Pyelonephritis":Pyelonephritis,
            # "Renal_Calculi":Renal_Calculi,
            # "Diverticulitis":Diverticulitis,
            # "Inflammatory_Bowel":Inflammatory_Bowel,
            # "Irritable_Bowel":Irritable_Bowel,
            # "Pancreatitis":Pancreatitis,
            # "Endometriosis":Endometriosis,
            # "Gastritis":Gastritis


        }
        print (context)
        x = sorted(((v,k) for k,v in context.items() if v > 0))
        print ("len of x",len(x))
        if len(x) == 0:
            context2 = {
                "Disease": "No disease found",

                }

            user_diesease_update = top_disease_user_overall.objects.create(analysistype="cough", disease1="Disease",p1="No disease found",last_date_of_analysis=datetime.datetime.now())
            user_diesease_update.save()
            request.session['Diagnosis']= "No disease"
            request.session['P1_score']= "0"
            request.session['Diagnosis_type']= "Cough"

            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id

            return render(request,"questionscompleted.html")

        if len(x) == 1:
            first_name = x[-1][1]
            first_value = x[-1][0]
            # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="cough", disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()


            context2 = {
                first_name: "Most Likely",

                }
            request.session['Diagnosis']= first_name
            request.session['P1_score']= first_value
            request.session['Diagnosis_type']= "Cough"



            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id
            request.session['detailed User message']= "Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined You are likely to have " + first_name + ". The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms."

            return render(request,"questionscompleted.html")

            return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

        if len(x) == 2:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            context2 = {
                first_name: "Most Likely",
                second_name :"Possible",
                }
            request.session['Diagnosis']= first_name
            request.session['P1_score']= first_value
            request.session['Diagnosis_type']= "Cough"

            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id
            request.session['detailed User message']= "Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined You are likely to have " + first_name + "," + second_name + ". The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms."


            return render(request,"questionscompleted.html")



        if len(x) == 3:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            third_name = x[-3][1]
            third_value = x[-3][0]
            # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            context2 = {
                first_name: "Most Likely",
                second_name :"Likely",
                third_name : "Possible",
                }
            request.session['Diagnosis']= first_name
            request.session['P1_score']= first_value
            request.session['Diagnosis_type']= "Cough"

            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id
            request.session['detailed User message']= "Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined You are likely to have " + first_name + " , " + second_name + " or " + third_name +  ". The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms."

            return render(request,"questionscompleted.html")


            # return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

        if len(x) > 3:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            third_name = x[-3][1]
            third_value = x[-3][0]
            fourth_name = x[-4][1]
            fourth_value = x[-4][0]
            # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            print("first_value",first_value)
            print("second_value",second_value)
            print("third_value",third_value)
            print("fourth_value",fourth_value)
            context2 = {
                first_name: "Most Likely",
                second_name :"Very Likely",
                third_name : "Likely",
                fourth_name : "Possible"

            }
            request.session['Diagnosis']= first_name
            request.session['P1_score']= first_value
            request.session['Diagnosis_type']= "Cough"

            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id
            request.session['detailed User message']= "Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined You are likely to have " + first_name + " , " + second_name + " or " + third_name +  ". The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms."

            return render(request,"questionscompleted.html")



def contactushome(request):
    if request.method =="GET":
        print ("In contact Us page get request")
        print ("data",request.GET)
        # name = request.GET["name"]

        # phone = request.GET["phone"]
        name = request.GET["name"]
        email1 = request.GET["email"]
        Number = request.GET["Number"]
        CountryName = request.GET["CountryName"]
        message = request.GET["message"]
        if len(name) == 0:
            return JsonResponse({"status":"name"})

        if len(email1) == 0:
            return JsonResponse({"status":"Error"})


        if len(message) == 0:
            return JsonResponse({"status":"message"})


        msz =  "Hi ApnaMd \n My name is {} and I'm from {} \n {} My contact are {} \ n {} ".format(name,CountryName,message,Number,email1)
        try :
            email = EmailMessage("Apna MD (AI Diagnosis)",msz,to=["aidev2@365cal.com"])
            email.send()
            return JsonResponse({"status":"sent"})
        except Exception as e:
            print ("Error in email exception",e)
            return JsonResponse({"status":"Error"})
    return render(request,"contactus_home.html")


def contactus_home(request):

    return render(request,"contactus_home.html")


@csrf_exempt
def google_login(request):
    # return render (request,"Authentication/Google_signin.html")
    return render (request,"Authentication/google_index.html")

@csrf_exempt
def depression_test(request):
    score=0
    if request.method=='POST':
        print("POST request accepeted and post data is", request.POST)

        try:
            dp1=request.POST['dq1']
            print("Your dp1 is", dp1)
        except:
            dp1 =" "
            pass

        try:
            dp2=request.POST['dq2']
            print("Your dp2 is", dp2)
        except:
            dp2 =" "
            pass

        try:
            dp3=request.POST['dq3']
            print("Your are dp3", dp3)
        except:
            dp3 =" "
            pass

        try:
            dp4=request.POST['dq4']
            print("Your are dp4", dp4)

        except:
            dp4 =" "
            pass

        try:
            dp5=request.POST['dq5']
            print("Your are dp5", dp5)
        except:
            dp5 =" "
            pass

        try:
            dp6=request.POST['dq6']
            print("Your are dp6", dp6)
        except:
            dp6 =" "
            pass

        try:
            dp7=request.POST['dq7']
            print("Your are dp7", dp7)
        except:
            dp7 =" "
            pass

        try:
            dp8 =request.POST['dq8']
            print("Your are dp8", dp8)
        except:
            dp8 =" "
            pass

        try:
            dp9 =request.POST['dq9']
            print("Your are dp9", dp9)
        except:
            dp9 =" "
            pass

        score=0

        if dp1=="Several days":
            score+=1
        if dp1=="More than half the days":
            score+=2
        if dp1=="Nearly every day":
            score+=3

        print("score is", score)

        if dp2=="Several days":
            score+=1
        if dp2=="More than half the days":
            score+=2
        if dp2=="Nearly every day":
            score+=3
        print("score is", score)

        if dp3=="Several days":
            score+=1
        if dp3=="More than half the days":
            score+=2
        if dp3=="Nearly every day":
            score+=3
        print("score is", score)

        if dp4=="Several days":
            score+=1
        if dp4=="More than half the days":
            score+=2
        if dp4=="Nearly every day":
            score+=3
        print("score is", score)

        if dp5=="Several days":
            score+=1
        if dp5=="More than half the days":
            score+=2
        if dp5=="Nearly every day":
            score+=3
        print("score is", score)

        if dp6=="Several days":
            score+=1
        if dp6=="More than half the days":
            score+=2
        if dp6=="Nearly every day":
            score+=3
        print("score is", score)

        if dp7=="Several days":
            score+=1
        if dp7=="More than half the days":
            score+=2
        if dp7=="Nearly every day":
            score+=3
        print("score is", score)

        if dp8=="Several days":
            score+=1
        if dp8=="More than half the days":
            score+=2
        if dp8=="Nearly every day":
            score+=3
        print("score is", score)

        if dp9=="Several days":
            score+=1
        if dp9=="More than half the days":
            score+=2
        if dp9=="Nearly every day":
            score+=3
        print("score is", score)


        score_data={
            "context1":score,
        }

        print("YOUR FINAL TOTAL SCORE IS", score)



        if score<4:
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="depression test",disease1="None", p1=score, last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # request.session['score']=round(score)
            request.session['overallDiagnosis']= "Your overall risk assessment is Normal"
            # request.session['user_diesease_update']=user_diesease_update.id
            request.session['Diagnosis']= "Normal"
            request.session['P1_score']= score
            request.session['Diagnosis_type']= "Depression"

            return render(request, "depression_result_updated.html")
            # return render(request,"depression_test_display.html",{"score_data":score_data, 'Risk_Assessment' : "Your overall risk assessment for depression is Normal"})

        if score>=5 and score<=9:
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="depression test",disease1="Mild", p1=score, last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # request.session['score']=round(score)
            request.session['overallDiagnosis']= "Your overall risk assessment is Mild"
            # request.session['user_diesease_update']=user_diesease_update.id
            request.session['Diagnosis']= "Mild"
            request.session['P1_score']= score
            request.session['Diagnosis_type']= "Depression"

            return render(request, "depression_result_updated.html")
            # return render(request,"depression_test_display.html",{"score_data":score_data, 'Risk_Assessment' : "Your overall risk assessment for depression is Mild"})

        if score>=10 and score<=14:
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="depression test",disease1="Moderate", p1=score, last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # request.session['score']=round(score)
            request.session['overallDiagnosis']= "Your overall risk assessment is Moderate"
            # request.session['user_diesease_update']=user_diesease_update.id
            request.session['Diagnosis']= "Moderate"
            request.session['P1_score']= score
            request.session['Diagnosis_type']= "Depression"

            return render(request, "depression_result_updated.html")
            # return render(request,"depression_test_display.html",{"score_data":score_data, 'Risk_Assessment' : "Your overall risk assessment for depression is Moderate"})

        if score>=15 and score<=19:
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="depression test",disease1="Moderately severe", p1=score, last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # request.session['score']=round(score)
            request.session['overallDiagnosis']= "Your overall risk assessment is Moderately severe"
            # request.session['user_diesease_update']=user_diesease_update.id
            request.session['Diagnosis']= "severe"
            request.session['P1_score']= score
            request.session['Diagnosis_type']= "Depression"

            return render(request, "depression_result_updated.html")
            # return render(request,"depression_test_display.html",{"score_data":score_data, 'Risk_Assessment' : "Your overall risk assessment for depression is Moderately severe"})

        if score>=20 and score<=27:
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="depression test",disease1="Severe", p1=score, last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # request.session['score']=round(score)
            request.session['overallDiagnosis']= "Your overall risk assessment is Severe"
            # request.session['user_diesease_update']=user_diesease_update.id
            request.session['Diagnosis']= "Severe"
            request.session['P1_score']= score
            request.session['Diagnosis_type']= "Depression"

            return render(request, "depression_result_updated.html")
            # return render(request,"depression_test_display.html",{"score_data":score_data, 'Risk_Assessment' : "Your overall risk assessment for depression is Severe"})



    return render(request,"depressionTest.html")


def depression_optverification(request):

    return render(request, "otpcode_Depression.html")



def resendotp_depression(request):
    try :

        otp = random.randint (1000,9999)
        request.session['otp']=otp
        account_sid = "AC933127d38ff7d1939cc865520fff97cf"

        # Your Auth Token from twilio.com/console
        auth_token  = "69196d7c514f51c4c7733b4afb4c57e6"

        otp = request.session.get('otp')
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to=request.session.get('otpnumber'),
            from_="+18508212276",
            body=f'Your OTP verification number is {otp}')
        html = render_to_string('otpcode_Depression.html')
        print ("messgae sid",message.sid )
        return render(request,"otpcode_Depression.html")
    except Exception as e:
        print ("Error",e)
        return JsonResponse({"status":"Error"})



@csrf_exempt
def sendotp_depression(request):
    if request.method =="GET":

        print ("data",request.GET)
        otpnumber = request.GET["num"]
        request.session['otpnumber']=otpnumber



        # otpnumber=request.session.get('otpnumber')
        print("your otp number is",otpnumber)
        user_diesease_update = request.session.get('user_diesease_update')
        Depression_Diagnosis = request.session.get('Diagnosis')
            # Score_obtained= request.session.get('score')


        try :

            print("You have entered in try method")

            account_sid = "AC933127d38ff7d1939cc865520fff97cf"

            # Your Auth Token from twilio.com/console
            auth_token  = "69196d7c514f51c4c7733b4afb4c57e6"

            client = Client(account_sid, auth_token)

            message = client.messages.create(
                to=request.session.get('otpnumber'),
                from_="+18508212276",
                body=f'{Depression_Diagnosis}' )
            # html = render_to_string('otpcode_Depression.html')
            print ("messgae sid",message.sid )

            # numberdatsave =  number_with_topdisease.objects.create(phonenumber=request.session.get('otpnumber'),topdisease=user_diesease_update)
            # numberdatsave.save()
            # newnumbers_store =  newnumbers.objects.create(number=request.session.get('otpnumber'),create_Date= datetime.datetime.now())
            # newnumbers_store.save()


            return JsonResponse({"status":"sent"})
        except Exception as e:
            print ("Error",e)
            return JsonResponse({"status":"Error"})


    return render(request,"depression_result_updated.html")


def depression_thanks(request):
    if request.user.is_authenticated:
        usr = request.user
        email1 = usr.email
        Depression_Diagnosis = request.session.get('overallDiagnosis')

        # user_diesease_update = top_disease_user_overall_with_user.objects.create(analysistype=request.session.get('Diagnosis_type'),disease1=request.session.get('Diagnosis'), p1=request.session.get('P1_score'),email=email1,verified="Yes",userfrom="Web Application", last_date_of_analysis=datetime.datetime.now())
        # user_diesease_update.save()
        details_overall = request.session.get('detailed User message')

        msz =  "Hi there,Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined Your Diagnosis: {} \n The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms. \n Our most commonly visited symptoms are chest pain (https://www.apnamd.ai/ChestPain/ ) and depression (https://www.apnamd.ai/Depression/Test/). \n Kind Regards \n ApnaMD Team ".format(Depression_Diagnosis)

        email = EmailMessage("Apna MD (AI Diagnosis)",msz,to=[email1])
        email.send()
        # newemails_store =  newemails.objects.create(email=email1,create_Date= datetime.datetime.now())
        # newemails_store.save()

    return render(request,"afterverification_depression.html")


def Depression_contactus(request):
    global context
    print ("In contact Us page")
    if request.method =="GET":
        print ("In contact Us page get request")
        print ("data",request.GET)
        # name = request.GET["name"]

        # phone = request.GET["phone"]
        email1 = request.GET["email"]
        # message = request.GET["discription"]


        user_diesease_update = request.session.get('user_diesease_update')
        Depression_Diagnosis = request.session.get('overallDiagnosis')
        print ("user_diesease_update",user_diesease_update)



        if len(email1) == 0:
            return JsonResponse({"status":"Error"})


        msz =  "Hi there,Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined Your Diagnosis: {} \n The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms. \n Our most commonly visited symptoms are chest pain (https://www.apnamd.ai/ChestPain/ ) and depression (https://www.apnamd.ai/Depression/Test/). \n Kind Regards \n ApnaMD Team ".format(Depression_Diagnosis)
        try :
            email = EmailMessage("Apna MD (AI Diagnosis)",msz,to=[email1])
            email.send()
            # newemails_store =  newemails.objects.create(email=email1,create_Date= datetime.datetime.now())
            # newemails_store.save()
            # user_diesease_update = top_disease_user_overall_with_user.objects.create(analysistype=request.session.get('Diagnosis_type'),disease1=request.session.get('Diagnosis'), p1=request.session.get('P1_score'),email=email1,verified="No",userfrom="Web Application", last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()


            return JsonResponse({"status":"sent"})
        except Exception as e:
            print ("Error in email exception",e)
            return JsonResponse({"status":"Error"})

    return redirect("HOME")




def generalthankupage(request):
    if request.user.is_authenticated:
        usr = request.user
        email1 = usr.email

        # user_diesease_update = top_disease_user_overall_with_user.objects.create(analysistype=request.session.get('Diagnosis_type'),disease1=request.session.get('Diagnosis'), p1=request.session.get('P1_score'),email=email1,verified="Yes",userfrom="Web Application", last_date_of_analysis=datetime.datetime.now())
        # user_diesease_update.save()
        details_overall = request.session.get('detailed User message')

        msz =  " Hi there, {} \n Our most commonly visited symptoms are chest pain (https://www.apnamd.ai/_2_CVD_cal/ ) and depression (https://www.apnamd.ai/Depression/Test/). \n Kind Regards \n ApnaMD Team ".format(details_overall)

        email = EmailMessage("Apna MD (AI Diagnosis)",msz,to=[email1])
        email.send()
        # newemails_store =  newemails.objects.create(email=email1,create_Date= datetime.datetime.now())
        # newemails_store.save()

    return render(request,"generalthankupage.html")


def general_optverification(request):
    return render(request, "General_otpcode.html")



def general_email(request):
    if request.method =="GET":
        print ("In contact Us page get request")
        print ("data",request.GET)
        # name = request.GET["name"]

        # phone = request.GET["phone"]
        email1 = request.GET["email"]
        # message = request.GET["discription"]

        details = request.session.get('General Details')
        print ("details",details)
        details_id = request.session.get('General Details id')
        print ("details_id",details_id)
        details_overall = request.session.get('detailed User message')


        if len(email1) == 0:
            return JsonResponse({"status":"Error"})


        msz =  " Hi there, {} \n Our most commonly visited symptoms are chest pain (https://www.apnamd.ai/_2_CVD_cal/ ) and depression (https://www.apnamd.ai/Depression/Test/). \n Kind Regards \n ApnaMD Team ".format(details_overall)
        try :
            email = EmailMessage("Apna MD (AI Diagnosis)",msz,to=[email1])
            email.send()
            # newemails_store =  newemails.objects.create(email=email1,create_Date= datetime.datetime.now())
            # newemails_store.save()
            # user_diesease_update = top_disease_user_overall_with_user.objects.create(analysistype=request.session.get('Diagnosis_type'),disease1=request.session.get('Diagnosis'), p1=request.session.get('P1_score'),email=email1,verified="No",userfrom="Web Application", last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()


            return JsonResponse({"status":"sent"})
        except Exception as e:
            print ("Error in email exception",e)
            return JsonResponse({"status":"Error"})



def General_resendotp(request):
    try :

        otp = random.randint (1000,9999)
        request.session['otp']=otp
        account_sid = "AC933127d38ff7d1939cc865520fff97cf"

        # Your Auth Token from twilio.com/console
        auth_token  = "69196d7c514f51c4c7733b4afb4c57e6"

        client = Client(account_sid, auth_token)
        otp = request.session.get('otp')
        message = client.messages.create(
            to=request.session.get('otpnumber'),
            from_="+18508212276",
            body=f'Here is your otp {otp}')
        html = render_to_string('General_otpcode.html')
        print ("messgae sid",message.sid )
        return render(request,"General_otpcode.html")
    except Exception as e:
        print ("Error",e)
        return JsonResponse({"status":"Error"})



@csrf_exempt
def General_sendotp(request):
    if request.method =="GET":
        print ("data",request.GET)
        try :
            otpnumber = request.GET["num"]
            request.session['otpnumber']=otpnumber
            # check = verifiednumbers.objects.filter(number=otpnumber)
            details_overall = request.session.get('detailed User message')
            print ("check",check)

            print ("data",request.session.get('General Details'))
            details = request.session.get('General Details')
            print ("details",details)
            details_id = request.session.get('General Details id')
            print ("details_id",details_id)

            print (type(details))
            print ("Details",(details))
            try :

                account_sid = "AC933127d38ff7d1939cc865520fff97cf"

                # Your Auth Token from twilio.com/console
                auth_token  = "69196d7c514f51c4c7733b4afb4c57e6"

                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    to=request.session.get('otpnumber'),
                    from_="+18508212276",
                    body=f'{details_overall}')
                html = render_to_string('General_otpcode.html')
                print ("messgae sid",message.sid )

                # numberdatsave =  number_with_topdisease.objects.create(phonenumber=request.session.get('otpnumber'),topdisease=details_id)
                # numberdatsave.save()
                # newnumbers_store =  newnumbers.objects.create(number=request.session.get('otpnumber'),create_Date= datetime.datetime.now())
                # newnumbers_store.save()

                return JsonResponse({"status":"sent"})
            except Exception as e:
                print ("Error",e)
                return JsonResponse({"status":"Error"})




        except Exception as e:
            print ("Error",e)
            return JsonResponse({"status":"Error"})

    return render(request,"General_otpcode.html")


def otp_verification_diabetes_complications(request):

    return render (request,"otpcode_diabetes_complications.html")


def resendotp_diabetes_complications(request):
    try :
        otp = random.randint (1000,9999)
        request.session['otp']=otp
        account_sid = "AC933127d38ff7d1939cc865520fff97cf"

        # Your Auth Token from twilio.com/console
        auth_token  = "69196d7c514f51c4c7733b4afb4c57e6"
        otp = request.session.get('otp')
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to=request.session.get('otpnumber'),
            from_="+18508212276",
            body=f'Your OTP verification number is {otp}')
        html = render_to_string('otpcode_diabetes_complications.html')
        print ("messgae sid",message.sid )
        return render(request,"otpcode_diabetes_complications.html")
    except Exception as e:
        print ("Error",e)
        return JsonResponse({"status":"Error"})


def email_diabetes_complications(request):
    if request.method =="GET":
        print ("In contact Us page get request")
        print ("data",request.GET)
        # name = request.GET["name"]

        # phone = request.GET["phone"]
        email1 = request.GET["email"]
        # message = request.GET["discription"]

        user_diesease_update = request.session.get('user_diesease_update')
        overall_risk = request.session.get('OverallRisk')
        Heart_attack= request.session.get('HeartAttack')
        Heart_failure= request.session.get('HeartFailure')
        Kidney_failure= request.session.get('KidneyFailure')


        if len(email1) == 0:
            return JsonResponse({"status":"Error"})


        msz =  "{}\n Your risk of heart attacks in 10 years is {}% \n Your risk of heart failure in 10 years is {} % \n Your risk of kidney failure in 10 years is {} % \n Contact us for a free AI monitoring program of your Diabetes.".format(overall_risk,Heart_attack,Heart_failure,Kidney_failure)
        try :
            email = EmailMessage("Apna MD (AI Diagnosis)",msz,to=[email1])
            email.send()
            # newemails_store =  newemails.objects.create(email=email1,create_Date= datetime.datetime.now())
            # newemails_store.save()

            return JsonResponse({"status":"sent"})
        except Exception as e:
            print ("Error in email exception",e)
            return JsonResponse({"status":"Error"})




@csrf_exempt
def sendotp_diabetes_complications(request):
    if request.method =="GET":

        print ("data",request.GET)
        try :
            otpnumber = request.GET["num"]
            request.session['otpnumber']=otpnumber

            user_diesease_update = request.session.get('user_diesease_update')
            overall_risk = request.session.get('OverallRisk')
            Heart_attack= request.session.get('HeartAttack')
            Heart_failure= request.session.get('HeartFailure')
            Kidney_failure= request.session.get('KidneyFailure')

            try :
                account_sid = "AC933127d38ff7d1939cc865520fff97cf"
                auth_token  = "69196d7c514f51c4c7733b4afb4c57e6"
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                    to=request.session.get('otpnumber'),
                    from_="+18508212276",
                    body=f'{overall_risk} \n Your risk of heart attacks in 10 years is {Heart_attack} % \n Your risk of heart failure in 10 years is {Heart_failure} % \n Your risk of kidney failure in 10 years is {Kidney_failure} % \n Contact us for a free AI monitoring program of your Diabetes.')
                # numberdatsave =  number_with_topdisease.objects.create(phonenumber=request.session.get('otpnumber'),topdisease=user_diesease_update)
                # numberdatsave.save()
                # newnumbers_store =  newnumbers.objects.create(number=request.session.get('otpnumber'),create_Date= datetime.datetime.now())
                # newnumbers_store.save()


                return JsonResponse({"status":"sent"})
            except Exception as e:
                print ("Error",e)
                return JsonResponse({"status":"sent"})
        except Exception as e:
            print ("Error",e)
            return JsonResponse({"status":"Error"})

    return render(request,"otpcode_diabetes_complications.html")


def afterverification_thankyou(request):

    return render (request,"afterverification_thankyou.html")

@csrf_exempt
def Diabetes_complications(request):

    if request.method=='GET':
       return render(request,"diabetes_risk.html")
    if request.method=='POST':
        print("POST request accepeted and post data is", request.POST)
        updated_data= dict(request.POST.lists())
        try:
            Age=request.POST['age']

            print("Your age is", Age)
        except:
            Age =" "
            pass

        try:
            Gender=request.POST['gender']
            print("Your gender is", Gender)
        except:
            Gender =" "
            pass



        try :
            BMI_data=updated_data['bmi[]']

            print("Your BMI_data is", BMI_data)
            print("Your BMI_data weight is ", BMI_data[0])
            print("Your BMI_data height is ", BMI_data[1])
            weight= BMI_data[0]
            height= BMI_data[1]
            height_in_meter = round((int(height)/100),2)
            print ("height_in_meter",height_in_meter)
            BMI = round((int(weight) / (height_in_meter * height_in_meter)),2)
            print("Your calculated BMI is", BMI)
        except:
            BMI = 0
            pass


        try:
            Race=request.POST['race']
            print("Your Race is", Race)
        except:
            Race =" "
            pass

        try:
            Smoke=request.POST['smoke']
            print("Your Smoke is", Smoke)
        except:
            Smoke =" "
            pass

        try:

            History=updated_data['history[]']
            print("Your History is", History)
        except:
            History =" "
            pass

        try:
            hb=request.POST['Hb']
            print("Your hb is", hb)
        except:
            hb =" "
            pass

        try:
            BP=request.POST['systolicBlood']
            print("Your BP is", BP)
        except:
            BP =" "
            pass

        try:
            Creatinine=request.POST['creatinine']
            print("Your creatinine is", Creatinine)
        except:
            Creatinine =" "
            pass

        try:
            Cholesterol=request.POST['cholesterol']
            print("Your cholesterol is", Cholesterol)
        except:
            Cholesterol =" "
            pass

        try:
            Medications=request.POST.getlist('medications[]')
            print("Your current_Medi is", Medications)
            print(type(Medications))
        except:
            Medications =" "
            pass
        score=0

        if Age=='Under 35 years':
            score+=0.9
        if Age=='35-44 years':
            score+=1.8
        if Age=='45-54 years':
            score+=2.7
        if Age=='55-64 years':
            score+=3.6
        if Age=='65 years or Over':
            score+=4.5
        if Gender=='Male':
            score+=9
        if Gender=='Female':
            score+=0
        if BMI>30:
            score+=0.7
        if Race=='Indian':
            score+=0.2
        if Race=='Asian':
            score+=0.1
        if Smoke=='Current':
            score+=2.3
        if History=='Hypertension':
            score+=0.5
        if History!='High Cholesterol':
            score+=0.3
        if History!='Heart Disease':
            score+=2.9
        if History!='Strokes':
            score+=0.4
        if History!='Kidney Disease':
            score+=0.8
        if hb=='Greater than 7':
            score+=2.2
        if BP=='141-160':
            score+=0.1
        if BP=='161 and above':
            score+=0.1
        if Creatinine=='Greater than 1.5':
            score+=0.8
        if Cholesterol=='Greater than 5':
            score+=0.3

        if 'Insulin' not in Medications:
            print("current_Medi1 is executed")
            score+=0.4
        for current_Medi in Medications:
            print("current_Medi ", current_Medi)

            if current_Medi=='Other diabetes medication (non insulin)':
                score+=1.5
            if current_Medi=='Cholesterol Tablets (Lipid Lowering medications)':
                score+=0.1
            if current_Medi=='Heart Tablets':
                score+=0.2
            if current_Medi=='Aspirin':
                score+=4.3

        score_data={
            "context1":round(score,2),
        }
        print("Total score obtained for heart attack is",score)
        score_diff= score-5

        #### Heart Failure Risk####

        score1=0

        if Age=='Under 35 years':
            score1+=1.44
        if Age=='35-44 years':
            score1+=2.88
        if Age=='45-54 years':
            score1+=4.32
        if Age=='55-64 years':
            score1+=5.76
        if Age=='65 years or Over':
            score1+=7.2
        if Gender=='Male':
            score1+=0.7
        if Gender=='Female':
            score1+=0
        if BMI>30:
            score1+=6.4
        if Race=='Indian':
            score1+=0.4
        if Race=='Asian':
            score1+=0.2
        if Smoke=='Current':
            score1+=0.7
        if History=='Hypertension':
            score1+=0.2
        if History!='High Cholesterol':
            score1+=0.4
        if History!='Heart Disease':
            score1+=0.5
        if History!='Strokes':
            score1+=0.2
        if History!='Kidney Disease':
            score1+=0.4
        if hb=='Greater than 7':
            score1+=5.4
        if BP=='141-160':
            score1+=2.8
        if BP=='161 and above':
            score1+=2.8
        if Creatinine=='Greater than 1.5':
            score1+=0.4
        if Cholesterol=='Greater than 5':
            score1+=0.4

        if 'Insulin' not in Medications:
            print("current_Medi1 is executed")
            score1+=0.6
        for current_Medi in Medications:
            print("current_Medi ", current_Medi)

            if current_Medi=='Other diabetes medication (non insulin)':
                score1+=2.2
            if current_Medi=='Cholesterol Tablets (Lipid Lowering medications)':
                score1+=0.2
            if current_Medi=='Heart Tablets':
                score1+=0
            if current_Medi=='Aspirin':
                score1+=0.5

        score_data1={
            "context2":round(score1,2),
        }
        print("Total score obtained for heart failure is",score1)

        score_diff1= score1-2


    #### Kidney Failure risk ####


        score2=0

        if Age=='Under 35 years':
            score2+=0.36
        if Age=='35-44 years':
            score2+=0.72
        if Age=='45-54 years':
            score2+=1.08
        if Age=='55-64 years':
            score2+=1.44
        if Age=='65 years or Over':
            score2+=1.8
        if Gender=='Male':
            score2+=0.1
        if Gender=='Female':
            score2+=0
        if BMI>30:
            score2+=0.1
        if Race=='Indian':
            score2+=0.1
        if Race=='Asian':
            score2+=0.05
        if Smoke=='Current':
            score2+=0.1
        if History=='Hypertension':
            score2+=0.2
        if History!='High Cholesterol':
            score2+=0.2
        if History!='Heart Disease':
            score2+=0.5
        if History!='Strokes':
            score2+=0.2
        if History!='Kidney Disease':
            score2+=7.5
        if hb=='Greater than 7':
            score2+=0.2
        if BP=='141-160':
            score2+=0.3
        if BP=='161 and above':
            score2+=0.3
        if Creatinine=='Greater than 1.5':
            score2+=7.5
        if Cholesterol=='Greater than 5':
            score2+=0.2

        print(" Type of current_Medi is", type(Medications))

        if 'Insulin' not in Medications:
            print("current_Medi1 is executed")
            score2+=0.2
        for current_Medi in Medications:
            print("current_Medi ", current_Medi)

            if current_Medi=='Other diabetes medication (non insulin)':
                print("current_Medi2 is executed")
                score2+=0.1
            if current_Medi=='Cholesterol Tablets':
                print("current_Medi3 is executed")
                score2+=0.2
            if current_Medi=='Heart Tablets':
                print("current_Medi4 is executed")
                score2+=0.2
            if current_Medi=='Aspirin':
                print("current_Medi5 is executed")
                score2+=0

        score_data2={
            "context3":round(score2,2),
        }
        print("Total score obtained for Kidney failure is",score2)

        score_diff2= score2-8


        Total_score_difference= score_diff+score_diff1+score_diff2
        print("Your final assesment score is ",Total_score_difference )

        request.session['HeartAttack']=round(score,2)
        request.session['HeartFailure']=round(score1,2)
        request.session['KidneyFailure']=round(score2,2)
        if Total_score_difference<11:
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Diabetes Complications",disease1="Low Risk", p1=Total_score_difference, last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            request.session['OverallRisk']= "Your overall risk assessment is LOW"
            request.session['user_diesease_update']=user_diesease_update.id
            return render(request, "Diabetes_risk_complex_display.html", {'Risk_Assessment' : "Our AI Diagnostic Assessment had indicated that your risk of complications due to diabetes is LOW" })
        if Total_score_difference>=11 and Total_score_difference<32:
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Diabetes Complications",disease1="Intermediate Risk", p1=Total_score_difference, last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            request.session['OverallRisk']= "Your overall risk assessment is INTERMEDIATE"
            request.session['user_diesease_update']=user_diesease_update.id
            return render(request, "Diabetes_risk_complex_display.html", {'Risk_Assessment' : "Our AI Diagnostic Assessment had indicated that your risk of complications due to diabetes is INTERMEDIATE" })
        if Total_score_difference>=32:
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Diabetes Complications",disease1="High Risk", p1=Total_score_difference, last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            request.session['OverallRisk']= "Your overall risk assessment is HIGH"
            request.session['user_diesease_update']=user_diesease_update.id
            return render(request, "Diabetes_risk_complex_display.html", {'Risk_Assessment' : "Our AI Diagnostic Assessment had indicated that your risk of complications due to diabetes is HIGH" })


    return render(request,"diabetes_risk.html")





def DiabetesRiskform(request):

    return render (request,"DiabetesRiskform_home.html")


def DiabetesForm(request):

    return render (request,"diabates_home.html")





def optverification(request):

    return render (request,"otpcode.html")





def resendotp(request):

    try :

        otp = random.randint (1000,9999)
        request.session['otp']=otp
        account_sid = "AC933127d38ff7d1939cc865520fff97cf"

        # Your Auth Token from twilio.com/console
        auth_token  = "69196d7c514f51c4c7733b4afb4c57e6"
        otp = request.session.get('otp')
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to=request.session.get('otpnumber'),
            from_="+18508212276",
            body=f'Here is your otp {otp}')
        html = render_to_string('otpcode.html')
        print ("messgae sid",message.sid )
        return render(request,"otpcode.html")
    except Exception as e:
        print ("Error",e)
        return JsonResponse({"status":"Error"})


@csrf_exempt
def sendotp(request):

    if request.method =="GET":

        print ("data",request.GET)
        try :
            details = request.session.get('details')[0]
            user_diesease_update = request.session.get('user_diesease_update')
            print ("user_diesease_update",user_diesease_update)
            print (type(details))
            print ("Details",(details))
            score = details['score']
            data = details['data']

            otpnumber = request.GET["num"]
            request.session['otpnumber']=otpnumber
            otp = random.randint (1000,9999)
            request.session['otp']=otp
            account_sid = "AC933127d38ff7d1939cc865520fff97cf"

            # Your Auth Token from twilio.com/console
            auth_token  = "69196d7c514f51c4c7733b4afb4c57e6"
            otp = request.session.get('otp')
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                to=request.session.get('otpnumber'),
                from_="+18508212276",
                body=f'Here is your total score {score} \n {data}')
            # numberdatsave =  number_with_topdisease.objects.create(phonenumber=request.session.get('otpnumber'),topdisease=user_diesease_update)
            # numberdatsave.save()
            # newnumbers_store =  newnumbers.objects.create(number=request.session.get('otpnumber'),create_Date= datetime.datetime.now())
            # newnumbers_store.save()

            return JsonResponse({"status":"sent"})
        except Exception as e:
            print ("Error",e)
            return JsonResponse({"status":"Error"})

    return render(request,"index.html")


def thanku_diabetes(request):
    if request.user.is_authenticated:
        usr = request.user
        email1 = usr.email
        details = request.session.get('details')[0]
        user_diesease_update = request.session.get('user_diesease_update')
        print ("user_diesease_update",user_diesease_update)
        print (type(details))
        print ("Details",(details))
        score = details['score']
        data = details['data']
        # user_diesease_update = top_disease_user_overall_with_user.objects.create(analysistype=request.session.get('Diagnosis_type'),disease1=request.session.get('Diagnosis'), p1=request.session.get('P1_score'),email=email1,verified="Yes",userfrom="Web Application", last_date_of_analysis=datetime.datetime.now())
        # user_diesease_update.save()


        msz =  " Hi there,Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined Here is your total score {}. {} \n The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses.Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms. \n  Our most commonly visited symptoms are chest pain (https://www.apnamd.ai/ChestPain/ ) and depression (https://www.apnamd.ai/Depression/Test/). \n Kind Regards \n ApnaMD Team".format(score,data)

        email = EmailMessage("Apna MD (AI Diagnosis)",msz,to=[email1])
        email.send()
        # newemails_store =  newemails.objects.create(email=email1,create_Date= datetime.datetime.now())
        # newemails_store.save()

    return render (request,"afterverification_diabetes_risk.html")


def diabetes_email(request):
    if request.method =="GET":
        print ("In contact Us page get request")
        print ("data",request.GET)
        # name = request.GET["name"]

        # phone = request.GET["phone"]
        email1 = request.GET["email"]
        # message = request.GET["discription"]

        details = request.session.get('details')[0]
        user_diesease_update = request.session.get('user_diesease_update')
        print ("user_diesease_update",user_diesease_update)
        print (type(details))
        print ("Details",(details))
        score = details['score']
        data = details['data']
        # user_diesease_update = top_disease_user_overall_with_user.objects.create(analysistype=request.session.get('Diagnosis_type'),disease1=request.session.get('Diagnosis'), p1=request.session.get('P1_score'),email=email1,verified="Yes",userfrom="Web Application", last_date_of_analysis=datetime.datetime.now())
        # user_diesease_update.save()



        if len(email1) == 0:
            return JsonResponse({"status":"Error"})


        msz =  " Hi there,Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined Here is your total score {}. {} \n The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses.Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms. \n  Our most commonly visited symptoms are chest pain (https://www.apnamd.ai/ChestPain/ ) and depression (https://www.apnamd.ai/Depression/Test/). \n Kind Regards \n ApnaMD Team".format(score,data)
        try :
            email = EmailMessage("Apna MD (AI Diagnosis)",msz,to=[email1])
            email.send()
            # newemails_store =  newemails.objects.create(email=email1,create_Date= datetime.datetime.now())
            # newemails_store.save()
            # user_diesease_update = top_disease_user_overall_with_user.objects.create(analysistype=request.session.get('Diagnosis_type'),disease1=request.session.get('Diagnosis'), p1=request.session.get('P1_score'),email=email1,verified="No",userfrom="Web Application", last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()


            return JsonResponse({"status":"sent"})
        except Exception as e:
            print ("Error in email exception",e)
            return JsonResponse({"status":"Error"})



@csrf_exempt
def cough_check(request):
    if request.method == 'GET':
        # questions = cough_questions.objects.all()
        final_data1=[]
        for l in questions:
            options=[]
            # all_option=cough_options_questions.objects.filter(question=l.id)
            for data in all_option:
                options.append({
                    "options_data":data.option1,
                })
            if l.id == 1:
                final_data1.append({
                            "question_data":l.Question,
                            "question_id":l.id,
                            "MultiValue":True,
                            "option":options,


                        })
            else:
                final_data1.append({
                            "question_data":l.Question,
                            "question_id":l.id,
                            "MultiValue":False,
                            "option":options,

                        })
        return render(request,"cough_jotform.html")
    if request.method == 'POST':
        print('POST', request.POST)
        print('BODY', request.body)
        post_data = dict(request.POST.lists())
        VB=0
        BP=0
        A=0
        CHF=0
        CLD=0
        LC=0
        PE=0
        covid=0
        context1 ={

            "Viral_Bronchitis":VB,
            "Bacterial_Pneumonia":BP,
            "Asthma":A,
            "Chronic_Heart_Failure":CHF,
            "Chronic_Lung_Disease":CLD,
            "Lung_Cancer":LC,
            "Pleural_Embolism":PE,
            "covid":covid
        }
        print ("context1",context1)
        for question_id in post_data:
            print ("key",question_id)
            print ("value",post_data[question_id])
            answer_id = post_data[question_id]
            if question_id == "1[]":
                for answer_id in answer_id:
                    print ("answer_id",answer_id)
                    if answer_id=="Asthma":
                        VB+=0
                        BP+=0
                        A+=1
                        CHF+=0.25
                        CLD+=0.25
                        LC+=0
                        PE+=0
                    if answer_id=="Heart disease":
                        VB+=0
                        BP+=0
                        A+=0.5
                        CHF+=1
                        CLD+=0.5
                        LC+=0
                        PE+=0
                    if answer_id=="Lung disease":
                        VB+=0
                        BP+=0.5
                        A+=0.5
                        CHF+=0.5
                        CLD+=1
                        LC+=0
                        PE+=0
                    if answer_id=="Clots in the body":
                        VB+=0
                        BP+=0
                        A+=0
                        CHF+=0
                        CLD+=0
                        LC+=0
                        PE+=1
                    if answer_id=="Allergies":
                        VB+=0
                        BP+=0
                        A+=1
                        CHF+=0
                        CLD+=0
                        LC+=0
                        PE+=0
                    if answer_id=="Smoking":
                        VB+=0.5
                        BP+=0.5
                        A+=0.5
                        CHF+=0.5
                        CLD+=0.5
                        LC+=1
                        PE+=0
                    if answer_id=="COVID":
                        VB+=0.25
                        BP+=0.5
                        A+=0.5
                        CHF+=0.25
                        CLD+=1
                        LC+=0
                        PE+=0.5

            if question_id == "2":
                for answer_id in answer_id:
                    if answer_id == "Less than 1 week":
                        VB+=1
                        BP+=0.25
                        A+=0.25
                        CHF-=1
                        CLD-=1
                        LC-=1
                        PE+=1
                        covid+=1
                    if answer_id == "Less than 1 month":
                        VB-=0.5
                        BP+=1
                        A+=0.5
                        CHF+=0.25
                        CLD-=1
                        LC+=0.5
                        PE+=0.5
                        covid+=0.75
                    if answer_id == "More than 1 month":
                        VB-=1
                        BP+=0.25
                        A+=0.75
                        CHF+=1
                        CLD+=1
                        LC+=1
                        PE-=1
                        covid-=1

            if question_id =="3" :
                for answer_id in answer_id:
                    if answer_id == "Yes":
                        VB+=0.25
                        BP+=1
                        A+=0.25
                        CHF+=0.25
                        CLD+=0.5
                        LC+=0.5
                        PE+=0
                        covid+=0.5

            if question_id =="4":
                for answer_id in answer_id:
                    if answer_id == "Yes":
                        VB+=0.25
                        BP+=0.25
                        A+=0
                        CHF+=0.25
                        CLD+=0.5
                        LC+=1
                        PE+=1
                        covid+=0.5

            if question_id == "5":
                for answer_id in answer_id:
                    if answer_id == "Yes":
                        VB+=1
                        BP+=0.25
                        A+=0.25
                        CHF+=0
                        CLD+=0
                        LC+=0
                        PE+=0
                        covid+=1

            if question_id =="6":
                for answer_id in answer_id:
                    if answer_id == "Yes":
                        VB+=0
                        BP+=0.5
                        A+=0.5
                        CHF+=1
                        CLD+=1
                        LC+=0.5
                        PE+=1
                        covid+=0.5

            if question_id=="7":
                for answer_id in answer_id:
                    if answer_id == "Yes":
                        VB+=0.25
                        BP+=0.25
                        A+=0.25
                        CHF+=0.5
                        CLD+=0.25
                        LC+=0.5
                        PE+=1
                        covid+=0.5

            if question_id=="8":
                for answer_id in answer_id:
                    if answer_id == "Yes":
                        VB-=1
                        BP+=0.25
                        A+=0
                        CHF-=1
                        CLD+=0.75
                        LC+=1
                        PE-=1
                        covid-=1


            if question_id=="9":
                for answer_id in answer_id:
                    if answer_id == "Yes":
                        VB+=0.25
                        BP+=0.5
                        A+=0.5
                        CHF+=1
                        CLD+=1
                        LC+=1
                        PE+=1
                        covid-=0.5

            if question_id=="10":
                for answer_id in answer_id:
                    if answer_id == "Yes":
                        VB-=1
                        BP-=1
                        A-=1
                        CHF+=1
                        CLD-=1
                        LC-=1
                        PE-=1
                        covid-=1

            if question_id=="11":
                for answer_id in answer_id:
                    if answer_id == "Yes":
                        VB+=0.25
                        BP+=0.25
                        A-=1
                        CHF-=1
                        CLD-=1
                        LC-=1
                        PE-=1
                        covid+=1


        context ={

            "Viral_Bronchitis":VB,
            "Bacterial_Pneumonia":BP,
            "Asthma":A,
            "Chronic_Heart_Failure":CHF,
            "Chronic_Lung_Disease":CLD,
            "Lung_Cancer":LC,
            "Pleural_Embolism":PE,
            "covid":covid
        }
        print (context)
        x = sorted(((v,k) for k,v in context.items() if v > 0))
        print ("len of x",len(x))
        if len(x) == 0:
            context2 = {
                "Disease": "No disease found",

                }
            user_diesease_update = top_disease_user_overall.objects.create(analysistype="cough", disease1="Disease",p1="No disease found",last_date_of_analysis=datetime.datetime.now())
            user_diesease_update.save()
            request.session['Diagnosis']= "No disease"
            request.session['P1_score']= "0"
            request.session['Diagnosis_type']= "Cough"

            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id

            return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

        if len(x) == 1:
            first_name = x[-1][1]
            first_value = x[-1][0]
            # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="cough", disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()


            context2 = {
                first_name: "Most Likely",

                }
            request.session['Diagnosis']= first_name
            request.session['P1_score']= first_value
            request.session['Diagnosis_type']= "Cough"



            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id
            request.session['detailed User message']= "Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined You are likely to have " + first_name + ". The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms."

            return render(request,"questionscompleted.html",{'context':context2})

            return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

        if len(x) == 2:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            context2 = {
                first_name: "Most Likely",
                second_name :"Possible",
                }
            request.session['Diagnosis']= first_name
            request.session['P1_score']= first_value
            request.session['Diagnosis_type']= "Cough"

            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id
            request.session['detailed User message']= "Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined You are likely to have " + first_name + "," + second_name + ". The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms."


            return render(request,"questionscompleted.html",{'context':context2})



        if len(x) == 3:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            third_name = x[-3][1]
            third_value = x[-3][0]
            # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            context2 = {
                first_name: "Most Likely",
                second_name :"Likely",
                third_name : "Possible",
                }
            request.session['Diagnosis']= first_name
            request.session['P1_score']= first_value
            request.session['Diagnosis_type']= "Cough"

            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id
            request.session['detailed User message']= "Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined You are likely to have " + first_name + " , " + second_name + " or " + third_name +  ". The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms."

            return render(request,"questionscompleted.html",{'context':context2})


            # return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

        if len(x) > 3:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            third_name = x[-3][1]
            third_value = x[-3][0]
            fourth_name = x[-4][1]
            fourth_value = x[-4][0]
            # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            print("first_value",first_value)
            print("second_value",second_value)
            print("third_value",third_value)
            print("fourth_value",fourth_value)
            context2 = {
                first_name: "Most Likely",
                second_name :"Very Likely",
                third_name : "Likely",
                fourth_name : "Possible"

            }
            request.session['Diagnosis']= first_name
            request.session['P1_score']= first_value
            request.session['Diagnosis_type']= "Cough"

            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id
            request.session['detailed User message']= "Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined You are likely to have " + first_name + " , " + second_name + " or " + third_name +  ". The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms."

            return render(request,"questionscompleted.html",{'context':context2})





def cvd_email(request):
    if request.method =="GET":
        print ("In contact Us page get request")
        print ("data",request.GET)
        # name = request.GET["name"]

        # phone = request.GET["phone"]
        email1 = request.GET["email"]
        # message = request.GET["discription"]

        user_diesease_update = request.session.get('user_diesease_update')
        cvd_risk = request.session['OverallRisk']
        Events_over10Year= request.session.get('possible_events')


        if len(email1) == 0:
            return JsonResponse({"status":"Error"})


        msz =  "Hi There,Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined {} \n  Your risk for cardiovascular events (heart attack, angina and strokes) is calculated at possible {} % over a 10 year period. \n The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses.Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms. \n  Our most commonly visited symptoms are chest pain (https://www.apnamd.ai/ChestPain/ ) and depression (https://www.apnamd.ai/Depression/Test/). \n Kind Regards \n ApnaMD Team ".format(cvd_risk,Events_over10Year)
        try :
            email = EmailMessage("Apna MD (AI Diagnosis)",msz,to=[email1])
            email.send()
            # newemails_store =  newemails.objects.create(email=email1,create_Date= datetime.datetime.now())
            # newemails_store.save()
            # user_diesease_update = top_disease_user_overall_with_user.objects.create(analysistype=request.session.get('Diagnosis_type'),disease1=request.session.get('Diagnosis'), p1=request.session.get('P1_score'),email=email1,verified="No",userfrom="Web Application", last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            return JsonResponse({"status":"sent"})
        except Exception as e:
            print ("Error in email exception",e)
            return JsonResponse({"status":"Error"})


def cvdthankyoupage(request):
    if request.user.is_authenticated:
        usr = request.user
        email1 = usr.email

        # user_diesease_update = top_disease_user_overall_with_user.objects.create(analysistype=request.session.get('Diagnosis_type'),disease1=request.session.get('Diagnosis'), p1=request.session.get('P1_score'),email=email1,verified="Yes",userfrom="Web Application", last_date_of_analysis=datetime.datetime.now())
        # user_diesease_update.save()
        cvd_risk = request.session['OverallRisk']
        Events_over10Year= request.session.get('possible_events')


        msz =  "Hi There,Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined {} \n  Your risk for cardiovascular events (heart attack, angina and strokes) is calculated at possible {} % over a 10 year period. \n The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses.Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms. \n  Our most commonly visited symptoms are chest pain (https://www.apnamd.ai/ChestPain/ ) and depression (https://www.apnamd.ai/Depression/Test/). \n Kind Regards \n ApnaMD Team ".format(cvd_risk,Events_over10Year)

        email = EmailMessage("Apna MD (AI Diagnosis)",msz,to=[email1])
        email.send()
        # newemails_store =  newemails.objects.create(email=email1,create_Date= datetime.datetime.now())
        # newemails_store.save()


    return render (request,"afterverification_cvd.html")

def cvdriskfrom(request):

    return render (request,"cvd_risk_home.html")


@csrf_exempt
def sendotp_cvd_risk(request):

    if request.method =="GET":

        try :
            otpnumber = request.GET["num"]
            request.session['otpnumber']=otpnumber


            print ("data",request.GET)

            user_diesease_update = request.session.get('user_diesease_update')
            cvd_risk = request.session.get('OverallRisk')
            Events_over10Year= request.session.get('possible_events')

            try :

                account_sid = "AC933127d38ff7d1939cc865520fff97cf"

                # Your Auth Token from twilio.com/console
                auth_token  = "69196d7c514f51c4c7733b4afb4c57e6"

                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    to=request.session.get('otpnumber'),
                    from_="+18508212276",
                    body=f'{cvd_risk} \n Your risk for cardiovascular events (heart attack, angina and strokes) is calculated at possible {Events_over10Year}% over a 10 year period.'
                    )

                # numberdatsave =  number_with_topdisease.objects.create(phonenumber=request.session.get('otpnumber'),topdisease=user_diesease_update)
                # numberdatsave.save()

                # newnumbers_store =  newnumbers.objects.create(number=request.session.get('otpnumber'),create_Date= datetime.datetime.now())
                # newnumbers_store.save()

                return JsonResponse({"status":"sent"})
            except Exception as e:
                print ("Error",e)
                return JsonResponse({"status":"Error"})


        except Exception as e:
            print ("Error",e)
            return JsonResponse({"status":"Error"})



    return render(request,"otpcode_CVD_risk.html")


def resendotp_cvd_risk(request):

    try :

        otp = random.randint (1000,9999)
        request.session['otp']=otp
        account_sid = "AC933127d38ff7d1939cc865520fff97cf"

        # Your Auth Token from twilio.com/console
        auth_token  = "69196d7c514f51c4c7733b4afb4c57e6"

        client = Client(account_sid, auth_token)
        otp = request.session.get('otp')
        message = client.messages.create(
            to=request.session.get('otpnumber'),
            from_="+18508212276",
            body=f'Your OTP verification number is {otp}')
        html = render_to_string('otpcode_CVD_risk.html')
        print ("messgae sid",message.sid )
        return render(request,"otpcode_CVD_risk.html")
    except Exception as e:
        print ("Error",e)
        return JsonResponse({"status":"Error"})


def otp_verification_cvd_risk(request):

     return render (request,"otpcode_CVD_risk.html")




@csrf_exempt
def CVD_cal(request):


    score=0
    if request.method=='POST':
        print("POST request accepeted and post data is", request.POST)



        try:
            Age=request.POST['age']
        # print("Your age is", Age)
        except:
            Age =" "
            pass

        try:
            Gender=request.POST['gender']
        # print("Your gender is", Gender)
        except:
            Gender =" "
            pass

        try:
            Smoker=request.POST['smoker']
            print("Your are smoking or not", Smoker)
        except:
            Smoker =" "
            pass

        try:
            Diabetes=request.POST['diabetes']
            print("Do you have diabetes", Diabetes)
        except:
            Diabetes =" "
            pass

        try:
            BP_treatment=request.POST['ontreatment']
            print("Your BP_treatment is",BP_treatment)
        except:
            BP_treatment =" "
            pass

        try:
            Systolic_blood_pressure=request.POST['systolicblood']
            print("Your Systolic_blood_pressure is",Systolic_blood_pressure)
        except:
            Systolic_blood_pressure =" "
            pass

        try:
            Total_cholesterol=request.POST['total_cholesterol']
            print("Your Total_cholesterol is", Total_cholesterol)
        except:
            Total_cholesterol =" "
            pass

        try:
            HDL_cholesterol=request.POST['hdl_cholesterol']
            print("Your HDL_cholesterol is", HDL_cholesterol)
        except:
            HDL_cholesterol =" "
            pass


        if Gender=='Female':
            if int(Age) >=20 and int(Age)<=34:
                score-=7
                # print("your age is",Age)
                # print("your score is",score)
            if int(Age) >=35 and int(Age)<=39:
                score-=3
            if int(Age) >=40 and int(Age)<=44:
                score+=0
            if int(Age) >=45 and int(Age)<=49:
                score+=3
            if int(Age) >=50 and int(Age)<=54:
                score+=6
            if int(Age) >=55 and int(Age)<=59:
                score+=8
            if int(Age) >=60 and int(Age)<=64:
                score+=10
            if int(Age) >=65 and int(Age)<=69:
                score+=12
            if int(Age) >=70 and int(Age)<=74:
                score+=14
            if int(Age) >=75 and int(Age)<=79:
                score+=16
            print("Your gender score is", score)
    #totalcholesterol
            if int(Age) >=20 and int(Age)<=39:
                # print("instruction executed")
                if (Total_cholesterol)=="Less than 160":
                    score+=0
                if (Total_cholesterol)=="160 to 199":
                    print("instruction executed")
                    score+=4
                if (Total_cholesterol)=="200 to 239":
                    score+=8
                if (Total_cholesterol)=="240 to 279":
                    score+=11
                if (Total_cholesterol)=="Greater than or equal to 280":
                    score+=13
            print("your selected Total cholesterol is",score)

            if int(Age) >=40 and int(Age)<=49:
                if (Total_cholesterol)=="Less than 160":
                    score+=0
                if (Total_cholesterol)=="160 to 199":
                    score+=3
                if (Total_cholesterol)=="200 to 239":
                    score+=6
                if (Total_cholesterol)=="240 to 279":
                    score+=8
                if (Total_cholesterol)=="Greater than or equal to 280":
                    score+=10
            print("your selected Total cholesterol is",score)

            if int(Age) >=50 and int(Age)<=59:
                if (Total_cholesterol)=="Less than 160":
                    score+=0
                if (Total_cholesterol)=="160 to 199":
                    score+=2
                if (Total_cholesterol)=="200 to 239":
                    score+=4
                if (Total_cholesterol)=="240 to 279":
                    score+=5
                if (Total_cholesterol)=="Greater than or equal to 280":
                    score+=7
            print("your selected Total cholesterol is",score)

            if int(Age) >=60 and int(Age)<=69:
                if (Total_cholesterol)=="Less than 160":
                    score+=0
                if (Total_cholesterol)=="160 to 199":
                    score+=1
                if (Total_cholesterol)=="200 to 239":
                    score+=2
                if (Total_cholesterol)=="240 to 279":
                    score+=3
                if (Total_cholesterol)=="Greater than or equal to 280":
                    score+=4
            print("your selected Total cholesterol is",score)

            if int(Age) >=70 and int(Age)<=79:
                print("instruction executed")

                if (Total_cholesterol)=="Less than 160":
                    score+=0
                if (Total_cholesterol)=="160 to 199":
                    score+=1
                if (Total_cholesterol)=="200 to 239":
                    score+=1
                if (Total_cholesterol)=="240 to 279":
                    score+=2
                if (Total_cholesterol)=="Greater than or equal to 280":
                    score+=2
            print("your selected Total cholesterol is",score)
            #smoking
            if Smoker=="YES":
                if int(Age) >=20 and int(Age) <=39:
                    score+=9
                if int(Age) >=40 and int(Age) <=49:
                    score+=7
                if int(Age) >=50 and int(Age) <=59:
                    score+=4
                if int(Age) >=60 and int(Age) <=69:
                    score+=2
                if int(Age) >=70 and int(Age) <=79:
                    score+=1
            print("your smoking score is",score)
            #HDL CHolesterol
            if (HDL_cholesterol) =="Greater than or equal to 60":
                score-=1
            if (HDL_cholesterol) =="50 to 59":
                score+=0
            if (HDL_cholesterol) =="40 to 49":
                score+=1
            if (HDL_cholesterol) =="Less than 40":
                score+=2
            print(" your total score till HDL cholesterol is", score)


    #Systolic blood pressure, mm Hg:

            if BP_treatment=="NO":
                print("BP treatment2 executed")
                if (Systolic_blood_pressure) =="Less than 120":
                    score+=0
                if (Systolic_blood_pressure) =="120 to 129":
                    score+=1
                if (Systolic_blood_pressure) =="130 to 139":
                    score+=2
                if (Systolic_blood_pressure) =="140 to 159":
                    score+=3
                if (Systolic_blood_pressure) =="Greater than or equal to 160":
                    score+=4
                print(" your total score till HDL cholesterol is", score)

            if BP_treatment=="YES":
                print("BP treatment1 executed")
                if (Systolic_blood_pressure) =="Less than 120":
                    score+=0
                if (Systolic_blood_pressure) =="120 to 129":
                    score+=3
                if (Systolic_blood_pressure) =="130 to 139":
                    score+=4
                if (Systolic_blood_pressure) =="140 to 159":
                    score+=5
                if (Systolic_blood_pressure) =="Greater than or equal to 160":
                    score+=6
                print(" your total score till BP_treatment is", score)





        if Gender=='Male':
            if int(Age) >=20 and int(Age)<=34:
                score-=9
                # print("your age is",Age)
                # print("your score is",score)
            if int(Age) >=35 and int(Age)<=39:
                score-=4
            if int(Age) >=40 and int(Age)<=44:
                score+=0
            if int(Age) >=45 and int(Age)<=49:
                score+=3
            if int(Age) >=50 and int(Age)<=54:
                score+=6
            if int(Age) >=55 and int(Age)<=59:
                score+=8
            if int(Age) >=60 and int(Age)<=64:
                score+=10
            if int(Age) >=65 and int(Age)<=69:
                score+=11
            if int(Age) >=70 and int(Age)<=74:
                score+=12
            if int(Age) >=75 and int(Age)<=79:
                score+=13
            print("Your gender score is", score)

    #totalcholesterol
            if int(Age) >=20 and int(Age)<=39:
                # print("instruction executed")
                if (Total_cholesterol)=="Less than 160":
                    score+=0
                if (Total_cholesterol)=="160 to 199":
                    print("instruction executed")
                    score+=4
                if (Total_cholesterol)=="200 to 239":
                    score+=7
                if (Total_cholesterol)=="240 to 279":
                    score+=9
                if (Total_cholesterol)=="Greater than or equal to 280":
                    score+=11
            print("your selected Total cholesterol is",score)

            if int(Age) >=40 and int(Age)<=49:
                if (Total_cholesterol)=="Less than 160":
                    score+=0
                if (Total_cholesterol)=="160 to 199":
                    score+=3
                if (Total_cholesterol)=="200 to 239":
                    score+=5
                if (Total_cholesterol)=="240 to 279":
                    score+=6
                if (Total_cholesterol)=="Greater than or equal to 280":
                    score+=8
            print("your selected Total cholesterol is",score)

            if int(Age) >=50 and int(Age)<=59:
                if (Total_cholesterol)=="Less than 160":
                    score+=0
                if (Total_cholesterol)=="160 to 199":
                    score+=2
                if (Total_cholesterol)=="200 to 239":
                    score+=3
                if (Total_cholesterol)=="240 to 279":
                    score+=4
                if (Total_cholesterol)=="Greater than or equal to 280":
                    score+=5
            print("your selected Total cholesterol is",score)

            if int(Age) >=60 and int(Age)<=69:
                if (Total_cholesterol)=="Less than 160":
                    score+=0
                if (Total_cholesterol)=="160 to 199":
                    score+=1
                if (Total_cholesterol)=="200 to 239":
                    score+=1
                if (Total_cholesterol)=="240 to 279":
                    score+=2
                if (Total_cholesterol)=="Greater than or equal to 280":
                    score+=3
            print("your selected Total cholesterol is",score)

            if int(Age) >=70 and int(Age)<=79:
                print("instruction executed")

                if (Total_cholesterol)=="Less than 160":
                    score+=0
                if (Total_cholesterol)=="160 to 199":
                    score+=0
                if (Total_cholesterol)=="200 to 239":
                    score+=0
                if (Total_cholesterol)=="240 to 279":
                    score+=1
                if (Total_cholesterol)=="Greater than or equal to 280":
                    score+=1
            print("your selected Total cholesterol is",score)
            #smoking
            if Smoker=="YES":
                if int(Age) >=20 and int(Age) <=39:
                    score+=8
                if int(Age) >=40 and int(Age) <=49:
                    score+=5
                if int(Age) >=50 and int(Age) <=59:
                    score+=3
                if int(Age) >=60 and int(Age) <=69:
                    score+=1
                if int(Age) >=70 and int(Age) <=79:
                    score+=1
            print("your smoking score is",score)
            #HDL CHolesterol
            if (HDL_cholesterol) =="Greater than or equal to 60":
                score-=1
            if (HDL_cholesterol) =="50 to 59":
                score+=0
            if (HDL_cholesterol) =="40 to 49":
                score+=1
            if (HDL_cholesterol) =="Less than 40":
                score+=2
            print(" your total score till HDL cholesterol is", score)


    #Systolic blood pressure, mm Hg:

            if BP_treatment=="NO":
                print("BP treatment2 executed")
                if (Systolic_blood_pressure) =="Less than 120":
                    score+=0
                if (Systolic_blood_pressure) =="120 to 129":
                    score+=0
                if (Systolic_blood_pressure) =="130 to 139":
                    score+=1
                if (Systolic_blood_pressure) =="140 to 159":
                    score+=1
                if (Systolic_blood_pressure) =="Greater than or equal to 160":
                    score+=2
                print(" your total score till BP_treatment is", score)

            if BP_treatment=="YES":
                print("BP treatment1 executed")
                if (Systolic_blood_pressure) =="Less than 120":
                    score+=0
                if (Systolic_blood_pressure) =="120 to 129":
                    score+=1
                if (Systolic_blood_pressure) =="130 to 139":
                    score+=2
                if (Systolic_blood_pressure) =="140 to 159":
                    score+=2
                if (Systolic_blood_pressure) =="Greater than or equal to 160":
                    score+=3
                print(" your total score till BP_treatment is", score)


        score_data={
            "context1":score,
        }

        print("YOUR FINAL TOTAL SCORE IS", score)

        if Gender=="Female":
            print("Your final Female gender is successfull")

            if score<=19:
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="CVD Risk assesment",disease1="Low Risk", p1=score, last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                request.session['possible_events']=round(score,2)
                request.session['OverallRisk']= "Your overall risk assessment is LOW"
                request.session['user_diesease_update']=user_diesease_update.id

                request.session['Diagnosis']= "LOW"
                request.session['P1_score']= score
                request.session['Diagnosis_type']= "CVD Risk Assessment "

                return render(request, "CVD_risk_display_updated.html", {'Risk_Assessment' : "Your cardiovascular risk is deemed to be LOW", "score_data":score_data })

            if score>19 and score<=23:
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="CVD Risk assesment",disease1="Intermediate Risk", p1=score, last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                request.session['possible_events']=round(score,2)
                request.session['OverallRisk']= "Your overall risk assessment is INTERMEDIATE"
                request.session['user_diesease_update']=user_diesease_update.id
                request.session['Diagnosis']= "INTERMEDIATE"
                request.session['P1_score']= score
                request.session['Diagnosis_type']= "CVD Risk Assessment "

                return render(request, "CVD_risk_display_updated.html", {'Risk_Assessment' : "Your cardiovascular risk is deemed to be INTERMEDIATE", "score_data":score_data })

            if score>=24:
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="CVD Risk assesment",disease1="High Risk", p1=score, last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                request.session['possible_events']=round(score,2)
                request.session['OverallRisk']= "Your overall risk assessment is HIGH"
                request.session['user_diesease_update']=user_diesease_update.id
                request.session['Diagnosis']= "HIGH"
                request.session['P1_score']= score
                request.session['Diagnosis_type']= "CVD Risk Assessment "

                return render(request, "CVD_risk_display_updated.html", {'Risk_Assessment' : "Your cardiovascular risk is deemed to be HIGH", "score_data":score_data  })



        if Gender=="Male":
            print("Your final male gender is successfull")

            if score<=12:
            #     user_diesease_update = top_disease_user_overall.objects.create(analysistype="CVD Risk assesment",disease1="Low Risk", p1=score, last_date_of_analysis=datetime.datetime.now())
            #     user_diesease_update.save()
                request.session['possible_events']=round(score,2)
                request.session['OverallRisk']= "Your overall risk assessment is LOW"
                # request.session['user_diesease_update']=user_diesease_update.id
                request.session['Diagnosis']= "LOW"
                request.session['P1_score']= score
                request.session['Diagnosis_type']= "CVD Risk Assessment "

                return render(request, "CVD_risk_display_updated.html", {'Risk_Assessment' : "Your cardiovascular risk is deemed to be LOW", "score_data":score_data })

            if score>12 and score<=16:
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="CVD Risk assesment",disease1="Intermediate Risk", p1=score, last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                request.session['possible_events']=round(score,2)
                request.session['OverallRisk']= "Your overall risk assessment is INTERMEDIATE"
                # request.session['user_diesease_update']=user_diesease_update.id
                request.session['Diagnosis']= "INTERMEDIATE"
                request.session['P1_score']= score
                request.session['Diagnosis_type']= "CVD Risk Assessment "

                return render(request, "CVD_risk_display_updated.html", {'Risk_Assessment' : "Your cardiovascular risk is deemed to be INTERMEDIATE", "score_data":score_data })

            if score>=17:
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="CVD Risk assesment",disease1="High Risk", p1=score, last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                request.session['possible_events']=round(score,2)
                request.session['OverallRisk']= "Your overall risk assessment is HIGH"
                request.session['Diagnosis']= "HIGH"
                request.session['P1_score']= score
                request.session['Diagnosis_type']= "CVD Risk Assessment "

                # request.session['user_diesease_update']=user_diesease_update.id
                return render(request, "CVD_risk_display_updated.html", {'Risk_Assessment' : "Your cardiovascular risk is deemed to be HIGH", "score_data":score_data })

    return render(request,"CHD cal_jotform.html")


@csrf_exempt
def Diabetes(request):

    if request.method =="POST":
        print ("Inpost",request.POST)
        print('BODY', request.body)
        user=request.user
        point = 0
        diseasedic={}
        for question_id in request.POST:
            answer_id = request.POST[question_id]
            gender = " "

            if question_id == "1" :
                print ("question id",question_id)
                print ("answer_id id",answer_id)
                print ("points",point)
                if answer_id == "Under 35 years":
                    point += 0
                if answer_id == "35 – 44 years":
                    point += 2
                if answer_id == "45 – 54 years":
                    point += 4
                if answer_id == "55 – 64 years":
                    point += 6
                if answer_id == "65 years or over":
                    point += 8
                print ("points",point)
            if question_id == "2" :
                if answer_id == "Male":
                    point += 3
                    gender = answer_id
                if answer_id == "Female":
                    point += 0
                    gender = answer_id

            if question_id == "3" :
                if answer_id == "Asian":
                    point += 0
                if answer_id == "Indian":
                    point += 2

            if question_id == "4" :
                if answer_id == "Yes":
                    point += 3

            if question_id == "5" :
                if answer_id == "Yes":
                    point += 6

            if question_id == "6" :
                if answer_id == "Yes":
                    point += 2

            if question_id == "7" :
                if answer_id == "Yes":
                    point += 2

            if question_id == "8" :
                if answer_id == "Not Every day":
                    point += 1

            if question_id == "9" :
                if answer_id == "No":
                    point += 2

            if question_id == "10" :

                if gender == "Female":
                    if int(answer_id)  > 80 :
                        point+=0
                    if int(answer_id)  > 79 and int(answer_id) < 91 :
                        point+=4
                    if int(answer_id)  > 90 :
                        point+=7
                if gender == "Male":
                    if int(answer_id)  > 90 :
                        point+=0
                    if int(answer_id)  > 89 and int(answer_id) < 101 :
                        point+=4
                    if int(answer_id)  > 100 :
                        point+=7

            if question_id != "csrfmiddlewaretoken" :

                diseasedic[question_id]=[answer_id]


        print ("diseasedic",diseasedic)
        try :
            diseasedic=json.dumps(diseasedic)
        except Exception as e:
            print ("Error",e)
        print ("diseasedic",diseasedic)
        print ("ok",point)
        context = []
        if point < 6 :
            context.append({
                "data": "Your risk of developing diabetes is 1% within 5 years.",
                "data1":"Your risk of developing diabetes is deemed to be LOW.",
                "score":point,
                "risk":"Low Risk",
            })
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Diabates",disease1="Low Risk",p1=point,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            request.session['Diagnosis']= "LOW"
            request.session['P1_score']= point
            request.session['Diagnosis_type']= "Diabetes Check "



        if point > 5 and point < 9 :
            context.append({
                "data": "Your risk of developing diabetes is 2% within 5 years.",
                "data1":"Your risk of developing diabetes is deemed to be INTERMEDIATE.",
                "score":point,
                "risk":"Intermediate Risk",
            })
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Diabates",disease1="Intermediate Risk",p1=point,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            request.session['Diagnosis']= "INTERMEDIATE"
            request.session['P1_score']= point
            request.session['Diagnosis_type']= "Diabetes Check "



        if point > 8 and point < 12 :
            context.append({
                "data": "Your risk of developing diabetes is 3% within 5 years. ",
                "data1":"Your risk of developing diabetes is deemed to be INTERMEDIATE.",
                "score":point,
                "risk":"Intermediate Risk",
            })
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Diabates",disease1="Intermediate Risk",p1=point,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            request.session['Diagnosis']= "INTERMEDIATE"
            request.session['P1_score']= point
            request.session['Diagnosis_type']= "Diabetes Check "




        if point > 11 and point < 16 :
            context.append({
                "data": "Your risk of developing diabetes is 7% within 5 years.",
                "data1":" Your risk of developing diabetes is deemed to be HIGH.",
                "score":point,
                "risk":"High Risk",
            })
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Diabates",disease1="High Risk",p1=point,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            request.session['Diagnosis']= "HIGH"
            request.session['P1_score']= point
            request.session['Diagnosis_type']= "Diabetes Check "



        if point > 15 and point < 20 :
            context.append({
                "data": "Your risk of developing diabetes is 14% within 5 years.",
                "data1":" Your risk of developing diabetes is deemed to be HIGH.",
                "score":point,
                "risk":"High Risk",
            })
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Diabates",disease1="High Risk",p1=point,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            request.session['Diagnosis']= "HIGH"
            request.session['P1_score']= point
            request.session['Diagnosis_type']= "Diabetes Check "



        if point > 19 :
            context.append({
                "data": "Your risk of developing diabetes is 33% within 5 years.",
                "data1":" Your risk of developing diabetes is deemed to be HIGH.",
                "score":point,
                "risk":"High Risk",
            })

            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Diabates",disease1="High Risk",p1=point,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            request.session['Diagnosis']= "HIGH"
            request.session['P1_score']= point
            request.session['Diagnosis_type']= "Diabetes Check "





        print ("context",context)
        request.session['details']=context
        request.session['user_diesease_update']=user_diesease_update.id

        return render (request,"Diabetes_Results.html",{'context':context})

    return render (request,"Diabetes.html")

def diabates_contactus(request):

    print ("In contact Us page diabates_contactus")
    if request.method =="GET":
        print ("In contact Us page get request")
        print ("data",request.GET)
        # name = request.GET["name"]

        # phone = request.GET["phone"]
        email1 = request.GET["email"]
        # message = request.GET["discription"]
        details = request.GET["details"]
        risk1 = request.GET["risk1"]

        print ("details",(details))

        print ("len of details",len(details))
        print ("type of details",type(details))


        if len(email1) == 0:
            return JsonResponse({"status":"Error"})


        msz =  "Hi ,\n my score is {} \n  and my risk is {}. \n King Regards \n ApnaMd".format(details,risk1)
        try :
            email = EmailMessage("Apna MD (AI Diagnosis)",msz,to=[email1])
            email.send()

            return JsonResponse({"status":"sent"})
        except Exception as e:
            print ("Error in email exception",e)
            return JsonResponse({"status":"Error"})

    return redirect("HOME")




def termsconditions(request):

    return render(request,"Terms&conditions.html")

def privacypolicy(request):

    return render(request,"privacypolicy.html")

def pregnancyemail(request):
    # print ("In contact Us page 2")
    # if request.method =="GET":
    #     inputEmailCta = request.GET["inputEmailCta1"]
    #     msz =  "Dear ApnaMd \n I want to subsucribe weekly update on this email \n {} ".format(inputEmailCta)
    #     try :
    #         email = EmailMessage("Contact Us Email",msz,to=["aidev@365cal.com"])
    #         email.send()

    #         return JsonResponse({"status":"sent"})
    #     except Exception as e:
    #         print ("Error in email exception",e)
    #         return JsonResponse({"status":"Error"})
    # return redirect("HOME")
    print ("In contact Us page")
    if request.method =="GET":
        print ("In contact Us page get request")
        print ("data",request.GET)
        name = request.GET["name"]

        phone = request.GET["phone"]
        email1 = request.GET["email"]
        message = request.GET["discription"]


        if len(email1) == 0:
            return JsonResponse({"status":"Error"})


        msz =  "Dear ApnaMd \n I want to get update regaring this  {} \n Here are my contact details \n {} \n {}".format(message,phone,email1)
        try :
            email = EmailMessage("Contact Us Email",msz,to=["aidev2@365cal.com"])
            email.send()

            return JsonResponse({"status":"sent"})
        except Exception as e:
            print ("Error in email exception",e)
            return JsonResponse({"status":"Error"})

    return redirect("HOME")

def contactus(request):
    global context
    print ("In contact Us page")
    if request.method =="GET":
        print ("In contact Us page get request")
        print ("data",request.GET)
        # name = request.GET["name"]

        # phone = request.GET["phone"]
        email1 = request.GET["email"]
        # message = request.GET["discription"]
        details = request.GET["details"]

        print ("details",(details))

        print ("len of details",len(details))
        print ("type of details",type(details))
        # details =  dict(details)
        res = ast.literal_eval(details)

        # res = json.loads(details)

        print ("len of details",len(res))
        diseases =[]
        for key, value in res.items():
            print (key)
            print (value)
        # print ("1st of details",res[0][0])


        if len(email1) == 0:
            return JsonResponse({"status":"Error"})


        msz =  "Hi ,\n Thank you for using the apnamd platform to test your symptoms.\n Our clinically tested algorithm uses the information you have provided to diagnose the most common and most critical health condition that might affect you.\n The accuracy of the information is dependent on the quality and details that you have provided. \n Information provided by apnamd is not aimed to replace medical consultation, \n it is to assist you better understand and explore your symptoms.\n For a detailed understanding please read our terms of service.\n  \n The four most likely clinical conditions based on their probability are \n  {}  \n If you would like further information about these clinical conditions, please email us with your concerns. \n  All our services are free to use and we do not use your information for marketing or advertising. \n Kind Regards \n Admin (ApnaMD)".format(res)
        try :
            email = EmailMessage("Apna MD (AI Diagnosis)",msz,to=[email1])
            email.send()

            return JsonResponse({"status":"sent"})
        except Exception as e:
            print ("Error in email exception",e)
            return JsonResponse({"status":"Error"})

    return redirect("HOME")

def emailme(request):
    if request.method == 'POST':
        get_email= request.POST['email_me']
        print("provided email id is", get_email)

        msz =  "Dear ApnaMd I want my diagnosis result"
        try :
            email =EmailMessage("I want top 4 diagnosis details",msz, to=[get_email])
            # message = email.message.EmailMessage()
            # message.add_header("From", "admin@apnamd.ai")
            # message.add_header("To", get_email)
            email.send()

            return JsonResponse({"status":"sent"})
        except Exception as e:
            print ("Error in email exception",e)
            return JsonResponse({"status":"Error"})


def check_user(request):
    if request.method =="GET":
        un = request.GET["user_n"]
        check = User.objects.filter(username=un)

        if len(check)==1:
            return HttpResponse("Exists")
        else :
            return HttpResponse ("Not Exists")
        print (check,len(check))
        print (un)
    return HttpResponse("Hello")

def allbloodreport(request):
    if request.user.is_authenticated:
        user = request.user
        allchestimages = cough_answer_details.objects.filter(user=user,Diagnosis_name="CoughBloodReport").order_by("last_date_of_analysis")
        details= []
        for i in allchestimages:
            questiondata = blood_questions.objects.get(id= i.Question_id)
            optiondata = blood_options_questions.objects.get(id= i.Answer_id)
            print ("question id",questiondata.Question)
            print ("answer id ",optiondata.option1)
            details.append({
                "Date":i.last_date_of_analysis,
                "Question":questiondata.Question,
                "option":optiondata.option1,
            })

        allfeverbloodreport = Fever_answer_details.objects.filter(user=user,Diagnosis_name="FeverBloodReport").order_by("last_date_of_analysis")
        details1= []
        for i in allfeverbloodreport:
            questiondata = blood_questions.objects.get(id= i.Question_id)
            optiondata = blood_options_questions.objects.get(id= i.Answer_id)
            print ("question id",questiondata.Question)
            print ("answer id ",optiondata.option1)
            details1.append({
                "Date":i.last_date_of_analysis,
                "Question":questiondata.Question,
                "option":optiondata.option1,
            })
        allbloodabdominal = abdominal_answer_details.objects.filter(user=user,Diagnosis_name="AbdominalBloodReport").order_by("last_date_of_analysis")
        details2= []
        for i in allbloodabdominal:
            questiondata = blood_questions.objects.get(id= i.Question_id)
            optiondata = blood_options_questions.objects.get(id= i.Answer_id)
            print ("question id",questiondata.Question)
            print ("answer id ",optiondata.option1)
            details2.append({
                "Date":i.last_date_of_analysis,
                "Question":questiondata.Question,
                "option":optiondata.option1,
            })

        print ("alla chest xray",details)

        if len(details) + len(details1) + len (details2) == 0:
            return render(request,"alldataforusersubmitted.html",{'data0':"No record Found"})
        return render(request,"alldataforusersubmitted.html",{'data':details,'data1':details1,'data2':details2})



def previousdataforcxry(request):
    if request.user.is_authenticated:
        user = request.user
        allchestimages = Chest_Xray_image.objects.filter(user=user)
        print ("alla chest xray",allchestimages)
        if len(allchestimages) == 0:
            return render(request,"alldataforusersubmitted.html",{'data0':"No record Found"})
        return render(request,"alldataforusersubmitted.html",{'chestxray':allchestimages})


# @login_required(login_url='signin')
def blood_Report_cough(request):

    # if request.user.is_authenticated:
    #     user = request.user
        if request.method == 'GET':
            questions = blood_questions.objects.all()
            final_data1=[]
            for l in questions:
                options=[]
                all_option=blood_options_questions.objects.filter(question=l.id)
                for data in all_option:
                    options.append({
                        "options_id":data.id,
                        "options_data":data.option1,
                    })
                final_data1.append({
                            "question_data":l.Question,
                            "question_id":l.id,
                            "option":options,

                        })
            # context = {
            #     "data":final_data1
            # }
            return render(request,"questions.html",{'generalquestionsblood':final_data1})
        if request.method == 'POST':
            global VB
            global BP
            global A
            global CHF
            global CLD
            global LC
            global PE
            global covid
            global context
            print("VB",VB)
            print("BP",BP)
            print("A",A)
            print("CHF",CHF)
            print("CLD",CLD)
            print("LC",LC)
            print("PE",PE)
            print("covid",covid)
            for question_id in request.POST:
                answer_id = request.POST[question_id]
                # if question_id != "csrfmiddlewaretoken":
                #     question_answer_save = cough_answer_details.objects.create(user=user,Question_id=question_id,Answer_id=answer_id,Diagnosis_name="CoughBloodReport",last_date_of_analysis=datetime.datetime.now())
                #     question_answer_save.save()

                    # print ("question_id",question_id)
                    # print ("answer_id",answer_id)
                if question_id == "8":
                    if answer_id=="11":
                        BP+=1
                if question_id == "9":
                    if answer_id=="12":
                        VB+=1
                        PE+=0.5
                    if answer_id=="13":
                        BP+=0.5
                        PE+=0.5

                if question_id == "10":
                    if answer_id=="14":
                        LC+=0.5

                if question_id == "13":
                    if answer_id=="17":
                        CHF+=1
                if question_id == "14":
                    if answer_id=="18":
                        CHF+=1
                if question_id == "15":
                    if answer_id=="19":
                        LC+=1
            print ("POST")

            print("Viral_Bronchitis",VB)
            print("Bacterial_Pneumonia",BP)
            print("Asthma",A)
            print("Chronic_Heart_Failure",CHF)
            print("Chronic_Lung_Disease",CLD)
            print("Lung_Cancer",LC)
            print("Pleural_Embolism",PE)
            print("covid",covid)
            context ={

                "Viral_Bronchitis":VB,
                "Bacterial_Pneumonia":BP,
                "Asthma":A,
                "Chronic_Heart_Failure":CHF,
                "Chronic_Lung_Disease":CLD,
                "Lung_Cancer":LC,
                "Pleural_Embolism":PE,
                "covid":covid
            }
            print (context)

            x = sorted(((v,k) for k,v in context.items() if v > 0))
            print ("len of x",len(x))
            if len(x) == 0:
                return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

            if len(x) == 1:
                first_name = x[-1][1]
                first_value = x[-1][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="cough", disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",

                    }

                return render(request,"questionscompleted.html",{'context':context2})

                return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

            if len(x) == 2:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",
                    second_name :"Possible",
                    }

                return render(request,"questionscompleted.html",{'context':context2})



            if len(x) == 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                context2 = {
                    first_name: "Most Likely",
                    second_name :"Likely",
                    third_name : "Possible",
                    }

                return render(request,"questionscompleted.html",{'context':context2})


                # return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

            if len(x) > 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                fourth_name = x[-4][1]
                fourth_value = x[-4][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                print("first_value",first_value)
                print("second_value",second_value)
                print("third_value",third_value)
                print("fourth_value",fourth_value)
                context2 = {
                    first_name: "Most Likely",
                    second_name :"Very Likely",
                    third_name : "Likely",
                    fourth_name : "Possible"

                }

                return render(request,"questionscompleted.html",{'context':context2})

# @login_required(login_url='signin')
def chest_xray(request):
    # if request.user.is_authenticated:
    return render (request,"chestxray.html")
    # return redirect("signin")

# Create your views here.
# @login_required(login_url='signin')
def cough_question(request):
    global VB
    global BP
    global A
    global CHF
    global CLD
    global LC
    global PE
    global covid
    # if request.user.is_authenticated:
    #     user = request.user

    if request.method == 'GET':
        questions = cough_questions.objects.all()
        final_data1=[]
        for l in questions:
            options=[]
            all_option=cough_options_questions.objects.filter(question=l.id)
            for data in all_option:
                options.append({
                    "options_id":data.id,
                    "options_data":data.option1,
                })
            final_data1.append({
                        "question_data":l.Question,
                        "question_id":l.id,
                        "option":options,

                    })
        # context = {
        #     "data":final_data1
        # }
        return render(request,"questions.html",{'context':final_data1})
    if request.method == 'POST':
        # user = request.user
        # print ("user in cough with current smoker",user.user_detail.CurrentSmoker)
        # print ("user in cough with past smoker",user.user_detail.PastSmoker)
        VB=0
        BP=0
        A=0
        CHF=0
        CLD=0
        LC=0
        PE=0
        covid=0
        some_var = request.POST.getlist('checks[]')
        print (len(some_var))


        context1 ={

            "Viral_Bronchitis":VB,
            "Bacterial_Pneumonia":BP,
            "Asthma":A,
            "Chronic_Heart_Failure":CHF,
            "Chronic_Lung_Disease":CLD,
            "Lung_Cancer":LC,
            "Pleural_Embolism":PE,
            "covid":covid
        }
        print ("context1",context1)
        # if user.user_detail.CurrentSmoker== "Yes" or user.user_detail.PastSmoker=="Yes":
        #     print ("value can be added")
        #     VB+=0.5
        #     BP+=1
        #     CHF+=1
        #     CLD+=1
        #     LC+=1
        # print ("some_var",some_var)
        for qn1 in some_var:

                # question_answer_save = cough_answer_details.objects.create(user=user,Question_id="1",Answer_id=qn1,Diagnosis_name="Cough",last_date_of_analysis=datetime.datetime.now())
                # question_answer_save.save()
                print ("qn1",qn1)
                # VB0, BP0, A1, CHF.25, CLD.25, LC0, PE0)
                if qn1=="1":
                    VB+=0
                    BP+=0
                    A+=1
                    CHF+=0.25
                    CLD+=0.25
                    LC+=0
                    PE+=0
                if qn1=="2":
                    VB+=0
                    BP+=0
                    A+=0.5
                    CHF+=1
                    CLD+=0.5
                    LC+=0
                    PE+=0
                if qn1=="3":
                    VB+=0
                    BP+=0.5
                    A+=0.5
                    CHF+=0.5
                    CLD+=1
                    LC+=0
                    PE+=0
                if qn1=="4":
                    VB+=0
                    BP+=0
                    A+=0
                    CHF+=0
                    CLD+=0
                    LC+=0
                    PE+=1
                if qn1=="5":
                    VB+=0
                    BP+=0
                    A+=1
                    CHF+=0
                    CLD+=0
                    LC+=0
                    PE+=0
                if qn1=="6":
                    VB+=0.5
                    BP+=0.5
                    A+=0.5
                    CHF+=0.5
                    CLD+=0.5
                    LC+=1
                    PE+=0
                if qn1=="7":
                    VB+=0.25
                    BP+=0.5
                    A+=0.5
                    CHF+=0.25
                    CLD+=1
                    LC+=0
                    PE+=0.5

        for key, value in request.POST.items():
            print('Key: %s' % (key) )
            # print(f'Key: {key}') in Python >= 3.7
            print('Value %s' % (value) )
            # print(f'Value: {value}') in Python >= 3.7

        for question_id in request.POST:
            print ("question_id",question_id)
            answer_id = request.POST[question_id]
            print ("answer_id",answer_id)
            # if question_id != "csrfmiddlewaretoken" and question_id != "checks[]":
            #     print ("questions id in if condition",question_id)
            #     question_answer_save = cough_answer_details.objects.create(user=user,Question_id=question_id,Answer_id=answer_id,Diagnosis_name="Cough",last_date_of_analysis=datetime.datetime.now())
            #     question_answer_save.save()

            if question_id == "2":

                # question_answer_save = question_answers_user.objects.create(user=user,question=question_id,answer=answer_id,diagnosisname="Cough",last_date_of_analysis=datetime.datetime.now())
                # question_answer_save.save()
                # (VB1, BP.25, A.5, CHF-1, CLD-1, LC-1, PE.75)
                if answer_id == "8":
                    VB+=1
                    BP+=0.25
                    A+=0.25
                    CHF-=1
                    CLD-=1
                    LC-=1
                    PE+=1
                    covid+=1

                #  (VB-.5, BP1, A.5, CHF0, CLD0, LC0, PE.25)
                if answer_id == "9":
                    VB-=0.5
                    BP+=1
                    A+=0.5
                    CHF+=0.25
                    CLD-=1
                    LC+=0.5
                    PE+=0.5
                    covid+=0.75

                # (VB-1, BP.25, CHF1, CLD 1, LC1, PE0)
                if answer_id == "10":
                    VB-=1
                    BP+=0.25
                    A+=0.75
                    CHF+=1
                    CLD+=1
                    LC+=1
                    PE-=1
                    covid-=1

            if question_id =="3" :

                # question_answer_save = question_answers_user.objects.create(user=user,question=question_id,answer=answer_id,diagnosisname="Cough",last_date_of_analysis=datetime.datetime.now())
                # question_answer_save.save()
                # (VB.25, BP1, A.25, CHF.25, CLD.5, LC.5, PE.25)
                if answer_id == "11":
                    VB+=0.25
                    BP+=1
                    A+=0.25
                    CHF+=0.25
                    CLD+=0.5
                    LC+=0.5
                    PE+=0
                    covid+=0.5

            if question_id =="4":
                # question_answer_save = question_answers_user.objects.create(user=user,question=question_id,answer=answer_id,diagnosisname="Cough",last_date_of_analysis=datetime.datetime.now())
                # question_answer_save.save()
                if answer_id == "13":
                    VB+=0.25
                    BP+=0.25
                    A+=0
                    CHF+=0.25
                    CLD+=0.5
                    LC+=1
                    PE+=1
                    covid+=0.5



            if question_id == "5":
                # question_answer_save = question_answers_user.objects.create(user=user,question=question_id,answer=answer_id,diagnosisname="Cough",last_date_of_analysis=datetime.datetime.now())
                # question_answer_save.save()
                # (VB1, BP.5, A.75, CHF0, CLD0, LC0, PE0)
                if answer_id == "15":
                    VB+=1
                    BP+=0.25
                    A+=0.25
                    CHF+=0
                    CLD+=0
                    LC+=0
                    PE+=0
                    covid+=1

            if question_id =="6":
                # question_answer_save = question_answers_user.objects.create(user=user,question=question_id,answer=answer_id,diagnosisname="Cough",last_date_of_analysis=datetime.datetime.now())
                # question_answer_save.save()
                # (VB0, BP.5, A.5, CHF1, CLD1, LC.75, PE1)
                if answer_id == "17":
                    VB+=0
                    BP+=0.5
                    A+=0.5
                    CHF+=1
                    CLD+=1
                    LC+=0.5
                    PE+=1
                    covid+=0.5

            if question_id=="7":
                # question_answer_save = question_answers_user.objects.create(user=user,question=question_id,answer=answer_id,diagnosisname="Cough",last_date_of_analysis=datetime.datetime.now())
                # question_answer_save.save()
                if answer_id == "19":
                    VB+=0.25
                    BP+=0.25
                    A+=0.25
                    CHF+=0.5
                    CLD+=0.25
                    LC+=0.5
                    PE+=1
                    covid+=0.5

            if question_id=="8":
                # question_answer_save = question_answers_user.objects.create(user=user,question=question_id,answer=answer_id,diagnosisname="Cough",last_date_of_analysis=datetime.datetime.now())
                # question_answer_save.save()
                # (VB-1, BP.25, A.25, CHF.75, CLD1, LC1, PE-.25)
                if answer_id == "21":
                    VB-=1
                    BP+=0.25
                    A+=0
                    CHF-=1
                    CLD+=0.75
                    LC+=1
                    PE-=1
                    covid-=1


            if question_id=="9":
                # question_answer_save = question_answers_user.objects.create(user=user,question=question_id,answer=answer_id,diagnosisname="Cough",last_date_of_analysis=datetime.datetime.now())
                # question_answer_save.save()
                # •	Yes (VB.25, BP.5, A.5, CHF1, CLD1, LC1, PE1)
                if answer_id == "23":
                    VB+=0.25
                    BP+=0.5
                    A+=0.5
                    CHF+=1
                    CLD+=1
                    LC+=1
                    PE+=1
                    covid-=0.5

            if question_id=="10":
                # question_answer_save = question_answers_user.objects.create(user=user,question=question_id,answer=answer_id,diagnosisname="Cough",last_date_of_analysis=datetime.datetime.now())
                # question_answer_save.save()
                # •	Yes (VB.25, BP.5, A.5, CHF1, CLD1, LC1, PE1)
                if answer_id == "25":
                    VB-=1
                    BP-=1
                    A-=1
                    CHF+=1
                    CLD-=1
                    LC-=1
                    PE-=1
                    covid-=1

            if question_id=="11":
                # question_answer_save = question_answers_user.objects.create(user=user,question=question_id,answer=answer_id,diagnosisname="Cough",last_date_of_analysis=datetime.datetime.now())
                # question_answer_save.save()
                # •	Yes (VB.25, BP.5, A.5, CHF1, CLD1, LC1, PE1)
                if answer_id == "27":
                    VB+=0.25
                    BP+=0.25
                    A-=1
                    CHF-=1
                    CLD-=1
                    LC-=1
                    PE-=1
                    covid+=1


        context ={

            "Viral_Bronchitis":VB,
            "Bacterial_Pneumonia":BP,
            "Asthma":A,
            "Chronic_Heart_Failure":CHF,
            "Chronic_Lung_Disease":CLD,
            "Lung_Cancer":LC,
            "Pleural_Embolism":PE,
            "covid":covid
        }
        print (context)

        x = sorted(((v,k) for k,v in context.items()))
        first_name = x[-1][1]
        first_value = x[-1][0]
        second_name = x[-2][1]
        second_value = x[-2][0]
        third_name = x[-3][1]
        third_value = x[-3][0]
        fourth_name = x[-4][1]
        fourth_value = x[-4][0]

        print("first_value",first_value)
        print("second_value",second_value)
        print("third_value",third_value)
        print("fourth_value",fourth_value)
        context2 = {
            first_name: first_value,
            second_name :second_value,
            third_name : third_value,
            fourth_name : fourth_value

        }
        # user_diesease_update = disease_user.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now(),diagnosisname="Cough")
        # user_diesease_update.save()

        # return redirect ("questionscough")
        # return redirect ("chest_xray")
        # return render(request,"questionscompleted.html",{'context':context2})
        return render (request,"thanks_page_cough.html")


    return redirect("signin")

@login_required(login_url='signin')
def userprofile(request):

    return render(request,"Authentication/userprofile.html")

# @login_required(login_url='signin')
def cxr_description(request):

    # if request.user.is_authenticated:
    #     user = request.user
    return render (request,"forcxrdetail.html")
    # return redirect("signin")

# @login_required(login_url='signin')
def blood_description(request):

    # if request.user.is_authenticated:
    #     user = request.user
    return render (request,"forblooddetail.html")
    # return redirect("signin")


@csrf_exempt
def Dementia(request):


    if request.method == 'GET':

        return render(request,"dementia_qn.html")

    if request.method == 'POST':
        print("post req accepted")
        global Score

        O_Score = 0
        M_Score = 0
        AR_score = 0
        N_score = 0

        updated_data= dict(request.POST.lists())
        print("updated_data", updated_data)

        try:
            qn1=request.POST['dem_qn1']

            print("Your qn1 is", qn1)
        except:
            qn1 =" "
            pass

        try:
            qn2=request.POST['dem_qn2']
            print("Your qn2 is", qn2)
        except:
            qn2 =" "
            pass

        try :
            qn3=request.POST['dem_qn3']
            print("Your qn3 is", qn4)

        except:
            qn3 =" "
            pass


        try:
            qn4=request.POST['dem_qn4']
            print("Your qn4 is", qn4)
        except:
            qn4 =" "
            pass

        try:
            qn5=request.POST['dem_qn5']
            print("Your qn5 is", qn5)
        except:
            qn5 =" "
            pass

        try:
            qn6=request.POST['dem_qn6']
            print("Your qn6 is", qn6)
        except:
            qn6 =" "
            pass

        try:
            qn7=request.POST['dem_qn7']
            print("Your qn7 is", qn7)
        except:
            qn7 =" "
            pass

        try:
            qn8=request.POST['dem_qn8']
            print("Your qn8 is", qn8)
        except:
            qn8 =" "
            pass

        try:
            qn9=request.POST['dem_qn9']
            print("Your qn9 is", qn9)
        except:
            qn9 =" "
            pass

        try:
            qn10=request.POST['dem_qn10']
            print("Your qn10 is", qn10)
        except:
            qn10 =" "
            pass

        try:
            qn11=request.POST['dem_qn11']
            print("Your qn11 is", qn11)
        except:
            qn11 =" "
            pass

        try:
            qn12=request.POST['dem_qn12']
            print("Your qn12 is", qn12)
        except:
            qn12 =" "
            pass

        try:
            qn13=request.POST['dem_qn13']
            print("Your qn13 is", qn13)
        except:
            qn13 =" "
            pass

        try:
            question14=updated_data['dem_qn14[]']

            print("Your qn14 is", question14)
        except:
            question14 =" "
            pass


        if qn1 == "2022":
            O_Score+=1
            print("Total score qn1 is ", O_Score)


        if qn2 == "Summer":
            O_Score+=1
            print("Total score qn2 is ", O_Score)


        if qn3 == "May":
            O_Score+=1
            print("Total score qn3 is ", O_Score)


        if qn4 == "5 May 2022":
            O_Score+=1
            print("Total score qn4 is ", O_Score)


        if qn5 == "Friday":
            O_Score+=1
            print("Total score qn5 is ", O_Score)


        if qn6 == "India":
            O_Score+=1
            print("Total score qn6 is ", O_Score)


        if qn7 == "Maharashtra":
            O_Score+=1
            print("Total score qn7 is ", O_Score)


        if qn8 == "Pune":
            O_Score+=1
            print("Total score qn8 is ", O_Score)


        if qn9 == "1234 Main street":
            O_Score+=1
            print("Total score qn9 is ", O_Score)


        if qn10 == "Glora heights":
            O_Score+=1
            print("Total score qn10 is ", O_Score)


        if qn11 == "R-8":
            O_Score+=1
            print("Total score qn11 is ", O_Score)


        if qn12 == "F12":
            O_Score+=1
            print("Total score qn12 is ", O_Score)


        if qn13 == "DLROW":
            AR_score+=5
            print("Total score qn13 is ", O_Score)

        for qn14 in question14:
            print("qn14 executed", question14)

            if qn14 =="Ball":
                print("qn14-1 executed")
                M_Score+=1
                print("Total score qn14 is  ", M_Score)


            if qn14=="Car":
                print("qn14-2 executed")
                M_Score+=1
                print("Total score qn14 is ", M_Score)

            if qn14=="Man":
                print("qn14-3 executed")
                M_Score+=1
                print("Total score qn14 is ", M_Score)


        Total_score_obtained= O_Score+ M_Score + AR_score+ N_score

        print("Total_score_obtained", Total_score_obtained)


        score_data ={
                "context1":O_Score,
                "context2":AR_score,
                "context3":M_Score,
                "context4":N_score,
                "context5":Total_score_obtained,

            }
        # data_to_save = Cognition_analysis.objects.create(user_name= user, Orientation_Score_out_of_12 =O_Score, Memory_Score_out_of_3 = M_Score, Attention_and_recall_Score_out_of_5 =AR_score, N_Score_out_of_2 =N_score, Total_Score_out_of_22 =Total_score_obtained)
        # data_to_save.save()
        return render(request,"info_display.html",{"score_data":score_data})

    return redirect("signin")


@login_required(login_url='signin')
def Pregnancy(request):
    if request.user.is_authenticated:
        user = request.user
    return render(request,"Pregnancy.html")

# @login_required(login_url='signin')
def blood_Report_fever(request):

    # if request.user.is_authenticated:
    #     user = request.user
        if request.method == 'GET':
            questions = blood_questions.objects.all()
            final_data1=[]
            for l in questions:
                options=[]
                all_option=blood_options_questions.objects.filter(question=l.id)
                for data in all_option:
                    options.append({
                        "options_id":data.id,
                        "options_data":data.option1,
                    })
                final_data1.append({
                            "question_data":l.Question,
                            "question_id":l.id,
                            "option":options,

                        })
            # context = {
            #     "data":final_data1
            # }
            return render(request,"questions.html",{'generalquestionsblood':final_data1})

        if request.method == 'POST':
            global Viral_Fever
            global COVID
            global Pneumonia
            global Cholangitis
            global Endocarditis
            global Cellulitis
            global UTI
            global Osteomyelitis
            global Meningitis
            print("Viral_Fever",Viral_Fever)
            print("COVID",COVID)
            print("Pneumonia",Pneumonia)
            print("Cholangitis",Cholangitis)
            print("Endocarditis",Endocarditis)
            print("Cellulitis",Cellulitis)
            print("UTI",UTI)
            print("Osteomyelitis",Osteomyelitis)
            print("Meningitis",Meningitis)
            for question_id in request.POST:
                answer_id = request.POST[question_id]
                # if question_id != "csrfmiddlewaretoken":
                #     question_answer_save = Fever_answer_details.objects.create(user=user,Question_id=question_id,Answer_id=answer_id,Diagnosis_name="FeverBloodReport",last_date_of_analysis=datetime.datetime.now())
                #     question_answer_save.save()
                #     print ("question_id",question_id)
                #     print ("answer_id",answer_id)
                 ### J
                if question_id =="7":
                    if answer_id =="10":
                        Endocarditis+=1
                ####k
                if question_id =="8":
                    if answer_id == "11":
                        # Viral_Fever+=1
                        # COVID+=0.5
                        Pneumonia+=1
                        Cholangitis+=1
                        Endocarditis+=1
                        Cellulitis+=1
                        UTI+=1
                        Osteomyelitis+=1
                        Meningitis+=1
                ### L M
                if question_id == "9":
                    if answer_id == "12":
                        Osteomyelitis+=1
                        COVID+=1
                    if answer_id == "13":
                        Pneumonia+=1
                        Osteomyelitis+=1
                ### N
                if question_id =="10":
                    if answer_id =="14":
                        Cholangitis+=1
                        Endocarditis+=1

                ### P
                if question_id =="12":
                    if answer_id =="16":
                        Cholangitis+=1
                        Endocarditis+=1



                ####Q
                if question_id =="13":
                    if answer_id =="17":
                        UTI+=1

                ####R
                if question_id =="14":
                    if answer_id =="18":
                        UTI+=1

            print ("POST")
            context ={
                "Viral_Fever":Viral_Fever,
                "COVID":COVID,
                "Pneumonia":Pneumonia,
                "Cholangitis":Cholangitis,
                "Endocarditis":Endocarditis,
                "Cellulitis":Cellulitis,
                "UTI":UTI,
                "Osteomyelitis":Osteomyelitis,
                "Meningitis":Meningitis,
            }
            print (context)

            x = sorted(((v,k) for k,v in context.items() if v > 0))
            print ("len of x",len(x))
            if len(x) == 0:
                return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

            if len(x) == 1:
                first_name = x[-1][1]
                first_value = x[-1][0]
                # user_diesease_update = top_disease_user_Fever.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                context2 = {
                    first_name: "Most Likely",

                    }

                return render(request,"questionscompleted.html",{'context':context2})

                return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

            if len(x) == 2:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                # user_diesease_update = top_disease_user_Fever.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                context2 = {
                    first_name: "Most Likely",
                    second_name :"Possible",
                    }

                return render(request,"questionscompleted.html",{'context':context2})



            if len(x) == 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                # user_diesease_update = top_disease_user_Fever.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                context2 = {
                    first_name: "Most Likely",
                    second_name :"Likely",
                    third_name : "Possible",
                    }

                return render(request,"questionscompleted.html",{'context':context2})


                # return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

            if len(x) > 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                fourth_name = x[-4][1]
                fourth_value = x[-4][0]
                # user_diesease_update = top_disease_user_Fever.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                print("first_value",first_value)
                print("second_value",second_value)
                print("third_value",third_value)
                print("fourth_value",fourth_value)
                context2 = {
                    first_name: "Most Likely",
                    second_name :"Very Likely",
                    third_name : "Likely",
                    fourth_name : "Possible"

                }

                return render(request,"questionscompleted.html",{'context':context2})




@csrf_exempt
def fever_question(request):
    global Viral_Fever
    global COVID
    global Pneumonia
    global Cholangitis
    global Endocarditis
    global Cellulitis
    global UTI
    global Osteomyelitis
    global Meningitis


    # if request.user.is_authenticated:
    #     user = request.user
    if request.method == 'GET':


        return render(request,"fever_qn.html")
    if request.method == 'POST':
        # user=request.user

        Viral_Fever =0
        COVID=0
        Pneumonia=0
        Cholangitis=0
        Endocarditis=0
        Cellulitis=0
        UTI=0
        Osteomyelitis=0
        Meningitis=0

        # datae= user.user_detail.dob

        # print ("user.user_detail.dob",datae.year)
        def calculateAge(birthDate):
            global UTI

            days_in_year = 365.2425
            try :
                age = int((date.today() - birthDate).days / days_in_year)
                print ("age in try", age)
                if int(age) > 75:
                    print ("value can be added")
                    UTI+=1
            except Exception as e:
                pass
            return age

        # print(calculateAge(date(datae.year,datae.month,datae.day)), "years")

        # if user.user_detail.CurrentSmoker== "Yes" or user.user_detail.PastSmoker=="Yes":

        #     Pneumonia+=1



        for question_id in request.POST:
            print(request.POST)

            answer_id = request.POST[question_id]
            # print("answer_id", answer_id)
            # if question_id != "csrfmiddlewaretoken":
            #     print ("question_id",question_id)
            #     print ("answer_id",answer_id)
            #     question_answer_save = Fever_answer_details.objects.create(user=user,Question_id=question_id,Answer_id=answer_id,Diagnosis_name="Fever",last_date_of_analysis=datetime.datetime.now())
            #     question_answer_save.save()
            if question_id == "fever_qn1":
                # print("answer_id1", answer_id)

                if answer_id == "Less than 1 week":
                    Viral_Fever+=1
                    COVID+=0.5
                    Pneumonia+=0.25
                    Cholangitis+=0.5
                    Endocarditis-=1
                    Cellulitis+=0
                    UTI+=0
                    Osteomyelitis-=1
                    Meningitis+=1

                if answer_id == "More than 1 week":
                    Viral_Fever+=0
                    COVID+=0.5
                    Pneumonia+=1
                    Cholangitis+=0.5
                    Endocarditis+=1
                    Cellulitis+=1
                    UTI+=1
                    Osteomyelitis+=1
                    Meningitis+=0.5
            if question_id == "fever_qn2":
                # print("answer_id2", answer_id)
                if answer_id == "Yes":
                    Viral_Fever+=1
                    COVID+=0.5
                    Pneumonia+=0
                    Cholangitis-=1
                    Endocarditis-=1
                    Cellulitis-=1
                    UTI-=1
                    Osteomyelitis-=1
                    Meningitis+=0

            if question_id =="fever_qn3" :
                # print("answer_id3", answer_id)
                if answer_id == "Yes":
                    Viral_Fever+=1
                    COVID+=1
                    Pneumonia+=1
                    Cholangitis-=1
                    Endocarditis-=1
                    Cellulitis-=1
                    UTI-=1
                    Osteomyelitis-=1
                    Meningitis+=0.5

            if question_id =="fever_qn4":
                if answer_id == "Yes":
                    Viral_Fever+=0
                    COVID-=1
                    Pneumonia+=0
                    Cholangitis+=0
                    Endocarditis+=0
                    Cellulitis+=0
                    UTI+=0
                    Osteomyelitis+=0
                    Meningitis+=0.75

            if question_id == "fever_qn5":
                if answer_id == "Yes":
                    Viral_Fever+=0.25
                    COVID+=0.25
                    Pneumonia+=1
                    Cholangitis-=1
                    Endocarditis-=1
                    Cellulitis-=1
                    UTI-=1
                    Osteomyelitis-=1
                    Meningitis+=0

            if question_id =="fever_qn6":
                if answer_id == "Yes":
                    Viral_Fever-=0.5
                    COVID+=0.5
                    Pneumonia+=1
                    Cholangitis-=1
                    Endocarditis+=0.25
                    Cellulitis-=1
                    UTI-=1
                    Osteomyelitis-=1
                    Meningitis+=0
            if question_id=="fever_qn7":

                if answer_id == "Yes":
                    Viral_Fever+=0.25
                    COVID+=0.5
                    Pneumonia+=0.5
                    Cholangitis-=1
                    Endocarditis+=0.5
                    Cellulitis-=1
                    UTI-=1
                    Osteomyelitis-=1
                    Meningitis-=1

            if question_id=="fever_qn8":

                if answer_id == "Yes":
                    Viral_Fever-=1
                    COVID+=0
                    Pneumonia+=0
                    Cholangitis+=1
                    Endocarditis-=1
                    Cellulitis-=1
                    UTI+=1
                    Osteomyelitis-=1
                    Meningitis-=1

            if question_id=="fever_qn9":

                if answer_id == "Yes":
                    Viral_Fever+=0.25
                    COVID+=0
                    Pneumonia+=0
                    Cholangitis+=1
                    Endocarditis+=0
                    Cellulitis+=0
                    UTI+=0
                    Osteomyelitis-=1
                    Meningitis-=1

            if question_id=="fever_qn10":

                if answer_id == "Yes":
                    Viral_Fever-=1
                    COVID-=1
                    Pneumonia-=1
                    Cholangitis+=1
                    Endocarditis-=0
                    Cellulitis-=1
                    UTI-=1
                    Osteomyelitis-=1
                    Meningitis-=1

            if question_id=="fever_qn11":
                if answer_id == "Yes":
                    Viral_Fever-=1
                    COVID-=1
                    Pneumonia-=0.5
                    Cholangitis+=0.5
                    Endocarditis+=1
                    Cellulitis-=1
                    UTI-=1
                    Osteomyelitis+=1
                    Meningitis-=1

            if question_id=="fever_qn12":
                if answer_id == "Yes":
                    Viral_Fever-=1
                    COVID-=1
                    Pneumonia-=1
                    Cholangitis-=1
                    Endocarditis+=0.5
                    Cellulitis+=1
                    UTI-=1
                    Osteomyelitis+=1
                    Meningitis-=1

            if question_id=="fever_qn13":

                if answer_id == "Yes":
                    Viral_Fever-=1
                    COVID-=1
                    Pneumonia-=1
                    Cholangitis-=1
                    Endocarditis-=1
                    Cellulitis-=1
                    UTI+=1
                    Osteomyelitis-=1
                    Meningitis+=0

            if question_id=="fever_qn14":
                if answer_id == "Yes":
                    Viral_Fever+=0.25
                    COVID+=0.5
                    Pneumonia+=0.5
                    Cholangitis-=1
                    Endocarditis+=0.5
                    Cellulitis-=1
                    UTI+=0
                    Osteomyelitis+=0
                    Meningitis+=1

            if question_id=="fever_qn15":

                if answer_id == "Yes":
                    Viral_Fever-=1
                    COVID+=0.25
                    Pneumonia+=0.25
                    Cholangitis-=1
                    Endocarditis+=0
                    Cellulitis-=1
                    UTI-=1
                    Osteomyelitis-=1
                    Meningitis+=1

            if question_id=="fever_qn16":

                if answer_id == "Yes":
                    Viral_Fever-=1
                    COVID+=0
                    Pneumonia+=0
                    Cholangitis-=1
                    Endocarditis+=0
                    Cellulitis-=1
                    UTI-=1
                    Osteomyelitis-=1
                    Meningitis+=1

        context ={
            "Viral_Fever":Viral_Fever,
            "COVID":COVID,
            "Pneumonia":Pneumonia,
            "Cholangitis":Cholangitis,
            "Endocarditis":Endocarditis,
            "Cellulitis":Cellulitis,
            "UTI":UTI,
            "Osteomyelitis":Osteomyelitis,
            "Meningitis":Meningitis,
        }
        print (context)

        x = sorted(((v,k) for k,v in context.items() if v > 0))
        print ("len of x",len(x))
        if len(x) == 0:
            context2 = {
                "Disease": "No disease found",

                }
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Fever",disease1="Disease",p1="No disease found",last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            request.session['Diagnosis']= "No Disease Found"
            request.session['P1_score']= "0"
            request.session['Diagnosis_type']= "Fever"



            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id
            return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

        if len(x) == 1:
            first_name = x[-1][1]
            first_value = x[-1][0]
            # user_diesease_update = top_disease_user_Fever.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            user_diesease_update = top_disease_user_overall.objects.create(analysistype="Fever",disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
            user_diesease_update.save()

            context2 = {
                first_name: "Most Likely",

                }
            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id

            request.session['Diagnosis']= first_name
            request.session['P1_score']= first_value
            request.session['Diagnosis_type']= "Fever"
            request.session['detailed User message']= "Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined You are likely to have " + first_name +". The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms."

            disease_1= disease_details.objects.get(disease_name=first_name)
            print ("disease_1",disease_1.disease_description)
            context3 = {
                    first_name: disease_1.disease_description,

                }

            print ("disease detail",context3)
            return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


            return render(request,"questionscompleted.html",{'context':context2})

            return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

        if len(x) == 2:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            # user_diesease_update = top_disease_user_Fever.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Fever",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            context2 = {
                first_name: "Most Likely",
                second_name :"Possible",
                }
            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id

            request.session['Diagnosis']= first_name
            request.session['P1_score']= first_value
            request.session['Diagnosis_type']= "Fever"
            request.session['detailed User message']= "Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined You are likely to have " + first_name + " or " + second_name +  ". The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms."

            disease_1= disease_details.objects.get(disease_name=first_name)
            disease_2= disease_details.objects.get(disease_name=second_name)
            print ("disease_1",disease_1.disease_description)
            context3 = {
                    first_name: disease_1.disease_description,
                    second_name :disease_2.disease_description,

                }

            print ("disease detail",context3)
            return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


            return render(request,"questionscompleted.html",{'context':context2})



        if len(x) == 3:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            third_name = x[-3][1]
            third_value = x[-3][0]
            # user_diesease_update = top_disease_user_Fever.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Fever",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            context2 = {
                first_name: "Most Likely",
                second_name :"Likely",
                third_name : "Possible",
                }
            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id

            request.session['Diagnosis']= first_name
            request.session['P1_score']= first_value
            request.session['Diagnosis_type']= "Fever"
            request.session['detailed User message']= "Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined You are likely to have " + first_name + " or " + second_name + " or " + third_name + ". The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms."

            disease_1= disease_details.objects.get(disease_name=first_name)
            disease_2= disease_details.objects.get(disease_name=second_name)
            disease_3= disease_details.objects.get(disease_name=third_name)
            print ("disease_1",disease_1.disease_description)
            context3 = {
                    first_name: disease_1.disease_description,
                    second_name :disease_2.disease_description,
                    third_name : disease_3.disease_description,

                }

            print ("disease detail",context3)
            return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


            return render(request,"questionscompleted.html",{'context':context2})



        if len(x) > 3:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            third_name = x[-3][1]
            third_value = x[-3][0]
            fourth_name = x[-4][1]
            fourth_value = x[-4][0]
            # user_diesease_update = top_disease_user_Fever.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Fever",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()


            print("first_value",first_value)
            print("second_value",second_value)
            print("third_value",third_value)
            print("fourth_value",fourth_value)
            context2 = {
                first_name: "Most Likely",
                second_name :"Very Likely",
                third_name : "Likely",
                fourth_name : "Possible"

            }
            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id
            request.session['Diagnosis']= first_name
            request.session['P1_score']= first_value
            request.session['Diagnosis_type']= "Fever"
            request.session['detailed User message']= "Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined You are likely to have " + first_name + " or " + second_name + " or " + third_name + ". The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms."

            disease_1= disease_details.objects.get(disease_name=first_name)
            disease_2= disease_details.objects.get(disease_name=second_name)
            disease_3= disease_details.objects.get(disease_name=third_name)
            disease_4= disease_details.objects.get(disease_name=fourth_name)
            print ("disease_1",disease_1.disease_description)
            context3 = {
                    first_name: disease_1.disease_description,
                    second_name :disease_2.disease_description,
                    third_name : disease_3.disease_description,
                    fourth_name : disease_4.disease_description

                }

            print ("disease detail",context3)
            return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

    return redirect("signin")


# @login_required(login_url='signin')
def blood_Report_abdominal(request):

    # if request.user.is_authenticated:
    #     user = request.user
        if request.method == 'GET':
            questions = blood_questions.objects.all()
            final_data1=[]
            for l in questions:
                options=[]
                all_option=blood_options_questions.objects.filter(question=l.id)
                for data in all_option:
                    options.append({
                        "options_id":data.id,
                        "options_data":data.option1,
                    })
                final_data1.append({
                            "question_data":l.Question,
                            "question_id":l.id,
                            "option":options,

                        })
            # context = {
            #     "data":final_data1
            # }
            return render(request,"questions.html",{'generalquestionsblood':final_data1})

        if request.method == 'POST':
            global Appendicitis
            global Cholecystitis
            global Cystitis
            global Pyelonephritis
            global Renal_Calculi
            global Diverticulitis
            global Inflammatory_Bowel
            global Irritable_Bowel
            global Pancreatitis
            global Endometriosis
            global Gastritis
            print("Appendicitis",Appendicitis)
            print("Cholecystitis",Cholecystitis)
            print("Cystitis",Cystitis)
            print("Pyelonephritis",Pyelonephritis)
            print("Renal_Calculi",Renal_Calculi)
            print("Diverticulitis",Diverticulitis)
            print("Inflammatory_Bowel",Inflammatory_Bowel)
            print("Irritable_Bowel",Irritable_Bowel)

            print("Pancreatitis",Pancreatitis)
            print("Endometriosis",Endometriosis)
            print("Gastritis",Gastritis)
            for question_id in request.POST:
                answer_id = request.POST[question_id]
                # if question_id != "csrfmiddlewaretoken":
                #     question_answer_save = abdominal_answer_details.objects.create(user=user,Question_id=question_id,Answer_id=answer_id,Diagnosis_name="AbdominalBloodReport",last_date_of_analysis=datetime.datetime.now())
                #     question_answer_save.save()

                    # print ("question_id",question_id)
                    # print ("answer_id",answer_id)

                ####k
                if question_id =="8":
                    if answer_id == "11":
                        # Appendicitis-=1
                        #     Cholecystitis-=1
                        #     Cystitis+=1
                        Pyelonephritis+=1
                        Renal_Calculi+=1
                        Diverticulitis+=1
                        Inflammatory_Bowel+=1
                        #     Irritable_Bowel+=0

                        #     Pancreatitis+=0
                        #     Endometriosis-=1
                        Appendicitis+=1
                        Cholecystitis+=1
                        Cystitis+=1
                ### L M
                if question_id == "9":
                    if answer_id == "13":
                        Appendicitis+=1
                ### U V
                ### N
                if question_id =="10":
                    if answer_id =="14":
                        Cholecystitis+=1
                        Pancreatitis+=1
                ### O
                if question_id =="11":
                    if answer_id =="15":
                        Inflammatory_Bowel+=1
                        Pancreatitis+=1

                ### P
                if question_id =="12":
                    if answer_id =="16":
                        Cholecystitis+=1
                ####Q
                if question_id =="13":
                    if answer_id =="17":
                        Pyelonephritis+=1
                        Renal_Calculi+=1
                ####R
                if question_id =="14":
                    if answer_id =="18":
                        Renal_Calculi+=1
                        Pyelonephritis+=1
            print ("POST")
            context ={

                    "Appendicitis":Appendicitis,
                    "Cholecystitis":Cholecystitis,
                    "Cystitis":Cystitis,
                    "Pyelonephritis":Pyelonephritis,
                    "Renal_Calculi":Renal_Calculi,
                    "Diverticulitis":Diverticulitis,
                    "Inflammatory_Bowel":Inflammatory_Bowel,
                    "Irritable_Bowel":Irritable_Bowel,

                    "Pancreatitis":Pancreatitis,
                    "Endometriosis":Endometriosis,
                    "Gastritis":Gastritis
                }


            x = sorted(((v,k) for k,v in context.items() if v > 0))
            print ("len of x",len(x))
            if len(x) == 0:
                return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

            if len(x) == 1:
                first_name = x[-1][1]
                first_value = x[-1][0]
                # user_diesease_update = top_disease_user_abdominal.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                context2 = {
                    first_name: "Most Likely",

                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                return render(request,"questionscompleted.html",{'context':context2})

                return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

            if len(x) == 2:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                # user_diesease_update = top_disease_user_abdominal.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                context2 = {
                    first_name: "Most Likely",
                    second_name :"Possible",
                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                return render(request,"questionscompleted.html",{'context':context2})



            if len(x) == 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                # user_diesease_update = top_disease_user_abdominal.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                context2 = {
                    first_name: "Most Likely",
                    second_name :"Likely",
                    third_name : "Possible",
                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                disease_3= disease_details.objects.get(disease_name=third_name)

                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,
                        third_name : disease_3.disease_description,


                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                return render(request,"questionscompleted.html",{'context':context2})


                # return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

            if len(x) > 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                fourth_name = x[-4][1]
                fourth_value = x[-4][0]
                # user_diesease_update = top_disease_user_abdominal.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                print("first_value",first_value)
                print("second_value",second_value)
                print("third_value",third_value)
                print("fourth_value",fourth_value)
                context2 = {
                    first_name: "Most Likely",
                    second_name :"Very Likely",
                    third_name : "Likely",
                    fourth_name : "Possible"

                }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                disease_3= disease_details.objects.get(disease_name=third_name)
                disease_4= disease_details.objects.get(disease_name=fourth_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,
                        third_name : disease_3.disease_description,
                        fourth_name : disease_4.disease_description

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                return render(request,"questionscompleted.html",{'context':context2})



#### abdominal pain jotforms####

##### abdominal pain jotforms####

@csrf_exempt
def abdominal_pain(request):
    global Appendicitis
    global Cholecystitis
    global Cystitis
    global Pyelonephritis
    global Renal_Calculi
    global Diverticulitis
    global Inflammatory_Bowel
    global Irritable_Bowel

    global Pancreatitis
    global Endometriosis
    global Gastritis

    if request.method == 'GET':
        return render(request,"abdominal_qn.html" )

    if request.method == 'POST':
            # user=request.user
        print("POST request accepeted and post data is", request.POST)

        Appendicitis= 0
        Cholecystitis= 0
        Cystitis= 0
        Pyelonephritis= 0
        Renal_Calculi= 0
        Diverticulitis= 0
        Inflammatory_Bowel= 0
        Irritable_Bowel= 0

        Pancreatitis= 0
        Endometriosis= 0
        Gastritis = 0

        try:
            qn1=request.POST['abdominal_qn1']
            print("Your Duration of abdominal pain", qn1)
        except:
            qn1 =" "
            pass

        try:
            qn2=request.POST['abdominal_qn2']
            print("Do you have nausea and vomiting?", qn2)
        except:
            qn2 =" "
            pass

        try:
            qn3=request.POST['abdominal_qn3']
            print("Do you have a fever?", qn3)
        except:
            qn3 =" "
            pass

        try:
            qn4=request.POST['abdominal_qn4']
            print("Does it hurt when you pass urine?", qn4)
        except:
            qn4 =" "
            pass

        try:
            qn5=request.POST['abdominal_qn5']
            print("Do you have blood in your urine?",qn5)
        except:
            qn5 =" "
            pass

        try:
            qn6=request.POST['abdominal_qn6']
            print("Are you short of breath?",qn6)
        except:
            qn6 =" "
            pass

        try:
            qn7=request.POST['abdominal_qn7']
            print("Do you have any chest pain?", qn7)
        except:
            qn7 =" "
            pass

        try:
            qn8=request.POST['abdominal_qn8']
            print("Do you have abdominal pain?", qn8)
        except:
            qn8 =" "
            pass

        try:
            qn9=request.POST['abdominal_qn9']
            print("Are your stools black in colour?", qn9)
        except:
            qn9 =" "
            pass

        try:
            qn10=request.POST['abdominal_qn10']
            print("Is the pain related to your periods?", qn10)
        except:
            qn10 =" "
            pass

        try:
            qn11=request.POST['abdominal_qn11']
            print("Have you lost weight?", qn11)
        except:
            qn11 =" "
            pass

        try:
            qn12=request.POST['abdominal_qn12']
            print("Do you feel bloated?", qn12)
        except:
            qn12 =" "
            pass

        try:
            qn13=request.POST['abdominal_qn13']
            print("Do you feel an acidic taste in your mouth?", qn13)
        except:
            qn13 =" "
            pass

        try:
            qn14=request.POST['abdominal_qn14']
            print("Do you drink alcohol?", qn14)
        except:
            qn14 =" "
            pass

        try:
            qn15=request.POST['abdominal_qn15']
            print("Is the pain in the upper part of your abdomen?", qn15)
        except:
            qn15 =" "
            pass




        if qn1== "Less than 1 week":
            Appendicitis+=1
            Cholecystitis+=0.5
            Cystitis+=0.5
            Pyelonephritis+=0.5
            Renal_Calculi+=1
            Diverticulitis+=0.25
            Inflammatory_Bowel+=0.5
            Irritable_Bowel+=0

            Pancreatitis+=0.5
            Endometriosis+=0
            Gastritis +=0.5
        #  (VB-.5, BP1, A.5, CHF0, CLD0, LC0, PE.25)
        if qn1== "More than 1 week":
            Appendicitis-=0.5
            Cholecystitis+=0.5
            Cystitis+=0.5
            Pyelonephritis+=0.5
            Renal_Calculi-=1
            Diverticulitis+=0.75
            Inflammatory_Bowel+=0.5
            Irritable_Bowel+=1

            Pancreatitis+=0.5
            Endometriosis+=1
            Gastritis +=0.5

        if qn2=="Yes":
            Appendicitis+=0.75
            Cholecystitis+=1
            Cystitis+=0
            Pyelonephritis+=0.75
            Renal_Calculi+=0.5
            Diverticulitis+=1
            Inflammatory_Bowel+=0.5
            Irritable_Bowel+=0.5

            Pancreatitis+=1
            Endometriosis+=0
            Gastritis +=0.5

        if qn3=="Yes":
            Appendicitis+=0.75
            Cholecystitis+=1
            Cystitis+=0.5
            Pyelonephritis+=1
            Renal_Calculi+=0
            Diverticulitis+=0.75
            Inflammatory_Bowel+=0.75
            Irritable_Bowel-=1

            Pancreatitis+=0.5
            Endometriosis-=1
            Gastritis-=1

        if qn4=="Yes":
            Appendicitis-=1
            Cholecystitis-=1
            Cystitis+=1
            Pyelonephritis+=1
            Renal_Calculi+=1
            Diverticulitis+=0
            Inflammatory_Bowel+=0
            Irritable_Bowel+=0
            Pancreatitis-=1
            Endometriosis+=0.5
            Gastritis-=1

        if qn5=="Yes":
            Appendicitis-=1
            Cholecystitis-=1
            Cystitis+=1
            Pyelonephritis+=1
            Renal_Calculi+=1
            Diverticulitis-=1
            Inflammatory_Bowel-=1
            Irritable_Bowel-=1
            Pancreatitis-=1
            Endometriosis-=1
            Gastritis-=1

        if qn6=="Yes":
            Appendicitis+=0.5
            Cholecystitis+=0.5
            Cystitis+=0.5
            Pyelonephritis+=0.5
            Renal_Calculi+=0.5
            Diverticulitis+=1
            Inflammatory_Bowel+=1
            Irritable_Bowel+=1
            Pancreatitis+=0.5
            Endometriosis+=0.5
            Gastritis-=1

        if qn7=="Yes":
            Appendicitis-=0.5
            Cholecystitis-=0.5
            Cystitis-=1
            Pyelonephritis-=1
            Renal_Calculi-=1
            Diverticulitis+=0.75
            Inflammatory_Bowel+=1
            Irritable_Bowel-=1
            Pancreatitis+=0
            Endometriosis-=1
            Gastritis-=1

        if qn8=="Yes":
            Appendicitis+=0.25
            Cholecystitis+=0
            Cystitis-=1
            Pyelonephritis-=1
            Renal_Calculi-=1
            Diverticulitis+=0.5
            Inflammatory_Bowel+=1
            Irritable_Bowel-=1
            Pancreatitis+=0.5
            Endometriosis-=1
            Gastritis-=1

        if qn9=="Yes":
            Appendicitis-=1
            Cholecystitis-=1
            Cystitis-=1
            Pyelonephritis-=1
            Renal_Calculi-=1
            Diverticulitis-=1
            Inflammatory_Bowel-=1
            Irritable_Bowel-=1
            Pancreatitis-=1
            Endometriosis+=1
            Gastritis-=1

        if qn10=="Yes":
            Appendicitis-=1
            Cholecystitis-=0.5
            Cystitis-=1
            Pyelonephritis-=1
            Renal_Calculi-=1
            Diverticulitis+=0.5
            Inflammatory_Bowel+=1
            Irritable_Bowel-=1
            Pancreatitis+=0.75
            Endometriosis-=1
            Gastritis-=1

        if qn11=="Yes":
            Appendicitis+=0.5
            Cholecystitis+=0.5
            Cystitis+=0.25
            Pyelonephritis+=0.25
            Renal_Calculi+=0.25
            Diverticulitis+=1
            Inflammatory_Bowel+=1
            Irritable_Bowel+=1
            Pancreatitis+=0.5
            Endometriosis+=0.5
            Gastritis+=0.5

        if qn12=="Yes":
            Appendicitis-=1
            Cholecystitis-=1
            Cystitis-=1
            Pyelonephritis-=1
            Renal_Calculi-=1
            Diverticulitis+=0
            Inflammatory_Bowel+=0
            Irritable_Bowel+=0
            Pancreatitis+=0
            Endometriosis-=1
            Gastritis+=1

        if qn13=="Yes":
            Appendicitis+=0
            Cholecystitis+=0.5
            Cystitis+=0
            Pyelonephritis+=0
            Renal_Calculi+=0
            Diverticulitis+=0
            Inflammatory_Bowel+=0
            Irritable_Bowel+=0
            Pancreatitis+=1
            Endometriosis+=0
            Gastritis+=0.5

        if qn14=="Yes":
            Appendicitis-=1
            Cholecystitis+=1
            Cystitis-=1
            Pyelonephritis+=0.5
            Renal_Calculi+=0.5
            Diverticulitis-=1
            Inflammatory_Bowel-=1
            Irritable_Bowel-=1
            Pancreatitis+=1
            Endometriosis+=1
            Gastritis+=1

        if qn15=="Yes":
            Appendicitis+=1
            Cholecystitis-=1
            Cystitis+=1
            Pyelonephritis+=0.5
            Renal_Calculi+=0.5
            Diverticulitis+=1
            Inflammatory_Bowel+=1
            Irritable_Bowel+=1
            Pancreatitis-=0.5
            Endometriosis+=1
            Gastritis-=1


        context ={

            "Appendicitis":Appendicitis,
            "Cholecystitis":Cholecystitis,
            "Cystitis":Cystitis,
            "Pyelonephritis":Pyelonephritis,
            "Renal_Calculi":Renal_Calculi,
            "Diverticulitis":Diverticulitis,
            "Inflammatory_Bowel":Inflammatory_Bowel,
            "Irritable_Bowel":Irritable_Bowel,
            "Pancreatitis":Pancreatitis,
            "Endometriosis":Endometriosis,
            "Gastritis":Gastritis
        }


        # x = sorted(((v,k) for k,v in context.items()))

        x = sorted(((v,k) for k,v in context.items() if v > 0))
        print ("len of x",len(x))
        if len(x) == 0:
            context2 = {
                "Disease": "No disease found",

                }
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Abdominal", disease1="Disease",p1="No disease found",last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            request.session['Diagnosis']= "No disease"
            request.session['P1_score']= "0"
            request.session['Diagnosis_type']= "Abdominal"

            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id
            return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

        if len(x) == 1:
            first_name = x[-1][1]
            first_value = x[-1][0]
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Abdominal", disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            # user_diesease_update = top_disease_user_abdominal.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            context2 = {
                first_name: "Most Likely",

                }

            request.session['Diagnosis']= first_name
            request.session['P1_score']= first_value
            request.session['Diagnosis_type']= "Abdominal"

            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id
            request.session['detailed User message']= "Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined You are likely to have " + first_name + ". The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms."
            disease_1= disease_details.objects.get(disease_name=first_name)
            print ("disease_1",disease_1.disease_description)
            context3 = {
                    first_name: disease_1.disease_description,
                }

            print ("disease detail",context3)
            return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

        if len(x) == 2:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            # user_diesease_update = top_disease_user_abdominal.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Abdominal",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            context2 = {
                first_name: "Most Likely",
                second_name :"Possible",
                }

            request.session['Diagnosis']= first_name
            request.session['P1_score']= first_value
            request.session['Diagnosis_type']= "Abdominal"

            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id
            request.session['detailed User message']= "Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined You are likely to have " + first_name + " , " + second_name + ". The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms."
            disease_1= disease_details.objects.get(disease_name=first_name)
            disease_2= disease_details.objects.get(disease_name=second_name)
            print ("disease_1",disease_1.disease_description)
            context3 = {
                    first_name: disease_1.disease_description,
                    second_name :disease_2.disease_description,

                }

            print ("disease detail",context3)
            return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

        if len(x) == 3:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            third_name = x[-3][1]
            third_value = x[-3][0]
            # user_diesease_update = top_disease_user_abdominal.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Abdominal",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            context2 = {
                first_name: "Most Likely",
                second_name :"Likely",
                third_name : "Possible",
                }
            request.session['Diagnosis']= first_name
            request.session['P1_score']= first_value
            request.session['Diagnosis_type']= "Abdominal"

            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id
            request.session['detailed User message']= "Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined You are likely to have " + first_name + " , " + second_name + " or " + third_name +  ". The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms."
            disease_1= disease_details.objects.get(disease_name=first_name)
            disease_2= disease_details.objects.get(disease_name=second_name)
            disease_3= disease_details.objects.get(disease_name=third_name)

            print ("disease_1",disease_1.disease_description)
            context3 = {
                    first_name: disease_1.disease_description,
                    second_name :disease_2.disease_description,
                    third_name : disease_3.disease_description,


                }

            print ("disease detail",context3)
            return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

            return render(request,"questionscompleted.html",{'context':context2})

        if len(x) > 3:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            third_name = x[-3][1]
            third_value = x[-3][0]
            fourth_name = x[-4][1]
            fourth_value = x[-4][0]
            # user_diesease_update = top_disease_user_abdominal.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Abdominal",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            print("first_value",first_value)
            print("second_value",second_value)
            print("third_value",third_value)
            print("fourth_value",fourth_value)
            context2 = {
                first_name: "Most Likely",
                second_name :"Very Likely",
                third_name : "Likely",
                fourth_name : "Possible"

            }
            request.session['Diagnosis']= first_name
            request.session['P1_score']= first_value
            request.session['Diagnosis_type']= "Abdominal"
            request.session['detailed User message']= "Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined You are likely to have " + first_name + " , " + second_name + " or " + third_name +  ". The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms."
            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id


            disease_1= disease_details.objects.get(disease_name=first_name)
            disease_2= disease_details.objects.get(disease_name=second_name)
            disease_3= disease_details.objects.get(disease_name=third_name)
            disease_4= disease_details.objects.get(disease_name=fourth_name)
            print ("disease_1",disease_1.disease_description)
            context3 = {
                    first_name: disease_1.disease_description,
                    second_name :disease_2.disease_description,
                    third_name : disease_3.disease_description,
                    fourth_name : disease_4.disease_description

                }


            print ("disease detail",context3)

            return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


        return render (request,"thanks_page.html")

    return redirect("signin")



# @login_required(login_url='signin')
def abdominal_question(request):
        global Appendicitis
        global Cholecystitis
        global Cystitis
        global Pyelonephritis
        global Renal_Calculi
        global Diverticulitis
        global Inflammatory_Bowel
        global Irritable_Bowel

        global Pancreatitis
        global Endometriosis
        global Gastritis

        # if request.user.is_authenticated:
        #     user = request.user
        if request.method == 'GET':
            questions = abdominal_questions.objects.all()
            final_data1=[]
            for l in questions:
                options=[]
                all_option=abdominal_options_questions.objects.filter(question=l.id)
                for data in all_option:
                    options.append({
                        "options_id":data.id,
                        "options_data":data.option1,
                    })
                final_data1.append({
                            "question_data":l.Question,
                            "question_id":l.id,
                            "option":options,

                        })

            return render(request,"questions.html",{'generalquestions':final_data1})
        if request.method == 'POST':
            # user=request.user

            Appendicitis= 0
            Cholecystitis= 0
            Cystitis= 0
            Pyelonephritis= 0
            Renal_Calculi= 0
            Diverticulitis= 0
            Inflammatory_Bowel= 0
            Irritable_Bowel= 0

            Pancreatitis= 0
            Endometriosis= 0
            Gastritis = 0

            for question_id in request.POST:
                answer_id = request.POST[question_id]

                # if question_id != "csrfmiddlewaretoken":
                #     question_answer_save = abdominal_answer_details.objects.create(user=user,Question_id=question_id,Answer_id=answer_id,Diagnosis_name="Abdominal",last_date_of_analysis=datetime.datetime.now())
                #     question_answer_save.save()
                #     print ("question_id",question_id)
                #     print ("answer_id",answer_id)
                if question_id == "1":

                    # (VB1, BP.25, A.5, CHF-1, CLD-1, LC-1, PE.75)
                    if answer_id == "1":
                        Appendicitis+=1
                        Cholecystitis+=0.5
                        Cystitis+=0.5
                        Pyelonephritis+=0.5
                        Renal_Calculi+=1
                        Diverticulitis+=0.25
                        Inflammatory_Bowel+=0.5
                        Irritable_Bowel+=0

                        Pancreatitis+=0.5
                        Endometriosis+=0
                        Gastritis +=0.5
                    #  (VB-.5, BP1, A.5, CHF0, CLD0, LC0, PE.25)
                    if answer_id == "2":
                        Appendicitis-=0.5
                        Cholecystitis+=0.5
                        Cystitis+=0.5
                        Pyelonephritis+=0.5
                        Renal_Calculi-=1
                        Diverticulitis+=0.75
                        Inflammatory_Bowel+=0.5
                        Irritable_Bowel+=1

                        Pancreatitis+=0.5
                        Endometriosis+=1
                        Gastritis +=0.5

                if question_id == "2":
                    # (VB1, BP.25, A.5, CHF-1, CLD-1, LC-1, PE.75)
                    if answer_id == "3":
                        Appendicitis+=0.75
                        Cholecystitis+=1
                        Cystitis+=0
                        Pyelonephritis+=0.75
                        Renal_Calculi+=0.5
                        Diverticulitis+=1
                        Inflammatory_Bowel+=0.5
                        Irritable_Bowel+=0.5

                        Pancreatitis+=1
                        Endometriosis+=0
                        Gastritis +=0.5

                if question_id =="3" :

                    if answer_id == "5":
                        Appendicitis+=0.75
                        Cholecystitis+=1
                        Cystitis+=0.5
                        Pyelonephritis+=1
                        Renal_Calculi+=0
                        Diverticulitis+=0.75
                        Inflammatory_Bowel+=0.75
                        Irritable_Bowel-=1

                        Pancreatitis+=0.5
                        Endometriosis-=1
                        Gastritis-=1

                if question_id =="4":
                    if answer_id == "7":
                        Appendicitis-=1
                        Cholecystitis-=1
                        Cystitis+=1
                        Pyelonephritis+=1
                        Renal_Calculi+=1
                        Diverticulitis+=0
                        Inflammatory_Bowel+=0
                        Irritable_Bowel+=0
                        Pancreatitis-=1
                        Endometriosis+=0.5
                        Gastritis-=1

                if question_id == "5":
                    if answer_id == "9":
                        Appendicitis-=1
                        Cholecystitis-=1
                        Cystitis+=1
                        Pyelonephritis+=1
                        Renal_Calculi+=1
                        Diverticulitis-=1
                        Inflammatory_Bowel-=1
                        Irritable_Bowel-=1
                        Pancreatitis-=1
                        Endometriosis-=1
                        Gastritis-=1

                if question_id =="6":
                    if answer_id == "11":
                        Appendicitis+=0.5
                        Cholecystitis+=0.5
                        Cystitis+=0.5
                        Pyelonephritis+=0.5
                        Renal_Calculi+=0.5
                        Diverticulitis+=1
                        Inflammatory_Bowel+=1
                        Irritable_Bowel+=1
                        Pancreatitis+=0.5
                        Endometriosis+=0.5
                        Gastritis-=1

                if question_id=="7":

                    if answer_id == "13":
                        Appendicitis-=0.5
                        Cholecystitis-=0.5
                        Cystitis-=1
                        Pyelonephritis-=1
                        Renal_Calculi-=1
                        Diverticulitis+=0.75
                        Inflammatory_Bowel+=1
                        Irritable_Bowel-=1
                        Pancreatitis+=0
                        Endometriosis-=1
                        Gastritis-=1

                if question_id=="8":

                    if answer_id == "15":
                        Appendicitis+=0.25
                        Cholecystitis+=0
                        Cystitis-=1
                        Pyelonephritis-=1
                        Renal_Calculi-=1
                        Diverticulitis+=0.5
                        Inflammatory_Bowel+=1
                        Irritable_Bowel-=1
                        Pancreatitis+=0.5
                        Endometriosis-=1
                        Gastritis-=1

                if question_id=="9":
                    # •	Yes (VB.25, BP.5, A.5, CHF1, CLD1, LC1, PE1)
                    if answer_id == "17":
                        Appendicitis-=1
                        Cholecystitis-=1
                        Cystitis-=1
                        Pyelonephritis-=1
                        Renal_Calculi-=1
                        Diverticulitis-=1
                        Inflammatory_Bowel-=1
                        Irritable_Bowel-=1
                        Pancreatitis-=1
                        Endometriosis+=1
                        Gastritis-=1

                if question_id=="10":

                    if answer_id == "19":
                        Appendicitis-=1
                        Cholecystitis-=0.5
                        Cystitis-=1
                        Pyelonephritis-=1
                        Renal_Calculi-=1
                        Diverticulitis+=0.5
                        Inflammatory_Bowel+=1
                        Irritable_Bowel-=1
                        Pancreatitis+=0.75
                        Endometriosis-=1
                        Gastritis-=1

                if question_id=="11":
                    # •	Yes (VB.25, BP.5, A.5, CHF1, CLD1, LC1, PE1)
                    if answer_id == "21":
                        Appendicitis+=0.5
                        Cholecystitis+=0.5
                        Cystitis+=0.25
                        Pyelonephritis+=0.25
                        Renal_Calculi+=0.25
                        Diverticulitis+=1
                        Inflammatory_Bowel+=1
                        Irritable_Bowel+=1
                        Pancreatitis+=0.5
                        Endometriosis+=0.5
                        Gastritis+=0.5

                if question_id=="12":

                    if answer_id == "23":
                        Appendicitis-=1
                        Cholecystitis-=1
                        Cystitis-=1
                        Pyelonephritis-=1
                        Renal_Calculi-=1
                        Diverticulitis+=0
                        Inflammatory_Bowel+=0
                        Irritable_Bowel+=0
                        Pancreatitis+=0
                        Endometriosis-=1
                        Gastritis+=1

                if question_id=="13":

                    if answer_id == "25":
                        Appendicitis+=0
                        Cholecystitis+=0.5
                        Cystitis+=0
                        Pyelonephritis+=0
                        Renal_Calculi+=0
                        Diverticulitis+=0
                        Inflammatory_Bowel+=0
                        Irritable_Bowel+=0
                        Pancreatitis+=1
                        Endometriosis+=0
                        Gastritis+=0.5

                if question_id=="14":
                    if answer_id == "27":
                        Appendicitis-=1
                        Cholecystitis+=1
                        Cystitis-=1
                        Pyelonephritis+=0.5
                        Renal_Calculi+=0.5
                        Diverticulitis-=1
                        Inflammatory_Bowel-=1
                        Irritable_Bowel-=1
                        Pancreatitis+=1
                        Endometriosis+=1
                        Gastritis+=1

                if question_id=="15":

                    if answer_id == "29":
                        Appendicitis+=1
                        Cholecystitis-=1
                        Cystitis+=1
                        Pyelonephritis+=0.5
                        Renal_Calculi+=0.5
                        Diverticulitis+=1
                        Inflammatory_Bowel+=1
                        Irritable_Bowel+=1
                        Pancreatitis-=0.5
                        Endometriosis+=1
                        Gastritis-=1


            context ={

                "Appendicitis":Appendicitis,
                "Cholecystitis":Cholecystitis,
                "Cystitis":Cystitis,
                "Pyelonephritis":Pyelonephritis,
                "Renal_Calculi":Renal_Calculi,
                "Diverticulitis":Diverticulitis,
                "Inflammatory_Bowel":Inflammatory_Bowel,
                "Irritable_Bowel":Irritable_Bowel,
                "Pancreatitis":Pancreatitis,
                "Endometriosis":Endometriosis,
                "Gastritis":Gastritis
            }


            x = sorted(((v,k) for k,v in context.items()))
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            third_name = x[-3][1]
            third_value = x[-3][0]
            fourth_name = x[-4][1]
            fourth_value = x[-4][0]

            print("first_value",first_value)
            print("second_value",second_value)
            print("third_value",third_value)
            print("fourth_value",fourth_value)
            context2 = {
                first_name: first_value,
                second_name :second_value,
                third_name : third_value,
                fourth_name : fourth_value

            }
            print (context)
            # user_diesease_update = disease_user.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now(),diagnosisname="Abdominal Pain")
            # user_diesease_update.save()
            # return render(request,"questionscompleted.html",{'context':context2})
            # return redirect("blood_Report_abdominal")
            return render (request,"thanks_page.html")

        return redirect("signin")



# @login_required(login_url='signin') just for apis
def blood_question(request):

    url = "http://3.0.91.137/n/details/"
    response = requests.post(url)
    print ("response",response)
    data = response.json()
    print ("ok")
    data = (data['Questions'])
    # print ("ok",data)
    # for x in data['Questions']['option']:
    #     print ("data in for loop",x)


    print (len(data))
    for data in data:
        print (data['option']['PRODUCT'])
        INFORMATIONS =  Nutrient_Information.objects.create(PRODUCT=data['option']['PRODUCT'],CATEGORY=data['option']['CATEGORY'],CALORIE=data['option']['CALORIE'],CARB=data['option']['CARB'],PRO=data['option']['PRO'],FAT=data['option']['FAT'],Ex_Swim=data['option']['Ex_Swim'],Ex_Jog=data['option']['Ex_Jog'],Ex_Cycle=data['option']['Ex_Cycle'],Ex_Walk=data['option']['Ex_Walk'])
        INFORMATIONS.save()
    # print ("Data",data)
    return JsonResponse({"Questions":response.json()},safe=False)

# @login_required(login_url='signin')
def Abdominal_options(request):
    # if request.user.is_authenticated:
    #     user = request.user
        if request.method == 'GET':
            return render(request,"thanks_page.html")

        if request.method == 'POST':

            some_var = request.POST.getlist('checks[]')
            print ("some_var issssss" , len(some_var))
            print ("some_var isssss" , some_var)

            context ={

                    "Appendicitis":Appendicitis,
                    "Cholecystitis":Cholecystitis,
                    "Cystitis":Cystitis,
                    "Pyelonephritis":Pyelonephritis,
                    "Renal_Calculi":Renal_Calculi,
                    "Diverticulitis":Diverticulitis,
                    "Inflammatory_Bowel":Inflammatory_Bowel,
                    "Irritable_Bowel":Irritable_Bowel,
                    "Pancreatitis":Pancreatitis,
                    "Endometriosis":Endometriosis,
                    "Gastritis":Gastritis
                }
            if len(some_var) ==0:
                print("i am checking to length is 0")

                x = sorted(((v,k) for k,v in context.items() if v > 0))
                print ("len of x",len(x))
                if len(x) == 0:
                    return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

                if len(x) == 1:
                    first_name = x[-1][1]
                    first_value = x[-1][0]
                    # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Abdominal", disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    # user_diesease_update = top_disease_user_abdominal.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()
                    context2 = {
                        first_name: "Most Likely",

                        }
                    disease_1= disease_details.objects.get(disease_name=first_name)
                    print ("disease_1",disease_1.disease_description)
                    context3 = {
                            first_name: disease_1.disease_description,
                        }

                    print ("disease detail",context3)
                    return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                    return render(request,"questionscompleted.html",{'context':context2})

                    return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

                if len(x) == 2:
                    first_name = x[-1][1]
                    first_value = x[-1][0]
                    second_name = x[-2][1]
                    second_value = x[-2][0]
                    # user_diesease_update = top_disease_user_abdominal.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()
                    # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Abdominal",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    context2 = {
                        first_name: "Most Likely",
                        second_name :"Possible",
                        }
                    disease_1= disease_details.objects.get(disease_name=first_name)
                    disease_2= disease_details.objects.get(disease_name=second_name)
                    print ("disease_1",disease_1.disease_description)
                    context3 = {
                            first_name: disease_1.disease_description,
                            second_name :disease_2.disease_description,

                        }

                    print ("disease detail",context3)
                    return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                    return render(request,"questionscompleted.html",{'context':context2})



                if len(x) == 3:
                    first_name = x[-1][1]
                    first_value = x[-1][0]
                    second_name = x[-2][1]
                    second_value = x[-2][0]
                    third_name = x[-3][1]
                    third_value = x[-3][0]
                    # user_diesease_update = top_disease_user_abdominal.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()
                    # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Abdominal",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    context2 = {
                        first_name: "Most Likely",
                        second_name :"Likely",
                        third_name : "Possible",
                        }
                    disease_1= disease_details.objects.get(disease_name=first_name)
                    disease_2= disease_details.objects.get(disease_name=second_name)
                    disease_3= disease_details.objects.get(disease_name=third_name)

                    print ("disease_1",disease_1.disease_description)
                    context3 = {
                            first_name: disease_1.disease_description,
                            second_name :disease_2.disease_description,
                            third_name : disease_3.disease_description,


                        }

                    print ("disease detail",context3)
                    return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                    return render(request,"questionscompleted.html",{'context':context2})

                if len(x) > 3:
                    first_name = x[-1][1]
                    first_value = x[-1][0]
                    second_name = x[-2][1]
                    second_value = x[-2][0]
                    third_name = x[-3][1]
                    third_value = x[-3][0]
                    fourth_name = x[-4][1]
                    fourth_value = x[-4][0]
                    # user_diesease_update = top_disease_user_abdominal.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()
                    # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Abdominal",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    print("first_value",first_value)
                    print("second_value",second_value)
                    print("third_value",third_value)
                    print("fourth_value",fourth_value)
                    context2 = {
                        first_name: "Most Likely",
                        second_name :"Very Likely",
                        third_name : "Likely",
                        fourth_name : "Possible"

                    }
                    disease_1= disease_details.objects.get(disease_name=first_name)
                    disease_2= disease_details.objects.get(disease_name=second_name)
                    disease_3= disease_details.objects.get(disease_name=third_name)
                    disease_4= disease_details.objects.get(disease_name=fourth_name)
                    print ("disease_1",disease_1.disease_description)
                    context3 = {
                            first_name: disease_1.disease_description,
                            second_name :disease_2.disease_description,
                            third_name : disease_3.disease_description,
                            fourth_name : disease_4.disease_description

                        }

                    print ("disease detail",context3)
                    return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                    return render(request,"questionscompleted.html",{'context':context2})



            for op1 in some_var:
                if op1== "1":
                    return redirect("Choose_Abdominal_blood_test")

        return render(request,"thanks_page.html")

# @login_required(login_url='signin')
def Choose_Abdominal_blood_test(request):
    global num


    # if request.user.is_authenticated:
    #     user = request.user
    if request.method == 'GET':
        return render(request,"Choose_bloodtest.html")

    if request.method == 'POST':
        check_var = request.POST.getlist('checks[]')
        print ("some_var" , len(check_var))
        print ("some_var" , check_var)

        context ={

                "Appendicitis":Appendicitis,
                "Cholecystitis":Cholecystitis,
                "Cystitis":Cystitis,
                "Pyelonephritis":Pyelonephritis,
                "Renal_Calculi":Renal_Calculi,
                "Diverticulitis":Diverticulitis,
                "Inflammatory_Bowel":Inflammatory_Bowel,
                "Irritable_Bowel":Irritable_Bowel,
                "Pancreatitis":Pancreatitis,
                "Endometriosis":Endometriosis,
                "Gastritis":Gastritis
            }
        if len(check_var) ==0:
            print("i am checking to length is 0")

            x = sorted(((v,k) for k,v in context.items() if v > 0))
            print ("len of x",len(x))
            if len(x) == 0:
                return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

            if len(x) == 1:
                first_name = x[-1][1]
                first_value = x[-1][0]
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Abdominal", disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                # user_diesease_update = top_disease_user_abdominal.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                context2 = {
                    first_name: "Most Likely",

                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})

                return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

            if len(x) == 2:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                # user_diesease_update = top_disease_user_abdominal.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Abdominal",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",
                    second_name :"Possible",
                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})



            if len(x) == 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                # user_diesease_update = top_disease_user_abdominal.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Abdominal",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",
                    second_name :"Likely",
                    third_name : "Possible",
                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                disease_3= disease_details.objects.get(disease_name=third_name)

                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,
                        third_name : disease_3.disease_description,


                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})

            if len(x) > 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                fourth_name = x[-4][1]
                fourth_value = x[-4][0]
                # user_diesease_update = top_disease_user_abdominal.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Abdominal",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                print("first_value",first_value)
                print("second_value",second_value)
                print("third_value",third_value)
                print("fourth_value",fourth_value)
                context2 = {
                    first_name: "Most Likely",
                    second_name :"Very Likely",
                    third_name : "Likely",
                    fourth_name : "Possible"

                }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                disease_3= disease_details.objects.get(disease_name=third_name)
                disease_4= disease_details.objects.get(disease_name=fourth_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,
                        third_name : disease_3.disease_description,
                        fourth_name : disease_4.disease_description

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})


        num=[]
        for i in check_var:
            num.append(i)
            print("num list is" ,i)

        return redirect("Abdominal_blood")

    return render(request,"thanks_page.html")

# @login_required(login_url='signin')
def Abdominal_blood(request):

    # if request.user.is_authenticated:
    #     user = request.user
        if request.method == 'GET':

            q1= [7,8,9]
            q2= [13,14,15,16,17]
            q3= [10,11,12]
            q4= [5,6]
            q5= [1,2,3]
            q6= [4]
            merge_qn=[]
            for p in num:

                if p=="1":
                    for q in q1:
                        merge_qn.append(q)

                if p=="2":
                    for q in q2:
                        merge_qn.append(q)

                if p=="3":
                    for q in q3:
                        merge_qn.append(q)

                if p=="4":
                    for q in q4:
                        merge_qn.append(q)

                if p=="5":
                    for q in q5:
                        merge_qn.append(q)

                if p=="6":
                    for q in q6:
                        merge_qn.append(q)

            print("merge_qn" ,merge_qn)

            final_data1=[]
            for a in merge_qn:
                questions = blood_questions.objects.filter(id=a)
                print("questions are", questions)

                for l in questions:
                    options=[]
                    all_option=blood_options_questions.objects.filter(question=l.id)
                    for data in all_option:
                        options.append({
                            "options_id":data.id,
                            "options_data":data.option1,
                        })
                final_data1.append({
                            "question_data":l.Question,
                            "question_id":l.id,
                            "option":options,

                        })


            return render(request,"bloodtest.html",{'context7':final_data1})

        if request.method == 'POST':
            print ("shdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
            global Appendicitis
            global Cholecystitis
            global Cystitis
            global Pyelonephritis
            global Renal_Calculi
            global Diverticulitis
            global Inflammatory_Bowel
            global Irritable_Bowel
            global Pancreatitis
            global Endometriosis
            global Gastritis
            print("Appendicitis",Appendicitis)
            print("Cholecystitis",Cholecystitis)
            print("Cystitis",Cystitis)
            print("Pyelonephritis",Pyelonephritis)
            print("Renal_Calculi",Renal_Calculi)
            print("Diverticulitis",Diverticulitis)
            print("Inflammatory_Bowel",Inflammatory_Bowel)
            print("Irritable_Bowel",Irritable_Bowel)

            print("Pancreatitis",Pancreatitis)
            print("Endometriosis",Endometriosis)
            print("Gastritis",Gastritis)
            for question_id in request.POST:
                answer_id = request.POST[question_id]
                # if question_id != "csrfmiddlewaretoken":
                #     question_answer_save = abdominal_answer_details.objects.create(user=user,Question_id=question_id,Answer_id=answer_id,Diagnosis_name="AbdominalBloodReport",last_date_of_analysis=datetime.datetime.now())
                #     question_answer_save.save()

                #     print ("question_id",question_id)
                #     print ("answer_id",answer_id)

                ####k
                if question_id =="8":
                    if answer_id == "11":
                        # Appendicitis-=1
                        #     Cholecystitis-=1
                        #     Cystitis+=1
                        Pyelonephritis+=1
                        Renal_Calculi+=1
                        Diverticulitis+=1
                        Inflammatory_Bowel+=1
                        #     Irritable_Bowel+=0

                        #     Pancreatitis+=0
                        #     Endometriosis-=1
                        Appendicitis+=1
                        Cholecystitis+=1
                        Cystitis+=1
                ### L M
                if question_id == "9":
                    if answer_id == "13":
                        Appendicitis+=1
                ### U V
                ### N
                if question_id =="10":
                    if answer_id =="14":
                        Cholecystitis+=1
                        Pancreatitis+=1
                ### O
                if question_id =="11":
                    if answer_id =="15":
                        Inflammatory_Bowel+=1
                        Pancreatitis+=1

                ### P
                if question_id =="12":
                    if answer_id =="16":
                        Cholecystitis+=1
                ####Q
                if question_id =="13":
                    if answer_id =="17":
                        Pyelonephritis+=1
                        Renal_Calculi+=1
                ####R
                if question_id =="14":
                    if answer_id =="18":
                        Renal_Calculi+=1
                        Pyelonephritis+=1
            print ("POST")
            context ={

                    "Appendicitis":Appendicitis,
                    "Cholecystitis":Cholecystitis,
                    "Cystitis":Cystitis,
                    "Pyelonephritis":Pyelonephritis,
                    "Renal_Calculi":Renal_Calculi,
                    "Diverticulitis":Diverticulitis,
                    "Inflammatory_Bowel":Inflammatory_Bowel,
                    "Irritable_Bowel":Irritable_Bowel,

                    "Pancreatitis":Pancreatitis,
                    "Endometriosis":Endometriosis,
                    "Gastritis":Gastritis
                }


            x = sorted(((v,k) for k,v in context.items() if v > 0))
            print ("len of x",len(x))
            if len(x) == 0:
                return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

            if len(x) == 1:
                first_name = x[-1][1]
                first_value = x[-1][0]
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Abdominal", disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                # user_diesease_update = top_disease_user_abdominal.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                context2 = {
                    first_name: "Most Likely",

                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})

                return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

            if len(x) == 2:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                # user_diesease_update = top_disease_user_abdominal.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Abdominal",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",
                    second_name :"Possible",
                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})



            if len(x) == 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                # user_diesease_update = top_disease_user_abdominal.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Abdominal",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",
                    second_name :"Likely",
                    third_name : "Possible",
                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                disease_3= disease_details.objects.get(disease_name=third_name)

                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,
                        third_name : disease_3.disease_description,


                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})

            if len(x) > 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                fourth_name = x[-4][1]
                fourth_value = x[-4][0]
                # user_diesease_update = top_disease_user_abdominal.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Abdominal",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                print("first_value",first_value)
                print("second_value",second_value)
                print("third_value",third_value)
                print("fourth_value",fourth_value)
                context2 = {
                    first_name: "Most Likely",
                    second_name :"Very Likely",
                    third_name : "Likely",
                    fourth_name : "Possible"

                }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                disease_3= disease_details.objects.get(disease_name=third_name)
                disease_4= disease_details.objects.get(disease_name=fourth_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,
                        third_name : disease_3.disease_description,
                        fourth_name : disease_4.disease_description

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                return render(request,"questionscompleted.html",{'context':context2})


# @login_required(login_url='signin')
def fever_options(request):
    # if request.user.is_authenticated:
    #     user = request.user
        if request.method == 'GET':
            return render(request,"thanks_page_fever.html")

        if request.method == 'POST':
            print("I am checking values are not getting or not")
            some_var = request.POST.getlist('checks[]')
            print ("some_var issssss" , len(some_var))
            print ("some_var isssss" , some_var)
            context ={
                "Viral_Fever":Viral_Fever,
                "COVID":COVID,
                "Pneumonia":Pneumonia,
                "Cholangitis":Cholangitis,
                "Endocarditis":Endocarditis,
                "Cellulitis":Cellulitis,
                "UTI":UTI,
                "Osteomyelitis":Osteomyelitis,
                "Meningitis":Meningitis,
            }

            if len(some_var) ==0:
                print("i am checking to length is 0")

                x = sorted(((v,k) for k,v in context.items() if v > 0))
                print ("len of x",len(x))
                if len(x) == 0:
                    return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

                if len(x) == 1:
                    first_name = x[-1][1]
                    first_value = x[-1][0]
                    # user_diesease_update = top_disease_user_Fever.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Fever",disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    context2 = {
                        first_name: "Most Likely",

                        }
                    disease_1= disease_details.objects.get(disease_name=first_name)
                    print ("disease_1",disease_1.disease_description)
                    context3 = {
                            first_name: disease_1.disease_description,

                        }

                    print ("disease detail",context3)
                    return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                    return render(request,"questionscompleted.html",{'context':context2})

                    return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

                if len(x) == 2:
                    first_name = x[-1][1]
                    first_value = x[-1][0]
                    second_name = x[-2][1]
                    second_value = x[-2][0]
                    # user_diesease_update = top_disease_user_Fever.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Fever",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    context2 = {
                        first_name: "Most Likely",
                        second_name :"Possible",
                        }
                    disease_1= disease_details.objects.get(disease_name=first_name)
                    disease_2= disease_details.objects.get(disease_name=second_name)
                    print ("disease_1",disease_1.disease_description)
                    context3 = {
                            first_name: disease_1.disease_description,
                            second_name :disease_2.disease_description,

                        }

                    print ("disease detail",context3)
                    return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                    return render(request,"questionscompleted.html",{'context':context2})



                if len(x) == 3:
                    first_name = x[-1][1]
                    first_value = x[-1][0]
                    second_name = x[-2][1]
                    second_value = x[-2][0]
                    third_name = x[-3][1]
                    third_value = x[-3][0]
                    # user_diesease_update = top_disease_user_Fever.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Fever",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    context2 = {
                        first_name: "Most Likely",
                        second_name :"Likely",
                        third_name : "Possible",
                        }
                    disease_1= disease_details.objects.get(disease_name=first_name)
                    disease_2= disease_details.objects.get(disease_name=second_name)
                    disease_3= disease_details.objects.get(disease_name=third_name)
                    print ("disease_1",disease_1.disease_description)
                    context3 = {
                            first_name: disease_1.disease_description,
                            second_name :disease_2.disease_description,
                            third_name : disease_3.disease_description,

                        }

                    print ("disease detail",context3)
                    return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                    return render(request,"questionscompleted.html",{'context':context2})



                if len(x) > 3:
                    first_name = x[-1][1]
                    first_value = x[-1][0]
                    second_name = x[-2][1]
                    second_value = x[-2][0]
                    third_name = x[-3][1]
                    third_value = x[-3][0]
                    fourth_name = x[-4][1]
                    fourth_value = x[-4][0]
                    # user_diesease_update = top_disease_user_Fever.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Fever",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()


                    print("first_value",first_value)
                    print("second_value",second_value)
                    print("third_value",third_value)
                    print("fourth_value",fourth_value)
                    context2 = {
                        first_name: "Most Likely",
                        second_name :"Very Likely",
                        third_name : "Likely",
                        fourth_name : "Possible"

                    }
                    disease_1= disease_details.objects.get(disease_name=first_name)
                    disease_2= disease_details.objects.get(disease_name=second_name)
                    disease_3= disease_details.objects.get(disease_name=third_name)
                    disease_4= disease_details.objects.get(disease_name=fourth_name)
                    print ("disease_1",disease_1.disease_description)
                    context3 = {
                            first_name: disease_1.disease_description,
                            second_name :disease_2.disease_description,
                            third_name : disease_3.disease_description,
                            fourth_name : disease_4.disease_description

                        }

                    print ("disease detail",context3)
                    return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                    return render(request,"questionscompleted.html",{'context':context2})

            for op1 in some_var:
                if op1== "1":
                    return redirect("Choose_fever_blood_test")
                # if op1== "2":
                #     return redirect("Abdominal_chest_xray")
        return render(request,"thanks_page_fever.html")

# @login_required(login_url='signin')
def Choose_fever_blood_test(request):
    global num

    # if request.user.is_authenticated:
    #     user = request.user
    if request.method == 'GET':
        return render(request,"Choose_bloodtest.html")


    if request.method == 'POST':
        some_var = request.POST.getlist('checks[]')
        print ("some_var" , len(some_var))
        print ("some_var" , some_var)

        context ={
        "Viral_Fever":Viral_Fever,
        "COVID":COVID,
        "Pneumonia":Pneumonia,
        "Cholangitis":Cholangitis,
        "Endocarditis":Endocarditis,
        "Cellulitis":Cellulitis,
        "UTI":UTI,
        "Osteomyelitis":Osteomyelitis,
        "Meningitis":Meningitis,
    }

        if len(some_var) ==0:
            print("i am checking to length is 0")

            x = sorted(((v,k) for k,v in context.items() if v > 0))
            print ("len of x",len(x))
            if len(x) == 0:
                return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

            if len(x) == 1:
                first_name = x[-1][1]
                first_value = x[-1][0]
                # user_diesease_update = top_disease_user_Fever.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Fever",disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",

                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                return render(request,"questionscompleted.html",{'context':context2})

                return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

            if len(x) == 2:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                # user_diesease_update = top_disease_user_Fever.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Fever",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",
                    second_name :"Possible",
                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                return render(request,"questionscompleted.html",{'context':context2})



            if len(x) == 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                # user_diesease_update = top_disease_user_Fever.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Fever",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",
                    second_name :"Likely",
                    third_name : "Possible",
                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                disease_3= disease_details.objects.get(disease_name=third_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,
                        third_name : disease_3.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                return render(request,"questionscompleted.html",{'context':context2})



            if len(x) > 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                fourth_name = x[-4][1]
                fourth_value = x[-4][0]
                # user_diesease_update = top_disease_user_Fever.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Fever",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()


                print("first_value",first_value)
                print("second_value",second_value)
                print("third_value",third_value)
                print("fourth_value",fourth_value)
                context2 = {
                    first_name: "Most Likely",
                    second_name :"Very Likely",
                    third_name : "Likely",
                    fourth_name : "Possible"

                }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                disease_3= disease_details.objects.get(disease_name=third_name)
                disease_4= disease_details.objects.get(disease_name=fourth_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,
                        third_name : disease_3.disease_description,
                        fourth_name : disease_4.disease_description

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})



        num=[]
        for i in some_var:
            num.append(i)
            print("num list is" ,i)

        return redirect("fever_blood")

    return render(request,"thanks_page_fever.html")


# @login_required(login_url='signin')
def fever_blood(request):

    # if request.user.is_authenticated:
    #     user = request.user
        if request.method == 'GET':

            q1= [7,8,9]
            q2= [13,14,15,16,17]
            q3= [10,11,12]
            q4= [5,6]
            q5= [1,2,3]
            q6= [4]
            merge_qn=[]
            for p in num:
                if p=="1":
                    for q in q1:
                        merge_qn.append(q)

                if p=="2":
                    for q in q2:
                        merge_qn.append(q)

                if p=="3":
                    for q in q3:
                        merge_qn.append(q)

                if p=="4":
                    for q in q4:
                        merge_qn.append(q)

                if p=="5":
                    for q in q5:
                        merge_qn.append(q)

                if p=="6":
                    for q in q6:
                        merge_qn.append(q)

            print("merge_qn" ,merge_qn)

            final_data1=[]
            for a in merge_qn:
                questions = blood_questions.objects.filter(id=a)
                print("questions are", questions)

                for l in questions:
                    options=[]
                    all_option=blood_options_questions.objects.filter(question=l.id)
                    for data in all_option:
                        options.append({
                            "options_id":data.id,
                            "options_data":data.option1,
                        })
                final_data1.append({
                            "question_data":l.Question,
                            "question_id":l.id,
                            "option":options,

                        })


            return render(request,"bloodtest.html",{'context7':final_data1})

        if request.method == 'POST':
            global Viral_Fever
            global COVID
            global Pneumonia
            global Cholangitis
            global Endocarditis
            global Cellulitis
            global UTI
            global Osteomyelitis
            global Meningitis
            print("Viral_Fever",Viral_Fever)
            print("COVID",COVID)
            print("Pneumonia",Pneumonia)
            print("Cholangitis",Cholangitis)
            print("Endocarditis",Endocarditis)
            print("Cellulitis",Cellulitis)
            print("UTI",UTI)
            print("Osteomyelitis",Osteomyelitis)
            print("Meningitis",Meningitis)
            for question_id in request.POST:
                answer_id = request.POST[question_id]
                # if question_id != "csrfmiddlewaretoken":
                #     question_answer_save = Fever_answer_details.objects.create(user=user,Question_id=question_id,Answer_id=answer_id,Diagnosis_name="FeverBloodReport",last_date_of_analysis=datetime.datetime.now())
                #     question_answer_save.save()
                #     print ("question_id",question_id)
                #     print ("answer_id",answer_id)
                 ### J
                if question_id =="7":
                    if answer_id =="10":
                        Endocarditis+=1
                ####k
                if question_id =="8":
                    if answer_id == "11":
                        # Viral_Fever+=1
                        # COVID+=0.5
                        Pneumonia+=1
                        Cholangitis+=1
                        Endocarditis+=1
                        Cellulitis+=1
                        UTI+=1
                        Osteomyelitis+=1
                        Meningitis+=1
                ### L M
                if question_id == "9":
                    if answer_id == "12":
                        Osteomyelitis+=1
                        COVID+=1
                    if answer_id == "13":
                        Pneumonia+=1
                        Osteomyelitis+=1
                ### N
                if question_id =="10":
                    if answer_id =="14":
                        Cholangitis+=1
                        Endocarditis+=1

                ### P
                if question_id =="12":
                    if answer_id =="16":
                        Cholangitis+=1
                        Endocarditis+=1



                ####Q
                if question_id =="13":
                    if answer_id =="17":
                        UTI+=1

                ####R
                if question_id =="14":
                    if answer_id =="18":
                        UTI+=1

            print ("POST")
            context ={
                "Viral_Fever":Viral_Fever,
                "COVID":COVID,
                "Pneumonia":Pneumonia,
                "Cholangitis":Cholangitis,
                "Endocarditis":Endocarditis,
                "Cellulitis":Cellulitis,
                "UTI":UTI,
                "Osteomyelitis":Osteomyelitis,
                "Meningitis":Meningitis,
            }
            print (context)

            x = sorted(((v,k) for k,v in context.items() if v > 0))
            print ("len of x",len(x))
            if len(x) == 0:
                return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

            if len(x) == 1:
                first_name = x[-1][1]
                first_value = x[-1][0]
                # user_diesease_update = top_disease_user_Fever.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Fever",disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",

                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                return render(request,"questionscompleted.html",{'context':context2})

                return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

            if len(x) == 2:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                # user_diesease_update = top_disease_user_Fever.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Fever",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",
                    second_name :"Possible",
                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                return render(request,"questionscompleted.html",{'context':context2})



            if len(x) == 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                # user_diesease_update = top_disease_user_Fever.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Fever",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",
                    second_name :"Likely",
                    third_name : "Possible",
                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                disease_3= disease_details.objects.get(disease_name=third_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,
                        third_name : disease_3.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                return render(request,"questionscompleted.html",{'context':context2})



            if len(x) > 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                fourth_name = x[-4][1]
                fourth_value = x[-4][0]
                # user_diesease_update = top_disease_user_Fever.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Fever",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()


                print("first_value",first_value)
                print("second_value",second_value)
                print("third_value",third_value)
                print("fourth_value",fourth_value)
                context2 = {
                    first_name: "Most Likely",
                    second_name :"Very Likely",
                    third_name : "Likely",
                    fourth_name : "Possible"

                }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                disease_3= disease_details.objects.get(disease_name=third_name)
                disease_4= disease_details.objects.get(disease_name=fourth_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,
                        third_name : disease_3.disease_description,
                        fourth_name : disease_4.disease_description

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})

# @login_required(login_url='signin')
def cough_options(request):
    # if request.user.is_authenticated:
    #     user = request.user
        if request.method == 'GET':
            return render(request,"thanks_page_cough.html")

        if request.method == 'POST':
            print("I am checking values are not getting or not")
            some_var = request.POST.getlist('checks[]')
            print ("some_var issssss" , len(some_var))
            print ("some_var isssss" , some_var)
            context ={

                "Viral_Bronchitis":VB,
                "Bacterial_Pneumonia":BP,
                "Asthma":A,
                "Chronic_Heart_Failure":CHF,
                "Chronic_Lung_Disease":CLD,
                "Lung_Cancer":LC,
                "Pleural_Embolism":PE,
                "covid":covid
            }
            print (context)

            if len(some_var) ==0:
                print("i am checking to length is 0")

                x = sorted(((v,k) for k,v in context.items() if v > 0))
                print ("len of x",len(x))
                if len(x) == 0:
                    return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

                if len(x) == 1:
                    first_name = x[-1][1]
                    first_value = x[-1][0]
                    # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()
                    context2 = {
                        first_name: "Most Likely",

                        }
                    disease_1= disease_details.objects.get(disease_name=first_name)
                    print ("disease_1",disease_1.disease_description)
                    context3 = {
                            first_name: disease_1.disease_description,

                        }

                    print ("disease detail",context3)
                    return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                    return render(request,"questionscompleted.html",{'context':context2})


                if len(x) == 2:
                    first_name = x[-1][1]
                    first_value = x[-1][0]
                    second_name = x[-2][1]
                    second_value = x[-2][0]
                    # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    context2 = {
                        first_name: "Most Likely",
                        second_name :"Possible",
                        }
                    disease_1= disease_details.objects.get(disease_name=first_name)
                    disease_2= disease_details.objects.get(disease_name=second_name)
                    print ("disease_1",disease_1.disease_description)
                    context3 = {
                            first_name: disease_1.disease_description,
                            second_name :disease_2.disease_description,

                        }

                    print ("disease detail",context3)
                    return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                    return render(request,"questionscompleted.html",{'context':context2})



                if len(x) == 3:
                    first_name = x[-1][1]
                    first_value = x[-1][0]
                    second_name = x[-2][1]
                    second_value = x[-2][0]
                    third_name = x[-3][1]
                    third_value = x[-3][0]
                    # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    context2 = {
                        first_name: "Most Likely",
                        second_name :"Likely",
                        third_name : "Possible",
                        }
                    disease_1= disease_details.objects.get(disease_name=first_name)
                    disease_2= disease_details.objects.get(disease_name=second_name)
                    disease_3= disease_details.objects.get(disease_name=third_name)
                    print ("disease_1",disease_1.disease_description)
                    context3 = {
                            first_name: disease_1.disease_description,
                            second_name :disease_2.disease_description,
                            third_name : disease_3.disease_description,

                        }

                    print ("disease detail",context3)
                    return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                    return render(request,"questionscompleted.html",{'context':context2})

                if len(x) > 3:
                    first_name = x[-1][1]
                    first_value = x[-1][0]
                    second_name = x[-2][1]
                    second_value = x[-2][0]
                    third_name = x[-3][1]
                    third_value = x[-3][0]
                    fourth_name = x[-4][1]
                    fourth_value = x[-4][0]
                    # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()
                    # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    print("first_value",first_value)
                    print("second_value",second_value)
                    print("third_value",third_value)
                    print("fourth_value",fourth_value)
                    context2 = {
                        first_name: "Most Likely",
                        second_name :"Very Likely",
                        third_name : "Likely",
                        fourth_name : "Possible"

                    }
                    disease_1= disease_details.objects.get(disease_name=first_name)
                    disease_2= disease_details.objects.get(disease_name=second_name)
                    disease_3= disease_details.objects.get(disease_name=third_name)
                    disease_4= disease_details.objects.get(disease_name=fourth_name)
                    print ("disease_1",disease_1.disease_description)
                    context3 = {
                            first_name: disease_1.disease_description,
                            second_name :disease_2.disease_description,
                            third_name : disease_3.disease_description,
                            fourth_name : disease_4.disease_description

                        }

                    print ("disease detail",context3)
                    return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                    return render(request,"questionscompleted.html",{'context':context2})

            for op1 in some_var:
                if len(some_var) ==2:
                    print("both option are coming or not")
                    return redirect("Choose_cxray_blood_test")

                if op1== "1":
                    return redirect("Choose_cough_blood_test")
                if op1== "2":
                    return redirect("cough_chest_xray")


            return render(request,"thanks_page_cough.html")

# @login_required(login_url='signin')
def Choose_cough_blood_test(request):
    global num

    # if request.user.is_authenticated:
    #     user = request.user
    if request.method == 'GET':
        return render(request,"Choose_bloodtest.html")

    if request.method == 'POST':
        some_var = request.POST.getlist('checks[]')
        print ("some_var" , len(some_var))
        print ("some_var" , some_var)

        context ={

            "Viral_Bronchitis":VB,
            "Bacterial_Pneumonia":BP,
            "Asthma":A,
            "Chronic_Heart_Failure":CHF,
            "Chronic_Lung_Disease":CLD,
            "Lung_Cancer":LC,
            "Pleural_Embolism":PE,
            "covid":covid
        }
        print (context)

        if len(some_var) ==0:
            print("i am checking to length is 0")

            x = sorted(((v,k) for k,v in context.items() if v > 0))
            print ("len of x",len(x))
            if len(x) == 0:
                return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

            if len(x) == 1:
                first_name = x[-1][1]
                first_value = x[-1][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",

                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})


            if len(x) == 2:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",
                    second_name :"Possible",
                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})



            if len(x) == 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",
                    second_name :"Likely",
                    third_name : "Possible",
                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                disease_3= disease_details.objects.get(disease_name=third_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,
                        third_name : disease_3.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})

            if len(x) > 3:
                print ("in len 3")
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                fourth_name = x[-4][1]
                fourth_value = x[-4][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                # user_diesease_update = top_disease_user_overall.objects.create(disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                print("first_value",first_value)
                print("second_value",second_value)
                print("third_value",third_value)
                print("fourth_value",fourth_value)
                context2 = {
                    first_name: "Most Likely",
                    second_name :"Very Likely",
                    third_name : "Likely",
                    fourth_name : "Possible"

                }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                disease_3= disease_details.objects.get(disease_name=third_name)
                disease_4= disease_details.objects.get(disease_name=fourth_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,
                        third_name : disease_3.disease_description,
                        fourth_name : disease_4.disease_description

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})


        num=[]
        for i in some_var:
            num.append(i)
            print("num list is" ,i)

        return redirect("cough_blood")

    return render(request,"thanks_page_cough.html")

# @login_required(login_url='signin')
def cough_blood(request):

    # if request.user.is_authenticated:
    #     user = request.user
        if request.method == 'GET':

            q1= [7,8,9]
            q2= [13,14,15,16,17]
            q3= [10,11,12]
            q4= [5,6]
            q5= [1,2,3]
            q6= [4]
            merge_qn=[]
            for p in num:
                if p=="1":
                    for q in q1:
                        merge_qn.append(q)

                if p=="2":
                    for q in q2:
                        merge_qn.append(q)

                if p=="3":
                    for q in q3:
                        merge_qn.append(q)

                if p=="4":
                    for q in q4:
                        merge_qn.append(q)

                if p=="5":
                    for q in q5:
                        merge_qn.append(q)

                if p=="6":
                    for q in q6:
                        merge_qn.append(q)

            print("merge_qn" ,merge_qn)

            final_data1=[]
            for a in merge_qn:
                questions = blood_questions.objects.filter(id=a)
                print("questions are", questions)

                for l in questions:
                    options=[]
                    all_option=blood_options_questions.objects.filter(question=l.id)
                    for data in all_option:
                        options.append({
                            "options_id":data.id,
                            "options_data":data.option1,
                        })
                final_data1.append({
                            "question_data":l.Question,
                            "question_id":l.id,
                            "option":options,

                        })


            return render(request,"bloodtest.html",{'context7':final_data1})

        if request.method == 'POST':
            global VB
            global BP
            global A
            global CHF
            global CLD
            global LC
            global PE
            global covid
            print("VB",VB)
            print("BP",BP)
            print("A",A)
            print("CHF",CHF)
            print("CLD",CLD)
            print("LC",LC)
            print("PE",PE)
            print("covid",covid)
            for question_id in request.POST:
                answer_id = request.POST[question_id]
                # if question_id != "csrfmiddlewaretoken":
                #     question_answer_save = cough_answer_details.objects.create(user=user,Question_id=question_id,Answer_id=answer_id,Diagnosis_name="CoughBloodReport",last_date_of_analysis=datetime.datetime.now())
                #     question_answer_save.save()

                #     print ("question_id",question_id)
                #     print ("answer_id",answer_id)
                if question_id == "8":
                    if answer_id=="11":
                        BP+=1
                if question_id == "9":
                    if answer_id=="12":
                        VB+=1
                        PE+=0.5
                    if answer_id=="13":
                        BP+=0.5
                        PE+=0.5

                if question_id == "10":
                    if answer_id=="14":
                        LC+=0.5

                if question_id == "13":
                    if answer_id=="17":
                        CHF+=1
                if question_id == "14":
                    if answer_id=="18":
                        CHF+=1
                if question_id == "15":
                    if answer_id=="19":
                        LC+=1
            print ("POST")

            print("Viral_Bronchitis",VB)
            print("Bacterial_Pneumonia",BP)
            print("Asthma",A)
            print("Chronic_Heart_Failure",CHF)
            print("Chronic_Lung_Disease",CLD)
            print("Lung_Cancer",LC)
            print("Pleural_Embolism",PE)
            print("covid",covid)
            context ={

                "Viral_Bronchitis":VB,
                "Bacterial_Pneumonia":BP,
                "Asthma":A,
                "Chronic_Heart_Failure":CHF,
                "Chronic_Lung_Disease":CLD,
                "Lung_Cancer":LC,
                "Pleural_Embolism":PE,
                "covid":covid
            }
            print (context)

            x = sorted(((v,k) for k,v in context.items() if v > 0))

            print ("len of x",len(x))
            if len(x) == 0:
                return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

            if len(x) == 1:
                first_name = x[-1][1]
                first_value = x[-1][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",

                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                return render(request,"questionscompleted.html",{'context':context2})

                return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

            if len(x) == 2:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",
                    second_name :"Possible",
                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                return render(request,"questionscompleted.html",{'context':context2})



            if len(x) == 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",
                    second_name :"Likely",
                    third_name : "Possible",
                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                disease_3= disease_details.objects.get(disease_name=third_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,
                        third_name : disease_3.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})


                # return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

            if len(x) > 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                fourth_name = x[-4][1]
                fourth_value = x[-4][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                print("first_value",first_value)
                print("second_value",second_value)
                print("third_value",third_value)
                print("fourth_value",fourth_value)
                context2 = {
                    first_name: "Most Likely",
                    second_name :"Very Likely",
                    third_name : "Likely",
                    fourth_name : "Possible"

                }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                disease_3= disease_details.objects.get(disease_name=third_name)
                disease_4= disease_details.objects.get(disease_name=fourth_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,
                        third_name : disease_3.disease_description,
                        fourth_name : disease_4.disease_description

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})

# @login_required(login_url='signin')
def cough_chest_xray(request):
    # if request.user.is_authenticated:
    return render (request,"chestxray_new.html")
    # return redirect("signin")

# @login_required(login_url='signin')
def cough_result(request):
    # if request.user.is_authenticated:
    #     user = request.user
        context ={

                "Viral_Bronchitis":VB,
                "Bacterial_Pneumonia":BP,
                "Asthma":A,
                "Chronic_Heart_Failure":CHF,
                "Chronic_Lung_Disease":CLD,
                "Lung_Cancer":LC,
                "Pleural_Embolism":PE,
                "covid":covid
            }
        print(context)

        x = sorted(((v,k) for k,v in context.items() if v > 0))
        print ("len of x",len(x))
        if len(x) == 0:
            return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

        if len(x) == 1:
            first_name = x[-1][1]
            first_value = x[-1][0]
            # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            context2 = {
                first_name: "Most Likely",

                }
            disease_1= disease_details.objects.get(disease_name=first_name)
            print ("disease_1",disease_1.disease_description)
            context3 = {
                    first_name: disease_1.disease_description,
                }

            print ("disease detail",context3)
            return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

            return render(request,"questionscompleted.html",{'context':context2})

            return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

        if len(x) == 2:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            context2 = {
                first_name: "Most Likely",
                second_name :"Possible",
                }
            disease_1= disease_details.objects.get(disease_name=first_name)
            disease_2= disease_details.objects.get(disease_name=second_name)
            print ("disease_1",disease_1.disease_description)
            context3 = {
                    first_name: disease_1.disease_description,
                    second_name :disease_2.disease_description,

                }

            print ("disease detail",context3)
            return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

            return render(request,"questionscompleted.html",{'context':context2})

        if len(x) == 3:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            third_name = x[-3][1]
            third_value = x[-3][0]
            # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            context2 = {
                first_name: "Most Likely",
                second_name :"Likely",
                third_name : "Possible",
                }
            disease_1= disease_details.objects.get(disease_name=first_name)
            disease_2= disease_details.objects.get(disease_name=second_name)
            disease_3= disease_details.objects.get(disease_name=third_name)
            print ("disease_1",disease_1.disease_description)
            context3 = {
                    first_name: disease_1.disease_description,
                    second_name :disease_2.disease_description,
                    third_name : disease_3.disease_description,

                }

            print ("disease detail",context3)
            return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

            return render(request,"questionscompleted.html",{'context':context2})


            # return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

        if len(x) > 3:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            third_name = x[-3][1]
            third_value = x[-3][0]
            fourth_name = x[-4][1]
            fourth_value = x[-4][0]
            # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            print("first_value",first_value)
            print("second_value",second_value)
            print("third_value",third_value)
            print("fourth_value",fourth_value)
            context2 = {
                first_name: "Most Likely",
                second_name :"Very Likely",
                third_name : "Likely",
                fourth_name : "Possible"

            }
            disease_1= disease_details.objects.get(disease_name=first_name)
            disease_2= disease_details.objects.get(disease_name=second_name)
            disease_3= disease_details.objects.get(disease_name=third_name)
            disease_4= disease_details.objects.get(disease_name=fourth_name)
            print ("disease_1",disease_1.disease_description)
            context3 = {
                    first_name: disease_1.disease_description,
                    second_name :disease_2.disease_description,
                    third_name : disease_3.disease_description,
                    fourth_name : disease_4.disease_description

                }

            print ("disease detail",context3)
            return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

            return render(request,"questionscompleted.html",{'context':context2})

# @login_required(login_url='signin')
def Choose_cxray_blood_test(request):
    global num

    # if request.user.is_authenticated:
    #     user = request.user
    if request.method == 'GET':
        return render(request,"Choose_bloodtest.html")

    if request.method == 'POST':
        some_var = request.POST.getlist('checks[]')
        print ("some_var" , len(some_var))
        print ("some_var" , some_var)

        context ={

            "Viral_Bronchitis":VB,
            "Bacterial_Pneumonia":BP,
            "Asthma":A,
            "Chronic_Heart_Failure":CHF,
            "Chronic_Lung_Disease":CLD,
            "Lung_Cancer":LC,
            "Pleural_Embolism":PE,
            "covid":covid
        }
        print (context)

        if len(some_var) ==0:
            print("i am checking to length is 0")

            x = sorted(((v,k) for k,v in context.items() if v > 0))
            print ("len of x",len(x))
            if len(x) == 0:
                return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

            if len(x) == 1:
                first_name = x[-1][1]
                first_value = x[-1][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",

                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})

                return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

            if len(x) == 2:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",
                    second_name :"Possible",
                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})

            if len(x) == 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",
                    second_name :"Likely",
                    third_name : "Possible",
                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                disease_3= disease_details.objects.get(disease_name=third_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,
                        third_name : disease_3.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})


                # return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

            if len(x) > 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                fourth_name = x[-4][1]
                fourth_value = x[-4][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                print("first_value",first_value)
                print("second_value",second_value)
                print("third_value",third_value)
                print("fourth_value",fourth_value)
                context2 = {
                    first_name: "Most Likely",
                    second_name :"Very Likely",
                    third_name : "Likely",
                    fourth_name : "Possible"

                }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                disease_3= disease_details.objects.get(disease_name=third_name)
                disease_4= disease_details.objects.get(disease_name=fourth_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,
                        third_name : disease_3.disease_description,
                        fourth_name : disease_4.disease_description

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})

        num=[]
        for i in some_var:
            num.append(i)
            print("num list is" ,i)

        return redirect("Choose_cough_BT_Xray")

    return render(request,"thanks_page_cough.html")

def Choose_cough_BT_Xray(request):
    global num
    # if request.user.is_authenticated:
    #     user = request.user
    if request.method == 'GET':

        q1= [7,8,9]
        q2= [13,14,15,16,17]
        q3= [10,11,12]
        q4= [5,6]
        q5= [1,2,3]
        q6= [4]
        merge_qn=[]
        for p in num:
            if p=="1":
                for q in q1:
                    merge_qn.append(q)

            if p=="2":
                for q in q2:
                    merge_qn.append(q)

            if p=="3":
                for q in q3:
                    merge_qn.append(q)

            if p=="4":
                for q in q4:
                    merge_qn.append(q)

            if p=="5":
                for q in q5:
                    merge_qn.append(q)

            if p=="6":
                for q in q6:
                    merge_qn.append(q)

        print("merge_qn" ,merge_qn)

        final_data1=[]
        for a in merge_qn:
            questions = blood_questions.objects.filter(id=a)
            print("questions are", questions)

            for l in questions:
                options=[]
                all_option=blood_options_questions.objects.filter(question=l.id)
                for data in all_option:
                    options.append({
                        "options_id":data.id,
                        "options_data":data.option1,
                    })
            final_data1.append({
                        "question_data":l.Question,
                        "question_id":l.id,
                        "option":options,

                    })


        return render(request,"bloodtest.html",{'context7':final_data1})

    if request.method == 'POST':
        global VB
        global BP
        global A
        global CHF
        global CLD
        global LC
        global PE
        global covid
        print("VB",VB)
        print("BP",BP)
        print("A",A)
        print("CHF",CHF)
        print("CLD",CLD)
        print("LC",LC)
        print("PE",PE)
        print("covid",covid)
        for question_id in request.POST:
            answer_id = request.POST[question_id]

            # if question_id != "csrfmiddlewaretoken":
            #     question_answer_save = cough_answer_details.objects.create(user=user,Question_id=question_id,Answer_id=answer_id,Diagnosis_name="CoughBloodReport",last_date_of_analysis=datetime.datetime.now())
            #     question_answer_save.save()

            #     print ("question_id",question_id)
            #     print ("answer_id",answer_id)

            if question_id == "8":
                if answer_id=="11":
                    BP+=1
            if question_id == "9":
                if answer_id=="12":
                    VB+=1
                    PE+=0.5
                if answer_id=="13":
                    BP+=0.5
                    PE+=0.5

            if question_id == "10":
                if answer_id=="14":
                    LC+=0.5

            if question_id == "13":
                if answer_id=="17":
                    CHF+=1
            if question_id == "14":
                if answer_id=="18":
                    CHF+=1
            if question_id == "15":
                if answer_id=="19":
                    LC+=1
        print ("POST")

        print("Viral_Bronchitis",VB)
        print("Bacterial_Pneumonia",BP)
        print("Asthma",A)
        print("Chronic_Heart_Failure",CHF)
        print("Chronic_Lung_Disease",CLD)
        print("Lung_Cancer",LC)
        print("Pleural_Embolism",PE)
        print("covid",covid)
        context ={

            "Viral_Bronchitis":VB,
            "Bacterial_Pneumonia":BP,
            "Asthma":A,
            "Chronic_Heart_Failure":CHF,
            "Chronic_Lung_Disease":CLD,
            "Lung_Cancer":LC,
            "Pleural_Embolism":PE,
            "covid":covid
        }
        print (context)

        x = sorted(((v,k) for k,v in context.items()))
        first_name = x[-1][1]
        first_value = x[-1][0]
        second_name = x[-2][1]
        second_value = x[-2][0]
        third_name = x[-3][1]
        third_value = x[-3][0]
        fourth_name = x[-4][1]
        fourth_value = x[-4][0]
        # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
        # user_diesease_update.save()

        print("first_value",first_value)
        print("second_value",second_value)
        print("third_value",third_value)
        print("fourth_value",fourth_value)
        # context3 = {
        #     first_name: "Most Likely",
        #     second_name :"Very Likely",
        #     third_name : "Likely",
        #     fourth_name : "Possible"

        # }

        return redirect("cough_chest_xray")



class chest_Condition(APIView):
    print ("in function")
    def post(self, request, format=None):
        # user = request.user
        global VB
        global BP
        global A
        global CHF
        global CLD
        global LC
        global PE
        global covid
        print("VB",VB)
        print("BP",BP)
        print("A",A)
        print("CHF",CHF)
        print("CLD",CLD)
        print("LC",LC)
        print("PE",PE)
        print("covid",covid)

        try:
            file = request.data.get('fileup')
            staticPrefix = "static"
            filename = str(file)
            print ("filename",filename)

            filepath = 'images/uploadbyuser/' + filename
            with default_storage.open(filepath, 'wb+') as destination:
                for chunk in file.chunks():
                    # print ("chunk",chunk)
                    destination.write(chunk)
                    print ("desdestination",destination )

            # getting results
            results = model_cxr("media/"+filepath)
            print ("results",results)
            # for croping

            _, result_dir = results.crop(save=True)
            print ("result_dir",result_dir)
            # converting detection result to json format
            data = results.pandas().xyxy[0].to_json(orient="records")
            print ("previous data",data)

            try :
                # normalizing result_dir
                tmp = finders.find(result_dir)
                print ("tmp",tmp)
            except Exception as e:
                print ("normalizing result_dir",e)

            searched_loc = finders.searched_locations
            print ("searched_loc",searched_loc)

            modified_res_loc = os.path.relpath(tmp, searched_loc[0])
            print ("modified_res_loc",modified_res_loc)

            result_dir = str(result_dir.as_posix())
            print ("result_dir",result_dir)


            data = json.loads(data)
            print ("here is the complete data",len(data))

            if len(data) == 0:
                print ("ok")
                # saving_data=Chest_Xray_image.objects.create(user=user,uploaded_image=file,last_date_of_analysis=datetime.datetime.now())
                # saving_data.save()
                # chest_detected_diseases= chest_detected_disease.objects.create(chestimageid=saving_data,disease_name="No Disease Found",confidence="100%",last_date_of_analysis=datetime.datetime.now())
                # chest_detected_diseases.save()

                context ={

                "Viral_Bronchitis":VB,
                "Bacterial_Pneumonia":BP,
                "Asthma":A,
                "Chronic_Heart_Failure":CHF,
                "Chronic_Lung_Disease":CLD,
                "Lung_Cancer":LC,
                "Pleural_Embolism":PE,
                "covid":covid
            }
                print (context)

                x = sorted(((v,k) for k,v in context.items() if v > 0))
                print ("len of x",len(x))

                if len(x) == 0:
                    return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

                if len(x) == 1:
                    first_name = x[-1][1]
                    first_value = x[-1][0]
                    # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    context2 = {
                        first_name: "Most Likely",

                        }

                    disease_1= disease_details.objects.get(disease_name=first_name)
                    print ("disease_1",disease_1.disease_description)
                    context3 = {
                            first_name: disease_1.disease_description,
                        }

                    print ("disease detail",context3)
                    return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                    return render(request,"questionscompleted.html",{'context':context2})

                    return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

                if len(x) == 2:
                    first_name = x[-1][1]
                    first_value = x[-1][0]
                    second_name = x[-2][1]
                    second_value = x[-2][0]
                    # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    context2 = {
                        first_name: "Most Likely",
                        second_name :"Possible",
                        }
                    disease_1= disease_details.objects.get(disease_name=first_name)
                    disease_2= disease_details.objects.get(disease_name=second_name)
                    print ("disease_1",disease_1.disease_description)
                    context3 = {
                            first_name: disease_1.disease_description,
                            second_name :disease_2.disease_description,

                        }

                    print ("disease detail",context3)
                    return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                    return render(request,"questionscompleted.html",{'context':context2})

                if len(x) == 3:
                    first_name = x[-1][1]
                    first_value = x[-1][0]
                    second_name = x[-2][1]
                    second_value = x[-2][0]
                    third_name = x[-3][1]
                    third_value = x[-3][0]
                    # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()
                    # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    context2 = {
                        first_name: "Most Likely",
                        second_name :"Likely",
                        third_name : "Possible",
                        }
                    disease_1= disease_details.objects.get(disease_name=first_name)
                    disease_2= disease_details.objects.get(disease_name=second_name)
                    disease_3= disease_details.objects.get(disease_name=third_name)
                    print ("disease_1",disease_1.disease_description)
                    context3 = {
                            first_name: disease_1.disease_description,
                            second_name :disease_2.disease_description,
                            third_name : disease_3.disease_description,

                        }

                    print ("disease detail",context3)
                    return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                    return render(request,"questionscompleted.html",{'context':context2})


                    # return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

                if len(x) > 3:
                    first_name = x[-1][1]
                    first_value = x[-1][0]
                    second_name = x[-2][1]
                    second_value = x[-2][0]
                    third_name = x[-3][1]
                    third_value = x[-3][0]
                    fourth_name = x[-4][1]
                    fourth_value = x[-4][0]
                    # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()
                    # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                    # user_diesease_update.save()

                    print("first_value",first_value)
                    print("second_value",second_value)
                    print("third_value",third_value)
                    print("fourth_value",fourth_value)
                    context2 = {
                        first_name: "Most Likely",
                        second_name :"Very Likely",
                        third_name : "Likely",
                        fourth_name : "Possible"

                    }
                    disease_1= disease_details.objects.get(disease_name=first_name)
                    disease_2= disease_details.objects.get(disease_name=second_name)
                    disease_3= disease_details.objects.get(disease_name=third_name)
                    disease_4= disease_details.objects.get(disease_name=fourth_name)
                    print ("disease_1",disease_1.disease_description)
                    context3 = {
                            first_name: disease_1.disease_description,
                            second_name :disease_2.disease_description,
                            third_name : disease_3.disease_description,
                            fourth_name : disease_4.disease_description

                        }

                    print ("disease detail",context3)
                    return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                    return render(request,"questionscompleted.html",{'context':context2})
                # return render(request,"chestxray.html",{'context1':"No Disease Found"})

            unique_fruits = {}
            for fruit in data:
                unique_fruits[fruit.get('name')] = []
                print ("unique_fruits",unique_fruits)


            for fruit in unique_fruits:
                file_list = os.listdir(result_dir+'/crops/'+fruit)
                unique_fruits[fruit] = file_list
                print ("file_list",file_list)


            name_confidence = []
            final_data = []
            # i  = 0
            for record in data:
                name_confidence.append({
                    "name": record.get('name'),
                    "confidence": record.get('confidence')
                })
                final_data.append({
                    "name": record.get('name'),
                    "confidence": record.get('confidence'),
                    "image_url": staticPrefix+'/' + modified_res_loc + '/crops/' + record.get('name') + '/' + unique_fruits[record.get('name')].pop(0)
                })
                break
            print ("first type",type(name_confidence))
            print ("name_confidence",name_confidence)
            # print ("second type",type(dict(name_confidence)))
            # name_confidence=dict(name_confidence)
            print ("name_confidence 2",name_confidence)
            print ("Only Name",name_confidence[0]["name"])
            if name_confidence[0]["name"] == "Effusion":
                CHF+=1
                CLD+=1
                LC+=0.5
                print ("in if Effusion")
            if name_confidence[0]["name"] == "Pneumonia":
                BP+=1
                CLD+=1
                LC+=0.5
                covid+=1

                print ("in if Pneumonia")
            if name_confidence[0]["name"] == "Nodules":
                LC+=1

                print ("in if Nodules")
            if name_confidence[0]["name"] == "Normal":
                print ("in if Normal")
                VB+=0.5
                A+=0.75
                PE+=0.5
                covid+=0.5


            resultant_data = {
                "data": final_data,
                "actual_image_url": staticPrefix + '/'+modified_res_loc+'/'+filename
            }
            print("VB",VB)
            print("BP",BP)
            print("A",A)
            print("CHF",CHF)
            print("CLD",CLD)
            print("LC",LC)
            print("PE",PE)
            print("covid",covid)
            # saving_data=Chest_Xray_image.objects.create(user=user,uploaded_image=file,last_date_of_analysis=datetime.datetime.now())
            # saving_data.save()
            for i in name_confidence:
                print ("name confidence i",i['name'])
                # detecteddiseases= chest_detected_disease.objects.create(chestimageid=saving_data,disease_name=i['name'],confidence=i['confidence'],last_date_of_analysis=datetime.datetime.now())
                # detecteddiseases.save()

            context ={

                "Viral_Bronchitis":VB,
                "Bacterial_Pneumonia":BP,
                "Asthma":A,
                "Chronic_Heart_Failure":CHF,
                "Chronic_Lung_Disease":CLD,
                "Lung_Cancer":LC,
                "Pleural_Embolism":PE,
                "covid":covid
            }
            print (context)

            x = sorted(((v,k) for k,v in context.items() if v > 0))
            print ("len of x",len(x))

            if len(x) == 0:
                return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

            if len(x) == 1:
                first_name = x[-1][1]
                first_value = x[-1][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",

                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})

                return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

            if len(x) == 2:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",
                    second_name :"Possible",
                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})

            if len(x) == 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",
                    second_name :"Likely",
                    third_name : "Possible",
                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                disease_3= disease_details.objects.get(disease_name=third_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,
                        third_name : disease_3.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})


                # return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

            if len(x) > 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                fourth_name = x[-4][1]
                fourth_value = x[-4][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                print("first_value",first_value)
                print("second_value",second_value)
                print("third_value",third_value)
                print("fourth_value",fourth_value)
                context2 = {
                    first_name: "Most Likely",
                    second_name :"Very Likely",
                    third_name : "Likely",
                    fourth_name : "Possible"

                }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                disease_3= disease_details.objects.get(disease_name=third_name)
                disease_4= disease_details.objects.get(disease_name=fourth_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,
                        third_name : disease_3.disease_description,
                        fourth_name : disease_4.disease_description

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})
            # return redirect("blood_Report_cough")
        except Exception as e:
            print ("exception",e)

            context ={

                "Viral_Bronchitis":VB,
                "Bacterial_Pneumonia":BP,
                "Asthma":A,
                "Chronic_Heart_Failure":CHF,
                "Chronic_Lung_Disease":CLD,
                "Lung_Cancer":LC,
                "Pleural_Embolism":PE,
                "covid":covid
            }
            print (context)

            x = sorted(((v,k) for k,v in context.items() if v > 0))
            print ("len of x",len(x))

            if len(x) == 0:
                return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

            if len(x) == 1:
                first_name = x[-1][1]
                first_value = x[-1][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",

                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})

                return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

            if len(x) == 2:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",
                    second_name :"Possible",
                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})

            if len(x) == 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                context2 = {
                    first_name: "Most Likely",
                    second_name :"Likely",
                    third_name : "Possible",
                    }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                disease_3= disease_details.objects.get(disease_name=third_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,
                        third_name : disease_3.disease_description,

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})

                return render(request,"questionscompleted.html",{'context':context2})


                # return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

            if len(x) > 3:
                first_name = x[-1][1]
                first_value = x[-1][0]
                second_name = x[-2][1]
                second_value = x[-2][0]
                third_name = x[-3][1]
                third_value = x[-3][0]
                fourth_name = x[-4][1]
                fourth_value = x[-4][0]
                # user_diesease_update = top_disease_user_cough.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()
                # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Cough",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
                # user_diesease_update.save()

                print("first_value",first_value)
                print("second_value",second_value)
                print("third_value",third_value)
                print("fourth_value",fourth_value)
                context2 = {
                    first_name: "Most Likely",
                    second_name :"Very Likely",
                    third_name : "Likely",
                    fourth_name : "Possible"

                }
                disease_1= disease_details.objects.get(disease_name=first_name)
                disease_2= disease_details.objects.get(disease_name=second_name)
                disease_3= disease_details.objects.get(disease_name=third_name)
                disease_4= disease_details.objects.get(disease_name=fourth_name)
                print ("disease_1",disease_1.disease_description)
                context3 = {
                        first_name: disease_1.disease_description,
                        second_name :disease_2.disease_description,
                        third_name : disease_3.disease_description,
                        fourth_name : disease_4.disease_description

                    }

                print ("disease detail",context3)
                return render(request,"questionscompleted.html",{'context':context2,'context3':context3})


                # return render(request,"questionscompleted.html",{'context':context5})
            # return redirect("blood_Report_cough")



def emailskin(request):
    if request.method =="GET":
        print ("In contact Us page get request")
        print ("data",request.GET)
        # name = request.GET["name"]

        # phone = request.GET["phone"]
        email1 = request.GET["email"]
        # message = request.GET["discription"]

        details = request.session.get('detailed User message')


        if len(email1) == 0:
            return JsonResponse({"status":"Error"})

        msz =  " Hi there,Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined Here is your detail Analysis \n {} \n The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms.\n Our most commonly visited symptoms are chest pain (https://www.apnamd.ai/ChestPain/ ) and depression (https://www.apnamd.ai/Depression/Test/). \n Kind Regards \n ApnaMD Team  ".format(details)

        try :
            email = EmailMessage("Apna MD (AI Diagnosis)",msz,to=[email1])
            email.send()
            # newemails_store =  newemails.objects.create(email=email1,create_Date= datetime.datetime.now())
            # newemails_store.save()
            # user_diesease_update = top_disease_user_overall_with_user.objects.create(analysistype=request.session.get('Diagnosis_type'),disease1=request.session.get('Diagnosis'), p1=request.session.get('P1_score'),email=email1,verified="No",userfrom="Web Application", last_date_of_analysis=datetime.datetime.now(),imagepath=request.session.get('filename'))
            # user_diesease_update.save()

            return JsonResponse({"status":"sent"})
        except Exception as e:
            print ("Error in email exception",e)
            return JsonResponse({"status":"Error"})


def skinthankyou(request):
    if request.user.is_authenticated:
        usr = request.user
        email1 = usr.email

        # user_diesease_update = top_disease_user_overall_with_user.objects.create(analysistype=request.session.get('Diagnosis_type'),disease1=request.session.get('Diagnosis'), p1=request.session.get('P1_score'),email=email1,verified="Yes",userfrom="Web Application", last_date_of_analysis=datetime.datetime.now())
        # user_diesease_update.save()
        details = request.session.get('detailed User message')

        msz =  " Hi there,Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined Here is your detail Analysis \n {} \n The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms.\n Our most commonly visited symptoms are chest pain (https://www.apnamd.ai/ChestPain/ ) and depression (https://www.apnamd.ai/Depression/Test/). \n Kind Regards \n ApnaMD Team  ".format(details)

        email = EmailMessage("Apna MD (AI Diagnosis)",msz,to=[email1])
        email.send()
        newemails_store =  newemails.objects.create(email=email1,create_Date= datetime.datetime.now())
        newemails_store.save()

    return render (request,"skinthankupage.html")

# @login_required(login_url='signin')

def skin_disease(request):
    print ("in skin ")
    # if request.user.is_authenticated:
    #     print ("in skin in if condition")
    return render (request,"skinapi.html")
    # return redirect("signin")

class Skin_Condition(APIView):
    def post(self, request, format=None):
        # user = request.user
        # print ("user",request.user)
        try:
            print ("data",request.data)
            file = request.data.get('uploadfile[0]')
            filename = (file)
            print ("filename",filename)

            print (type(file))
            print ("file",file)
            staticPrefix = "static"

            filelink="http://www.jotform.com/uploads/apnamd/" +request.data.get('formID') +"/"+ request.data.get('submission_id')+ "/" + request.data.get('uploadfile[0]')
            print ("file link",filelink)
            downloadfile = 'media/images/skinimages/' + filename
            request.session['filename']= downloadfile
            print ("file path",downloadfile)
            res = requests.get(filelink, stream = True)
            if res.status_code == 200:
                with open( downloadfile,'wb') as f:
                    shutil.copyfileobj(res.raw, f)
                print('Image sucessfully Downloaded: ',file)
            else:
                print('Image Couldn\'t be retrieved')

            # getting results
            results = model_skin(downloadfile)
            print ("results",results)
            # for croping

            _, result_dir = results.crop(save=True)
            print ("result_dir",result_dir)
            # converting detection result to json format
            data = results.pandas().xyxy[0].to_json(orient="records")
            print ("previous data",data)

            try :
                # normalizing result_dir
                tmp = finders.find(result_dir)
                print ("tmp",tmp)
            except Exception as e:
                print ("normalizing result_dir",e)

            searched_loc = finders.searched_locations
            print ("searched_loc",searched_loc)

            modified_res_loc = os.path.relpath(tmp, searched_loc[0])
            print ("modified_res_loc",modified_res_loc)

            result_dir = str(result_dir.as_posix())
            print ("result_dir",result_dir)


            data = json.loads(data)
            print ("here is the complete data",len(data))

            if len(data) == 0:
                print ("ok")
                context1 = {
                "Disease": "No disease found",

                }


                # saving_data=Skin_image.objects.create(user=user,uploaded_image=file,last_date_of_analysis=datetime.datetime.now())
                # saving_data.save()
                # detecteddiseases= top_disease_user_overall.objects.create(analysistype = "Skin",disease1="Disease",p1="No Disease Found",last_date_of_analysis=datetime.datetime.now())
                # detecteddiseases.save()

                request.session['detailed User message']= "No disease Found"
                request.session['Skin_Details ID']= detecteddiseases.id

                # {'context1':"No Disease Found"}
                request.session['Diagnosis']= "No disease"
                request.session['P1_score']= "0"
                request.session['Diagnosis_type']= "Skin Disease"

                return render(request,"skin_diagnosis.html")

            unique_fruits = {}
            for fruit in data:
                unique_fruits[fruit.get('name')] = []
                print ("unique_fruits",unique_fruits)


            for fruit in unique_fruits:
                file_list = os.listdir(result_dir+'/crops/'+fruit)
                unique_fruits[fruit] = file_list
                print ("file_list",file_list)


            name_confidence = []
            final_data = []
            # i  = 0
            for record in data:
                name_confidence.append({
                    "name": record.get('name'),
                    "confidence": record.get('confidence')
                })
                final_data.append({
                    "name": record.get('name'),
                    "confidence": record.get('confidence'),
                    "image_url": staticPrefix+'/' + modified_res_loc + '/crops/' + record.get('name') + '/' + unique_fruits[record.get('name')].pop(0)
                })
                # i = i + 1
                # if i > 4:
                #     break

            resultant_data = {
                "data": final_data,
                "actual_image_url": staticPrefix + '/'+modified_res_loc+'/'+filename
            }
            # saving_data=Skin_image.objects.create(user=user,uploaded_image=file,last_date_of_analysis=datetime.datetime.now())
            # saving_data.save()
            for i in name_confidence:
                print ("name confidence i",i['name'])


                # detecteddiseases= Skin_detected_disease.objects.create(skinimageid=saving_data,disease_name=i['name'],confidence=i['confidence'],last_date_of_analysis=datetime.datetime.now())
                # detecteddiseases.save()
                # detecteddiseases= top_disease_user_overall.objects.create(analysistype = "Skin",disease1=i['name'],p1=i['confidence'],last_date_of_analysis=datetime.datetime.now(),imagepath=downloadfile)
                # detecteddiseases.save()

                request.session['Skin_Details ID']= detecteddiseases.id

                request.session['Diagnosis']= i['name']
                request.session['P1_score']= i['confidence']
                request.session['Diagnosis_type']= "Skin Disease"


                request.session['detailed User message']= "The most likely cause of your skin condition is "+ i['name'] + ". "
                break
            # return redirect("HOME")

             # {'context':final_data}
            return render(request,"skin_diagnosis.html")

        except Exception as e:
            print ("exception",e)
            context1 = {
                "Disease": "Some Error Occur",

                }

            request.session['detailed User message']= "Some Error Occur"
            request.session['Skin_Details ID']= "Error"
            request.session['Diagnosis']= "Some Error Occur"
            request.session['P1_score']= "Some Error Occur"
            request.session['Diagnosis_type']= "Skin Disease"



            # return JsonResponse({
            #     "data": [],
            #     "actual_image_url": ""
            # }, status=500)

            # {'context1':"Some Error Occur"}
            return render(request,"skin_diagnosis.html")

@csrf_exempt
def skin_otp(request):
    return render (request,"otpcode_skinCondition.html")

@csrf_exempt
def sendotp_skin_diagnosis(request):
    if request.method =="GET":
        print ("data",request.GET)
        try :
            otpnumber = request.GET["num"]
            request.session['otpnumber']=otpnumber
            details = request.session.get('detailed User message')
            details_Id = request.session.get('Skin_Details ID')
            print ("details",details)


            try :

                account_sid = "AC933127d38ff7d1939cc865520fff97cf"

                # Your Auth Token from twilio.com/console
                auth_token  = "69196d7c514f51c4c7733b4afb4c57e6"

                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    to=request.session.get('otpnumber'),
                    from_="+18508212276",
                    body=f'{details}')
                html = render_to_string('otpcode_skinCondition.html')
                print ("messgae sid",message.sid )

                # numberdatsave =  number_with_topdisease.objects.create(phonenumber=request.session.get('otpnumber'),topdisease=details_Id)
                # numberdatsave.save()

                # newnumbers_store =  newnumbers.objects.create(number=request.session.get('otpnumber'),create_Date= datetime.datetime.now())
                # newnumbers_store.save()




                return JsonResponse({"status":"sent"})
            except Exception as e:
                print ("Error",e)
                return JsonResponse({"status":"Error"})

        except Exception as e:
            print ("Error",e)
            return JsonResponse({"status":"Error"})

    return render(request,"otpcode_skinCondition.html")


def resendotp_skin_diagnosis(request):

    try :

        otp = random.randint (1000,9999)
        request.session['otp']=otp
        account_sid = "AC933127d38ff7d1939cc865520fff97cf"

        # Your Auth Token from twilio.com/console
        auth_token  = "69196d7c514f51c4c7733b4afb4c57e6"

        client = Client(account_sid, auth_token)
        otp = request.session.get('otp')
        message = client.messages.create(
            to=request.session.get('otpnumber'),
            from_="+18508212276",
            body=f'Your OTP verification number is {otp}')
        html = render_to_string('otpcode_skinCondition.html')
        print ("messgae sid",message.sid )
        return render(request,"otpcode_skinCondition.html")
    except Exception as e:
        print ("Error",e)
        return JsonResponse({"status":"Error"})






# @login_required(login_url='signin')
def Food_analysis(request):
    # if request.user.is_authenticated:
    return render (request,"foodanalysis.html")
    # return redirect("signin")



class Food_Recognition(APIView):

    print ("in function")
    def post(self, request, format=None):

        # if request.user.is_authenticated:
        #     user = request.user
            try:
                print ("data",request.data)
                file = request.data.get('uploadfile[0]')
                filename = (file)
                print ("filename",filename)

                print (type(file))
                print ("file",file)
                staticPrefix = "static"

                filelink="http://www.jotform.com/uploads/apnamd/" +request.data.get('formID') +"/"+ request.data.get('submission_id')+ "/" + request.data.get('uploadfile[0]')
                print ("file link",filelink)
                downloadfile = 'media/images/foodimages/' + filename
                print ("file path",downloadfile)
                res = requests.get(filelink, stream = True)
                if res.status_code == 200:
                    with open( downloadfile,'wb') as f:
                        shutil.copyfileobj(res.raw, f)
                    print('Image sucessfully Downloaded: ',file)
                else:
                    print('Image Couldn\'t be retrieved')


                # getting results
                results = model_food(downloadfile)
                print ("results",results)
                # for croping

                _, result_dir = results.crop(save=True)

                # converting detection result to json format
                data = results.pandas().xyxy[0].to_json(orient="records")
                print ("data",data)

                # normalizing result_dir
                tmp = finders.find(result_dir)
                print ("tmp",tmp)

                searched_loc = finders.searched_locations
                print ("searched_loc",searched_loc)

                modified_res_loc = os.path.relpath(tmp, searched_loc[0])
                print ("modified_res_loc",modified_res_loc)

                result_dir = str(result_dir.as_posix())
                print ("result_dir",result_dir)


                data = json.loads(data)
                print ("data",data)


                unique_fruits = {}
                for fruit in data:
                    unique_fruits[fruit.get('name')] = []
                    print ("unique_fruits",unique_fruits)


                for fruit in unique_fruits:
                    file_list = os.listdir(result_dir+'/crops/'+fruit)
                    unique_fruits[fruit] = file_list
                    print ("file_list",file_list)


                name_confidence = []
                final_data = []
                cal = 0

                for record in data:
                    a= Nutrient_Information.objects.get(PRODUCT=record.get('name'))
                    individual_food_cal= a.CALORIE
                    cal = cal + a.CALORIE

                print ("total cal",cal)
                for record in data:
                    a= Nutrient_Information.objects.get(PRODUCT=record.get('name'))
                    name_confidence.append({
                        "name": record.get('name'),
                        "confidence": record.get('confidence'),

                    })
                    final_data.append({
                        "name": record.get('name'),
                        "confidence": record.get('confidence'),
                        "category":a.CATEGORY,
                        "calorie":a.CALORIE,

                    })
                final_data12=[]
                i = 0
                for finaldata in final_data:
                    print ("final_data1",final_data)
                    if i == 0:
                        final_data12.append({
                            "name": finaldata["name"],
                            "confidence":"High (0.5 to 1)"
                        })
                    if i == 1:
                        final_data12.append({
                            "name": finaldata["name"],
                            "confidence":"Medium (0.25 to 0.5)"
                        })
                    if i == 2:
                        final_data12.append({
                            "name": finaldata["name"],
                            "confidence":"Low (below 0.25)"
                        })
                    if i > 2:
                        final_data12.append({
                            "name": finaldata["name"],
                            "confidence":"Low (below 0.10)"
                        })

                    i = i + 1

                print("finaldata12",final_data12)
                print("final_data",len(final_data))
                if len(final_data) == 0:
                    # saving_data=Food_image.objects.create(user=user,uploaded_image=file,last_date_of_analysis=datetime.datetime.now())
                    # saving_data.save()
                    # food_details = food_detected_informations_user.objects.create(user=user,foodimageid=saving_data, Processed_Food_Calorie="0", Ultra_Processed_Food_Calorie= "0", Not_Processed_Food_Calorie="0", Total_Calorie="0", Total_Carb_percentage_out_of_total="0", Total_Protein_percentage_out_of_total="0", Total_Fat_percentage_out_of_total="0", Swimming_Exercise_time_to_burn_calories="0" , Jogging_Exercise_time_to_burn_calories= "0", Cycling_Exercise_time_to_burn_calories= "0" ,Walking_Exercise_time_to_burn_calories="0", last_date_of_analysis=datetime.datetime.now())
                    # food_details.save()

                    # detecteddFood= Food_detected_disease.objects.create(foodimageid=saving_data,disease_name="No Disease Found",confidence="100%",last_date_of_analysis=datetime.datetime.now())
                    # detecteddFood.save()

                    return render(request,"foodanalysis.html",{'context1':"No Food Found"})

                totalCalories=0
                total_Carb_of_detected_food=0
                total_Protein_of_detected_food=0
                total_fat_of_detected_food=0
                processed_food_cal=0
                Ultra_processed_food_cal=0
                not_processed_food_cal=0
                Swimming_exercise_time_to_burn_calories=0
                Jogging_exercise_time_to_burn_calories=0
                Cycling_exercise_time_to_burn_calories=0
                walking_exercise_time_to_burn_calories=0

                for i in range (len(final_data)):
                    # print(i)
                    a= Nutrient_Information.objects.get(PRODUCT=final_data[i]["name"])
                    # nutrition_table= print('PRODUCT:', a.PRODUCT, ', CATEGORY:', a.CATEGORY, ', CALORIE:', a.CALORIE, ', CARB:', a.CARB, ', PRO:', a.PRO, ', FAT:', a.FAT, ', Ex_Swim:', a.Ex_Swim,', Ex_Jog:',a.Ex_Jog, ', Ex_Cycle:', a.Ex_Cycle,', Ex_Walk :', a.Ex_Walk )
                    nutrition_table=[{'Product': a.PRODUCT},{'CATEGORY': a.CATEGORY},{'CALORIE': a.CALORIE},{'CARB': a.CARB},{'PRO' : a.PRO},{'FAT': a.FAT},{'Ex_Swim': a.Ex_Swim},{'Ex_Jog': a.Ex_Jog},{'Ex_Cycle': a.Ex_Cycle},{'Ex_Walk': a.Ex_Walk}]
                    print(nutrition_table)
                    print("calorie of detected food is ",float(nutrition_table[2]['CALORIE']),'\n')
                    totalCalories += float(nutrition_table[2]['CALORIE'])
                    total_Carb_of_detected_food += float(nutrition_table[3]['CARB'])
                    total_Protein_of_detected_food += float(nutrition_table[4]['PRO'])
                    total_fat_of_detected_food += float(nutrition_table[5]['FAT'])

                    Swimming_exercise_time_to_burn_calories += float (nutrition_table[6]['Ex_Swim'])
                    Jogging_exercise_time_to_burn_calories += float (nutrition_table[7]['Ex_Jog'])
                    Cycling_exercise_time_to_burn_calories += float(nutrition_table[8]['Ex_Cycle'])
                    walking_exercise_time_to_burn_calories += float(nutrition_table[9]['Ex_Walk'])

                    if a.CATEGORY =='P':
                        processed_food_cal += a.CALORIE

                    if a.CATEGORY =='UP':
                        Ultra_processed_food_cal += a.CALORIE

                    if a.CATEGORY =='N':
                        not_processed_food_cal += a.CALORIE

                processed_food_cal_out_of_total= (processed_food_cal/ totalCalories) * 100
                Ultra_processed_food_cal_out_of_total= (Ultra_processed_food_cal/ totalCalories) * 100
                not_processed_food_cal_out_of_total= (not_processed_food_cal/ totalCalories) * 100


                print("Total calorie of all food is:", totalCalories)
                print("Total carb of all food is:", total_Carb_of_detected_food)
                print("Total Protein of all food is:", total_Protein_of_detected_food)
                print("Total Fat of all food is:", total_fat_of_detected_food)
                Total_carb_percentage_out_of_total= ((float(total_Carb_of_detected_food) * 4) / totalCalories) * 100
                print("Total_carb_percentage_out_of_total is ", Total_carb_percentage_out_of_total,'\n')
                Total_Protein_percentage_out_of_total=((float(total_Protein_of_detected_food) * 4) / totalCalories) * 100
                print("Total_Protein_percentage_out_of_total is ", Total_Protein_percentage_out_of_total,'\n')
                Total_Fat_percentage_out_of_total= ((float(total_fat_of_detected_food) * 8) / totalCalories) * 100
                print("Total_Fat_percentage_out_of_total is ", Total_Fat_percentage_out_of_total,'\n')

                print("Swimming_exercise_time_to_burn_calories in minutes", Swimming_exercise_time_to_burn_calories)
                print("Jogging_exercise_time_to_burn_calories in minutes", Jogging_exercise_time_to_burn_calories)
                print("Cycling_exercise_time_to_burn_calories in minutes", Cycling_exercise_time_to_burn_calories)
                print("walking_exercise_time_to_burn_calories in minutes", walking_exercise_time_to_burn_calories)


                resultant_data = {
                    "data": final_data,
                    "actual_image_url": staticPrefix + '/'+modified_res_loc+'/'+filename
                }
                categoriewise_cal_details ={
                    'Processed_food_Percentage' : round((processed_food_cal_out_of_total),2),
                    'Ultra_Processed_food_Percentage' : round((Ultra_processed_food_cal_out_of_total),2),
                    'Unprocessed_food_Percentage' : round((not_processed_food_cal_out_of_total),2),
                }

                nutrient_details ={
                    'Total_calorie':totalCalories,
                    'Total_carb_percentage': round((Total_carb_percentage_out_of_total),2),
                    'Total_Protein_percentage': round((Total_Protein_percentage_out_of_total),2),
                    'Total_Fat_percentage': round((Total_Fat_percentage_out_of_total),2)
                }

                exercise_Details ={
                    'Swimming_exercise_time_to_burn_calories':Swimming_exercise_time_to_burn_calories,
                    'Jogging_exercise_time_to_burn_calories': Jogging_exercise_time_to_burn_calories,
                    'Cycling_exercise_time_to_burn_calories': Cycling_exercise_time_to_burn_calories,
                    'walking_exercise_time_to_burn_calories': walking_exercise_time_to_burn_calories

                }

                print(categoriewise_cal_details )
                # saving_data=Food_image.objects.create(user=user,uploaded_image=file,last_date_of_analysis=datetime.datetime.now())
                # saving_data.save()

                # food_details = food_detected_informations_user.objects.create(user=user,foodimageid=saving_data, Total_Calorie=totalCalories, Processed_Food_Percentage=processed_food_cal_out_of_total, Ultra_Processed_Food_Percentage= Ultra_processed_food_cal_out_of_total, Unprocessed_Food_Percentage=not_processed_food_cal_out_of_total, Total_Carb_percentage= Total_carb_percentage_out_of_total, Total_Protein_percentage= Total_Protein_percentage_out_of_total, Total_Fat_percentage= Total_Fat_percentage_out_of_total, Swimming_Exercise_time_to_burn_calories=Swimming_exercise_time_to_burn_calories , Jogging_Exercise_time_to_burn_calories= Jogging_exercise_time_to_burn_calories, Cycling_Exercise_time_to_burn_calories= Cycling_exercise_time_to_burn_calories ,Walking_Exercise_time_to_burn_calories=walking_exercise_time_to_burn_calories, last_date_of_analysis=datetime.datetime.now())
                # food_details.save()

                for i in name_confidence:
                    print ("name confidence i",i['name'])
                    # detecteddFood= Food_detected_disease.objects.create(foodimageid=saving_data,disease_name=i['name'],confidence=i['confidence'],last_date_of_analysis=datetime.datetime.now())
                    # detecteddFood.save()
                    # detecteddiseases= Food_detected.objects.create(foodimageid=saving_data,Food_name=i['name'],confidence=i['confidence'],last_date_of_analysis=datetime.datetime.now())
                    # detecteddiseases.save()
                    # detecteddiseases= top_disease_user_overall.objects.create(analysistype = "Food",disease1=i['name'],p1=i['confidence'],last_date_of_analysis=datetime.datetime.now())
                    # detecteddiseases.save()
                    break


                return render(request,"foodanalysis.html",{'context':final_data12,'categorie_cal':categoriewise_cal_details, 'totalcal': nutrient_details,'totalex':exercise_Details})


            except Exception as e:
                print("error",e)
                return render(request,"foodanalysis.html",{'context1':"Some Error Occur"})


# @login_required(login_url='signin')
def cough_answer(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            print ("key",key)
            print ("value",value)
        for question_id in request.POST:
            print ("question_id",question_id)
        return JsonResponse({"Questions":"in post request"},safe=False)

def index(request):
    return render (request,"index.html")


def signin(request):
    if request.user.is_authenticated:
        print ("ok")
        # return redirect("DISEASE_SELECTION1")
    if request.method == 'POST':
        print ("in sign in post")
        un =  request.POST["email"]
        pass1 =  request.POST["password"]
        user= authenticate(username=un,password=pass1)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                # return redirect("userdetails")
                print ("super")
            if user.is_active:
                # return render(request,"diseaseselection.html")
                return redirect("disease_selection")
            # return render(request,"Client/index.html")
            # return HttpResponseRedirect('/')
        else:
            return render(request,"Authentication/signin.html",{'context':"Error in username or password"})

    return render (request,"Authentication/signin.html")

def signup(request):

    if request.method == 'POST':
        print ("post")
        Username=request.POST['Username1']
        email=request.POST['email']
        try:
            print ("in dob try")
            dob=request.POST['dob']
            print ("dob",dob)
            print ("date len",len(dob))
            if len(dob)==0:
                dob = datetime.date.now()
        except Exception as e:
            print ("in dob except")
            dob = " "
            dob = datetime.datetime.now()

            print ("dob",dob)

        try:
            sex=request.POST['gender']
        except:
            sex =" "
            pass
        heigh=request.POST['Height']
        weigth=request.POST['Weight']
        try :
            activity=request.POST['activity']
        except:
            activity= " "
            pass
        try:
            Diabetes=request.POST['Diabetes']
        except:
            Diabetes = " "
            pass
        try:
            Hypertension=request.POST['Hypertension']
        except:
            Hypertension= " "
            pass
        try:
            CurrentSmoker=request.POST['CurrentSmoker']
        except:
            CurrentSmoker = " "
            pass
        try :
            PastSmoker=request.POST['PastSmoker']
        except:
            PastSmoker=" "
            pass
        password=request.POST['password']
        try :
            height_in_meter = round((int(heigh)/100),2)
            print ("height_in_meter",height_in_meter)
            BMI = round((int(weigth) / (height_in_meter * height_in_meter)),2)
        except:
            BMI =" "
            pass

        print ("user password length",len(password))
        print ("user name length",len(Username))
        print ("Username",dob)


        try:
            x = dob.split("-")
            print ("x",x)
            def ageCalculator(years, months, days,year,month,date):
                global age
                import datetime
                today = datetime.date(years,months,days)
                dob = datetime.date(year, month, date)
                years= ((today-dob).total_seconds()/ (365.242*24*3600))
                yearsInt=int(years)
                months=(years-yearsInt)*12
                monthsInt=int(months)
                days=(months-monthsInt)*(365.242/12)
                daysInt=int(days)
                print('You are {0} years, {1} months, {2} days old.'.format(yearsInt,monthsInt,daysInt))
                age = str(yearsInt) + " years " + str(monthsInt) + " Months " + str(daysInt) + " Days"
                print ("age=",age)
            b_year = int(x[0])
            b_month = int(x[1])
            b_date = int(x[2])
            now = datetime.datetime.now()
            # get year from date
            c_year = int(now.strftime("%Y"))
            # get month from date
            c_month = int(now.strftime("%m"))
            # get day from date
            c_date =int( now.strftime("%d"))
            ageCalculator(c_year,c_month,c_date,b_year,b_month,b_date)
        except:
            pass
        #creating user
        if len(Username) and len(password) != 0:
            usr = User.objects.create_user(username=Username,email=email,password=password)
            usr.save()
            #creating objec
            detail = user_detail(user=usr,dob=dob,Age=age,sex=sex,heigh=heigh,weigth=weigth,activity=activity,Diabetes=Diabetes,Hypertension=Hypertension,CurrentSmoker=CurrentSmoker,PastSmoker=PastSmoker,BMI=BMI)
            detail.save()

        return redirect('signin')
    return render (request,"Authentication/signup.html")


# @login_required(login_url='signin')
def disease_selectin1(request):
    return render(request,"diseaseselection.html")

# @login_required(login_url='signin')
def disease_selection(request):
    if request.method == 'POST':
        answer_id= request.POST.get("Option3")
        print ("answer_id",answer_id)
        if answer_id == "1":
            return redirect("questionsfever")

        if answer_id == "2":
            return redirect("questionscough")



    return render (request,"diseaseselection.html")


def logout(request):

    django_logout(request)
    return HttpResponseRedirect("/")


#######chest pain jotform########


@csrf_exempt
def ChestPain(request):
    global Cardiac_Ischemia
    global PE
    global Cardiac_Ischemia
    global Costochondritis
    global Pneumonia

    if request.method == 'GET':
        return render(request, "chestpain_qn.html")

    if request.method == 'POST':
        print("POST request accepeted and post data is", request.POST)


        try:
            print("executed try1 method")
            qn1 = request.POST['chest_qn1']

        except:
            qn1 =" "
            pass

        try:
            print("executed try2 method")
            qn2=request.POST['chest_qn2']

        except:
            qn2 =" "
            pass

        try:
            qn3=request.POST['chest_qn3']

        except:
            qn3 =" "
            pass

        try:
            qn4=request.POST['chest_qn4']

        except:
            qn4 =" "
            pass

        try:
            qn5=request.POST['chest_qn5']

        except:
            qn5 =" "
            pass

        try:
            qn6=request.POST['chest_qn6']

        except:
            qn6 =" "
            pass

        try:
            qn7=request.POST['chest_qn7']

        except:
            qn7 =" "
            pass


        Cardiac_Ischemia=0
        Pleurisy=0
        Costochondritis=0
        PE=0
        Pneumonia=0



        if qn1 == "Less than a day":
            print("qn1 option1 executed")
            Cardiac_Ischemia += 1
            PE += 1
            Pleurisy +=0.5
            Costochondritis +=0.5
            Pneumonia -= 1



        if qn1 == "More than a day":
            print("qn1 option2 executed")
            Cardiac_Ischemia+=0.25
            PE-=0.5
            Pleurisy+=0.5
            Costochondritis+=0.5
            Pneumonia+=1



        if qn2 == "Yes":
            print("qn2 executed")
            Cardiac_Ischemia-=1
            PE-=1
            Pleurisy+=0.5
            Costochondritis+=1
            Pneumonia+=0.5



        if qn3 == "Yes":
            print("qn3 executed")
            Cardiac_Ischemia-=1
            PE-=1
            Pleurisy+=0.5
            Costochondritis+=0.5
            Pneumonia+=1



        if qn4 == "Yes":
            print("qn4 executed")
            Cardiac_Ischemia-=1
            PE+=1
            Pleurisy-=1
            Costochondritis-=1
            Pneumonia+=0.5



        if qn5 == "Yes":
            Cardiac_Ischemia-=1
            PE+=1
            Pleurisy+=1
            Costochondritis+=0.5
            Pneumonia+=0.5



        if qn6 == "Yes":
            Cardiac_Ischemia+=1
            PE-=1
            Pleurisy-=1
            Costochondritis-=1
            Pneumonia-=1



        if qn7 == "Yes":
            Cardiac_Ischemia+=1
            PE+=0.5
            Pleurisy+=0.25
            Costochondritis-=0.5
            Pneumonia+=1




        context ={
            "Cardiac_Ischemia":Cardiac_Ischemia,
            "Pleurisy":Pleurisy,
            "Pneumonia":Pneumonia,
            "Costochondritis":Costochondritis,
            "Pleural_Embolism":PE,
        }
        print (context)

        x = sorted(((v,k) for k,v in context.items() if v > 0))
        print ("len of x",len(x))
        if len(x) == 0:
            context2 = {
                "Disease": "No disease found",

                }

            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Chest Pain",disease1="Disease",p1="No disease found",last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            request.session['Diagnosis']= "No Disease"
            request.session['P1_score']= "0"
            request.session['Diagnosis_type']= "ChestPain"


            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id
            return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

        if len(x) == 1:
            first_name = x[-1][1]
            first_value = x[-1][0]
            # user_diesease_update = top_disease_user_chest.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Chest Pain",disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            context2 = {
                first_name: "Most Likely",

                }
            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id
            request.session['Diagnosis']= first_name
            request.session['P1_score']= first_value
            request.session['Diagnosis_type']= "ChestPain"
            request.session['detailed User message']= "Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined You are likely to have " + first_name + ". The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms."


            return render(request,"questionscompleted.html",{'contextchestpain':context2})

            return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

        if len(x) == 2:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            # user_diesease_update = top_disease_user_chest.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Chest Pain",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            context2 = {
                first_name: "Most Likely",
                second_name :"Possible",
                }
            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id
            request.session['Diagnosis']= first_name
            request.session['P1_score']= first_value
            request.session['Diagnosis_type']= "ChestPain"
            request.session['detailed User message']= "Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined You are likely to have " + first_name + " or " + second_name + ". The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms."


            return render(request,"questionscompleted.html",{'contextchestpain':context2})



        if len(x) == 3:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            third_name = x[-3][1]
            third_value = x[-3][0]
            # user_diesease_update = top_disease_user_chest.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Chest Pain",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            context2 = {
                first_name: "Most Likely",
                second_name :"Likely",
                third_name : "Possible",
                }
            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id
            request.session['Diagnosis']= first_name
            request.session['P1_score']= first_value
            request.session['Diagnosis_type']= "ChestPain"
            request.session['detailed User message']= "Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined You are likely to have " + first_name + " or " + second_name + " or " + third_name + ". The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms."


            return render(request,"questionscompleted.html",{'contextchestpain':context2})


            # return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

        if len(x) > 3:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            third_name = x[-3][1]
            third_value = x[-3][0]
            fourth_name = x[-4][1]
            fourth_value = x[-4][0]
            # user_diesease_update = top_disease_user_chest.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Chest Pain",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            print("first_value",first_value)
            print("second_value",second_value)
            print("third_value",third_value)
            print("fourth_value",fourth_value)
            context2 = {
                first_name: "Most Likely",
                second_name :"Very Likely",
                third_name : "Likely",
                fourth_name : "Possible"

            }
            request.session['General Details']= context2
            request.session['General Details id']= user_diesease_update.id
            request.session['Diagnosis']= first_name
            request.session['P1_score']= first_value
            request.session['Diagnosis_type']= "ChestPain"
            request.session['detailed User message']= "Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined You are likely to have " + first_name + " or " + second_name + " or " + third_name + ". The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses. Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms."


            return render(request,"questionscompleted.html",{'contextchestpain':context2})










# @login_required(login_url='signin')
def chest_pain(request):

    global Cardiac_Ischemia
    global PE
    global Cardiac_Ischemia
    global Costochondritis
    global Pneumonia


    # if request.user.is_authenticated:
    #     user = request.user
    if request.method == 'GET':


        questions = chest_questions.objects.all()
        final_data1=[]
        for l in questions:
            options=[]
            all_option=chest_options_questions.objects.filter(question=l.id)
            for data in all_option:
                options.append({
                    "options_id":data.id,
                    "options_data":data.option1,
                })
            final_data1.append({
                        "question_data":l.Question,
                        "question_id":l.id,
                        "option":options,

                    })

        return render(request,"questions.html",{'generalquestions':final_data1})

    if request.method == 'POST':
        user=request.user

        Cardiac_Ischemia=0
        Pleurisy=0
        Costochondritis=0
        PE=0
        Pneumonia=0

        for question_id in request.POST:

            answer_id = request.POST[question_id]
            if question_id != "csrfmiddlewaretoken" :
                print ("questions id in if condition",question_id)
                print ("answer_id id in if condition",answer_id)
                # question_answer_save = chest_answer_details.objects.create(user=user,Question_id=question_id,Answer_id=answer_id,Diagnosis_name="ChestPain",last_date_of_analysis=datetime.datetime.now())
                # question_answer_save.save()


            if question_id == "1":

                if answer_id == "1":
                    Cardiac_Ischemia+=1
                    PE+=1
                    Pleurisy+=0.5
                    Costochondritis+=0.5
                    Pneumonia-=1

                if answer_id == "2":
                    Cardiac_Ischemia+=0.25
                    PE-=0.5
                    Pleurisy+=0.5
                    Costochondritis+=0.5
                    Pneumonia+=1

            if question_id == "2":

                if answer_id == "3":
                    Cardiac_Ischemia-=1
                    PE-=1
                    Pleurisy+=0.5
                    Costochondritis+=1
                    Pneumonia+=0.5


            if question_id =="3" :

                if answer_id == "5":
                    Cardiac_Ischemia-=1
                    PE-=1
                    Pleurisy+=0.5
                    Costochondritis+=0.5
                    Pneumonia+=1

            if question_id =="4":
                if answer_id == "7":
                    Cardiac_Ischemia-=1
                    PE+=1
                    Pleurisy-=1
                    Costochondritis-=1
                    Pneumonia+=0.5

            if question_id == "5":
                if answer_id == "9":
                    Cardiac_Ischemia-=1
                    PE+=1
                    Pleurisy+=1
                    Costochondritis+=0.5
                    Pneumonia+=0.5

            if question_id =="6":
                if answer_id == "11":
                    Cardiac_Ischemia+=1
                    PE-=1
                    Pleurisy-=1
                    Costochondritis-=1
                    Pneumonia-=1

            if question_id=="7":

                if answer_id == "13":
                    Cardiac_Ischemia+=1
                    PE+=0.5
                    Pleurisy+=0.25
                    Costochondritis-=0.5
                    Pneumonia+=1


        context ={
            "Cardiac_Ischemia":Cardiac_Ischemia,
            "Pleurisy":Pleurisy,
            "Pneumonia":Pneumonia,
            "Costochondritis":Costochondritis,
            "Pleural_Embolism":PE,
        }
        print (context)

        x = sorted(((v,k) for k,v in context.items() if v > 0))
        print ("len of x",len(x))
        if len(x) == 0:
            return render(request,"questionscompleted.html",{'nodisease':"No Disease Found"})

        if len(x) == 1:
            first_name = x[-1][1]
            first_value = x[-1][0]
            # user_diesease_update = top_disease_user_chest.objects.create(user=user,disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Chest Pain",disease1=first_name,p1=first_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            context2 = {
                first_name: "Most Likely",

                }

            return render(request,"questionscompleted.html",{'contextchestpain':context2})

            return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

        if len(x) == 2:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            # user_diesease_update = top_disease_user_chest.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()
            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Chest Pain",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            context2 = {
                first_name: "Most Likely",
                second_name :"Possible",
                }

            return render(request,"questionscompleted.html",{'contextchestpain':context2})



        if len(x) == 3:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            third_name = x[-3][1]
            third_value = x[-3][0]
            # user_diesease_update = top_disease_user_chest.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Chest Pain",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            context2 = {
                first_name: "Most Likely",
                second_name :"Likely",
                third_name : "Possible",
                }

            return render(request,"questionscompleted.html",{'contextchestpain':context2})


            # return render(request,"questionscompleted.html",{'nodisease':"bazz aa ja masti kr rya aay"})

        if len(x) > 3:
            first_name = x[-1][1]
            first_value = x[-1][0]
            second_name = x[-2][1]
            second_value = x[-2][0]
            third_name = x[-3][1]
            third_value = x[-3][0]
            fourth_name = x[-4][1]
            fourth_value = x[-4][0]
            # user_diesease_update = top_disease_user_chest.objects.create(user=user,disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            # user_diesease_update = top_disease_user_overall.objects.create(analysistype="Chest Pain",disease1=first_name,p1=first_value,disease2=second_name,p2=second_value,disease3=third_name,p3=third_value,disease4=fourth_name,p4=fourth_value,last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()

            print("first_value",first_value)
            print("second_value",second_value)
            print("third_value",third_value)
            print("fourth_value",fourth_value)
            context2 = {
                first_name: "Most Likely",
                second_name :"Very Likely",
                third_name : "Likely",
                fourth_name : "Possible"

            }

            return render(request,"questionscompleted.html",{'contextchestpain':context2})




################ Apis ###########

################ Apis ###########

@csrf_exempt
def cough_question1(request):
    if request.method == 'GET':
        questions = cough_questions.objects.all()
        final_data1=[]
        for l in questions:
            options=[]
            all_option=cough_options_questions.objects.filter(question=l.id)
            for data in all_option:
                options.append({
                    "options_id":data.id,
                    "options_data":data.option1,
                })
            if l.id == 1:
                final_data1.append({
                            "question_data":l.Question,
                            "question_id":l.id,
                            "MultiValue":True,
                            "option":options,


                        })
            else:
                final_data1.append({
                            "question_data":l.Question,
                            "question_id":l.id,
                            "MultiValue":False,
                            "option":options,

                        })
        return JsonResponse({"Details":final_data1},safe=False)
    if request.method == 'POST':
        print('POST', request.POST)
        print('BODY', request.body)
        print('JSON', json.loads(request.body))
        data =  json.loads(request.body)
        print ("length of data",len(data))
        VB=0
        BP=0
        A=0
        CHF=0
        CLD=0
        LC=0
        PE=0
        covid=0
        context1 ={

            "Viral_Bronchitis":VB,
            "Bacterial_Pneumonia":BP,
            "Asthma":A,
            "Chronic_Heart_Failure":CHF,
            "Chronic_Lung_Disease":CLD,
            "Lung_Cancer":LC,
            "Pleural_Embolism":PE,
            "covid":covid
        }
        print ("context1",context1)
        for question_id in data:
            print ("key",question_id)
            print ("value",data[question_id])
            answer_id = data[question_id]
            if question_id == "1":
                for answer_id in answer_id:
                    print ("answer_id",answer_id)
                    if answer_id=="1":
                        VB+=0
                        BP+=0
                        A+=1
                        CHF+=0.25
                        CLD+=0.25
                        LC+=0
                        PE+=0
                    if answer_id=="2":
                        VB+=0
                        BP+=0
                        A+=0.5
                        CHF+=1
                        CLD+=0.5
                        LC+=0
                        PE+=0
                    if answer_id=="3":
                        VB+=0
                        BP+=0.5
                        A+=0.5
                        CHF+=0.5
                        CLD+=1
                        LC+=0
                        PE+=0
                    if answer_id=="4":
                        VB+=0
                        BP+=0
                        A+=0
                        CHF+=0
                        CLD+=0
                        LC+=0
                        PE+=1
                    if answer_id=="5":
                        VB+=0
                        BP+=0
                        A+=1
                        CHF+=0
                        CLD+=0
                        LC+=0
                        PE+=0
                    if answer_id=="6":
                        VB+=0.5
                        BP+=0.5
                        A+=0.5
                        CHF+=0.5
                        CLD+=0.5
                        LC+=1
                        PE+=0
                    if answer_id=="7":
                        VB+=0.25
                        BP+=0.5
                        A+=0.5
                        CHF+=0.25
                        CLD+=1
                        LC+=0
                        PE+=0.5
            if question_id == "2":
                for answer_id in answer_id:
                    if answer_id == "8":
                        VB+=1
                        BP+=0.25
                        A+=0.25
                        CHF-=1
                        CLD-=1
                        LC-=1
                        PE+=1
                        covid+=1
                    if answer_id == "9":
                        VB-=0.5
                        BP+=1
                        A+=0.5
                        CHF+=0.25
                        CLD-=1
                        LC+=0.5
                        PE+=0.5
                        covid+=0.75
                    if answer_id == "10":
                        VB-=1
                        BP+=0.25
                        A+=0.75
                        CHF+=1
                        CLD+=1
                        LC+=1
                        PE-=1
                        covid-=1

            if question_id =="3" :
                for answer_id in answer_id:
                    if answer_id == "11":
                        VB+=0.25
                        BP+=1
                        A+=0.25
                        CHF+=0.25
                        CLD+=0.5
                        LC+=0.5
                        PE+=0
                        covid+=0.5

            if question_id =="4":
                for answer_id in answer_id:
                    if answer_id == "13":
                        VB+=0.25
                        BP+=0.25
                        A+=0
                        CHF+=0.25
                        CLD+=0.5
                        LC+=1
                        PE+=1
                        covid+=0.5

            if question_id == "5":
                for answer_id in answer_id:
                    if answer_id == "15":
                        VB+=1
                        BP+=0.25
                        A+=0.25
                        CHF+=0
                        CLD+=0
                        LC+=0
                        PE+=0
                        covid+=1

            if question_id =="6":
                for answer_id in answer_id:
                    if answer_id == "17":
                        VB+=0
                        BP+=0.5
                        A+=0.5
                        CHF+=1
                        CLD+=1
                        LC+=0.5
                        PE+=1
                        covid+=0.5

            if question_id=="7":
                for answer_id in answer_id:
                    if answer_id == "19":
                        VB+=0.25
                        BP+=0.25
                        A+=0.25
                        CHF+=0.5
                        CLD+=0.25
                        LC+=0.5
                        PE+=1
                        covid+=0.5

            if question_id=="8":
                for answer_id in answer_id:
                    if answer_id == "21":
                        VB-=1
                        BP+=0.25
                        A+=0
                        CHF-=1
                        CLD+=0.75
                        LC+=1
                        PE-=1
                        covid-=1


            if question_id=="9":
                for answer_id in answer_id:
                    if answer_id == "23":
                        VB+=0.25
                        BP+=0.5
                        A+=0.5
                        CHF+=1
                        CLD+=1
                        LC+=1
                        PE+=1
                        covid-=0.5

            if question_id=="10":
                for answer_id in answer_id:
                    if answer_id == "25":
                        VB-=1
                        BP-=1
                        A-=1
                        CHF+=1
                        CLD-=1
                        LC-=1
                        PE-=1
                        covid-=1

            if question_id=="11":
                for answer_id in answer_id:
                    if answer_id == "27":
                        VB+=0.25
                        BP+=0.25
                        A-=1
                        CHF-=1
                        CLD-=1
                        LC-=1
                        PE-=1
                        covid+=1


        context ={

            "Viral_Bronchitis":VB,
            "Bacterial_Pneumonia":BP,
            "Asthma":A,
            "Chronic_Heart_Failure":CHF,
            "Chronic_Lung_Disease":CLD,
            "Lung_Cancer":LC,
            "Pleural_Embolism":PE,
            "covid":covid
        }
        print (context)
        x = sorted(((v,k) for k,v in context.items()))
        # print ("len of x",len(x))
        # if len(x) == 0:
        #     return JsonResponse({"Details":"No Disease Found "},safe=False)



        first_name = x[-1][1]
        first_value = x[-1][0]
        second_name = x[-2][1]
        second_value = x[-2][0]
        third_name = x[-3][1]
        third_value = x[-3][0]
        fourth_name = x[-4][1]
        fourth_value = x[-4][0]

        print("first_value",first_value)
        print("second_value",second_value)
        print("third_value",third_value)
        print("fourth_value",fourth_value)
        context2 = {
            "bloodrep": "blood/questions/cough/",
            "cxr_image" :"chest/images/api/",

        }

        return JsonResponse({"Details":context,"Extra_modules":context2},safe=False)



@csrf_exempt
def blood_cough_question1(request):
    if request.method == 'GET':
        questions = blood_questions.objects.all()
        final_data1=[]
        for l in questions:
            options=[]
            all_option=blood_options_questions.objects.filter(question=l.id)
            for data in all_option:
                options.append({
                    "options_id":data.id,
                    "options_data":data.option1,
                })
            final_data1.append({
                        "question_data":l.Question,
                        "question_id":l.id,
                        "MultiValue":False,
                        "option":options,

                    })

        return JsonResponse({"Details":final_data1},safe=False)

    if request.method == 'POST':
        print('POST', request.POST)
        print('BODY', request.body)
        print('JSON', json.loads(request.body))
        data =  json.loads(request.body)
        print ("length of data",len(data))
        Viral_Bronchitis= data['diseasedic']['Viral_Bronchitis']
        Bacterial_Pneumonia= data['diseasedic']['Bacterial_Pneumonia']
        Asthma= data['diseasedic']['Asthma']
        Chronic_Heart_Failure= data['diseasedic']['Chronic_Heart_Failure']
        Chronic_Lung_Disease= data['diseasedic']['Chronic_Lung_Disease']
        Lung_Cancer= data['diseasedic']['Lung_Cancer']
        Pleural_Embolism= data['diseasedic']['Pleural_Embolism']
        covid= data['diseasedic']['covid']
        for question_id in data:
            print ("key",question_id)
            print ("value",data[question_id])
            answer_id = data[question_id]


            if question_id == "8":
                for answer_id in answer_id:
                    if answer_id=="11":
                        Bacterial_Pneumonia+=1
            if question_id == "9":
                for answer_id in answer_id:
                    if answer_id=="12":
                        Viral_Bronchitis+=1
                        Pleural_Embolism+=0.5
                    if answer_id=="13":
                        Bacterial_Pneumonia+=0.5
                        Pleural_Embolism+=0.5

            if question_id == "10":
                for answer_id in answer_id:
                    if answer_id=="14":
                        Lung_Cancer+=0.5

            if question_id == "13":
                for answer_id in answer_id:
                    if answer_id=="17":
                        Chronic_Heart_Failure+=1
            if question_id == "14":
                print ("Chronic_Heart_Failure",Chronic_Heart_Failure)
                for answer_id in answer_id:
                    print ("answer_id",answer_id)
                    print ("Chronic_Heart_Failure",Chronic_Heart_Failure)
                    if answer_id=="18":
                        print (" inside Chronic_Heart_Failure",Chronic_Heart_Failure)
                        Chronic_Heart_Failure+=1
            if question_id == "15":
                for answer_id in answer_id:
                    if answer_id=="19":
                        Lung_Cancer+=1
            print ("Chronic_Heart_Failure",Chronic_Heart_Failure)
        context ={

            "Viral_Bronchitis":Viral_Bronchitis,
            "Bacterial_Pneumonia":Bacterial_Pneumonia,
            "Asthma":Asthma,
            "Chronic_Heart_Failure":Chronic_Heart_Failure,
            "Chronic_Lung_Disease":Chronic_Lung_Disease,
            "Lung_Cancer":Lung_Cancer,
            "Pleural_Embolism":Pleural_Embolism,
            "covid":covid
        }
        print ("Disease Dictionary",data['diseasedic']['Viral_Bronchitis'])
        return JsonResponse({"Details":context},safe=False)



@csrf_exempt
def fever_question1(request):
    if request.method == 'GET':
        questions = fever_questions.objects.all()
        final_data1=[]
        for l in questions:
            options=[]
            all_option=fever_options_questions.objects.filter(question=l.id)
            for data in all_option:
                options.append({
                    "options_id":data.id,
                    "options_data":data.option1,
                })
            final_data1.append({
                        "question_data":l.Question,
                        "question_id":l.id,
                        "MultiValue":False,
                        "option":options,

                    })

        return JsonResponse({"Details":final_data1},safe=False)
    if request.method == 'POST':
        print('POST', request.POST)
        print('BODY', request.body)
        print('JSON', json.loads(request.body))
        data =  json.loads(request.body)
        print ("Data",data)
        Viral_Fever =0
        COVID=0
        Pneumonia=0
        Cholangitis=0
        Endocarditis=0
        Cellulitis=0
        UTI=0
        Osteomyelitis=0
        Meningitis=0
        for question_id in data:
            print ("key",question_id)
            print ("value",data[question_id])
            answer_id = data[question_id]
            if question_id == "1":
                for answer_id in answer_id:
                    if answer_id == "1":
                        Viral_Fever+=1
                        COVID+=0.5
                        Pneumonia+=0.25
                        Cholangitis+=0.5
                        Endocarditis-=1
                        Cellulitis+=0
                        UTI+=0
                        Osteomyelitis-=1
                        Meningitis+=1

                    if answer_id == "2":
                        Viral_Fever+=0
                        COVID+=0.5
                        Pneumonia+=1
                        Cholangitis+=0.5
                        Endocarditis+=1
                        Cellulitis+=1
                        UTI+=1
                        Osteomyelitis+=1
                        Meningitis+=0.5

            if question_id == "2":
                for answer_id in answer_id:
                    if answer_id == "3":
                        Viral_Fever+=1
                        COVID+=0.5
                        Pneumonia+=0
                        Cholangitis-=1
                        Endocarditis-=1
                        Cellulitis-=1
                        UTI-=1
                        Osteomyelitis-=1
                        Meningitis+=0

            if question_id =="3" :
                for answer_id in answer_id:
                    if answer_id == "5":
                        Viral_Fever+=1
                        COVID+=1
                        Pneumonia+=1
                        Cholangitis-=1
                        Endocarditis-=1
                        Cellulitis-=1
                        UTI-=1
                        Osteomyelitis-=1
                        Meningitis+=0.5

            if question_id =="4":
                for answer_id in answer_id:
                    if answer_id == "7":
                        Viral_Fever+=0
                        COVID-=1
                        Pneumonia+=0
                        Cholangitis+=0
                        Endocarditis+=0
                        Cellulitis+=0
                        UTI+=0
                        Osteomyelitis+=0
                        Meningitis+=0.75

            if question_id == "5":
                for answer_id in answer_id:
                    if answer_id == "9":
                        Viral_Fever+=0.25
                        COVID+=0.25
                        Pneumonia+=1
                        Cholangitis-=1
                        Endocarditis-=1
                        Cellulitis-=1
                        UTI-=1
                        Osteomyelitis-=1
                        Meningitis+=0

            if question_id =="6":
                for answer_id in answer_id:
                    if answer_id == "11":
                        Viral_Fever-=0.5
                        COVID+=0.5
                        Pneumonia+=1
                        Cholangitis-=1
                        Endocarditis+=0.25
                        Cellulitis-=1
                        UTI-=1
                        Osteomyelitis-=1
                        Meningitis+=0
            if question_id=="7":
                for answer_id in answer_id:

                    if answer_id == "13":
                        Viral_Fever+=0.25
                        COVID+=0.5
                        Pneumonia+=0.5
                        Cholangitis-=1
                        Endocarditis+=0.5
                        Cellulitis-=1
                        UTI-=1
                        Osteomyelitis-=1
                        Meningitis-=1

            if question_id=="8":
                for answer_id in answer_id:
                    if answer_id == "15":
                        Viral_Fever-=1
                        COVID+=0
                        Pneumonia+=0
                        Cholangitis+=1
                        Endocarditis-=1
                        Cellulitis-=1
                        UTI+=1
                        Osteomyelitis-=1
                        Meningitis-=1

            if question_id=="9":
                for answer_id in answer_id:

                    if answer_id == "17":
                        Viral_Fever+=0.25
                        COVID+=0
                        Pneumonia+=0
                        Cholangitis+=1
                        Endocarditis+=0
                        Cellulitis+=0
                        UTI+=0
                        Osteomyelitis-=1
                        Meningitis-=1

            if question_id=="10":
                for answer_id in answer_id:
                    if answer_id == "19":
                        Viral_Fever-=1
                        COVID-=1
                        Pneumonia-=1
                        Cholangitis+=1
                        Endocarditis-=0
                        Cellulitis-=1
                        UTI-=1
                        Osteomyelitis-=1
                        Meningitis-=1

            if question_id=="11":
                for answer_id in answer_id:
                    if answer_id == "21":
                        Viral_Fever-=1
                        COVID-=1
                        Pneumonia-=0.5
                        Cholangitis+=0.5
                        Endocarditis+=1
                        Cellulitis-=1
                        UTI-=1
                        Osteomyelitis+=1
                        Meningitis-=1

            if question_id=="12":
                for answer_id in answer_id:
                    if answer_id == "23":
                        Viral_Fever-=1
                        COVID-=1
                        Pneumonia-=1
                        Cholangitis-=1
                        Endocarditis+=0.5
                        Cellulitis+=1
                        UTI-=1
                        Osteomyelitis+=1
                        Meningitis-=1

            if question_id=="13":
                for answer_id in answer_id:
                    if answer_id == "25":
                        Viral_Fever-=1
                        COVID-=1
                        Pneumonia-=1
                        Cholangitis-=1
                        Endocarditis-=1
                        Cellulitis-=1
                        UTI+=1
                        Osteomyelitis-=1
                        Meningitis+=0

            if question_id=="14":
                for answer_id in answer_id:
                    if answer_id == "27":
                        Viral_Fever+=0.25
                        COVID+=0.5
                        Pneumonia+=0.5
                        Cholangitis-=1
                        Endocarditis+=0.5
                        Cellulitis-=1
                        UTI+=0
                        Osteomyelitis+=0
                        Meningitis+=1

            if question_id=="15":
                for answer_id in answer_id:
                    if answer_id == "29":
                        Viral_Fever-=1
                        COVID+=0.25
                        Pneumonia+=0.25
                        Cholangitis-=1
                        Endocarditis+=0
                        Cellulitis-=1
                        UTI-=1
                        Osteomyelitis-=1
                        Meningitis+=1

            if question_id=="16":
                for answer_id in answer_id:

                    if answer_id == "31":
                        Viral_Fever-=1
                        COVID+=0
                        Pneumonia+=0
                        Cholangitis-=1
                        Endocarditis+=0
                        Cellulitis-=1
                        UTI-=1
                        Osteomyelitis-=1
                        Meningitis+=1

        context ={
            "Viral_Fever":Viral_Fever,
            "COVID":COVID,
            "Pneumonia":Pneumonia,
            "Cholangitis":Cholangitis,
            "Endocarditis":Endocarditis,
            "Cellulitis":Cellulitis,
            "UTI":UTI,
            "Osteomyelitis":Osteomyelitis,
            "Meningitis":Meningitis,
        }
        print (context)
        x = sorted(((v,k) for k,v in context.items()))
        # print ("len of x",len(x))
        # if len(x) == 0:
        #     return JsonResponse({"Details":"No Disease Found "},safe=False)


        first_name = x[-1][1]
        first_value = x[-1][0]
        second_name = x[-2][1]
        second_value = x[-2][0]
        third_name = x[-3][1]
        third_value = x[-3][0]
        fourth_name = x[-4][1]
        fourth_value = x[-4][0]

        print("first_value",first_value)
        print("second_value",second_value)
        print("third_value",third_value)
        print("fourth_value",fourth_value)
        context2 = {
            "bloodrep": "blood/questions/fever/",
        }

        return JsonResponse({"Details":context,"Extra_modules":context2},safe=False)


@csrf_exempt
def blood_fever_question1(request):
    if request.method == 'GET':
        questions = blood_questions.objects.all()
        final_data1=[]
        for l in questions:
            options=[]
            all_option=blood_options_questions.objects.filter(question=l.id)
            for data in all_option:
                options.append({
                    "options_id":data.id,
                    "options_data":data.option1,
                })
            final_data1.append({
                        "question_data":l.Question,
                        "question_id":l.id,
                        "MultiValue":False,
                        "option":options,

                    })

        return JsonResponse({"Details":final_data1},safe=False)

    if request.method == 'POST':
        print('POST', request.POST)
        print('BODY', request.body)
        print('JSON', json.loads(request.body))
        data =  json.loads(request.body)
        print ("length of data",len(data))
        Viral_Fever= data['diseasedic']['Viral_Fever']
        COVID= data['diseasedic']['COVID']
        Pneumonia= data['diseasedic']['Pneumonia']
        Cholangitis= data['diseasedic']['Cholangitis']
        Endocarditis= data['diseasedic']['Endocarditis']
        Cellulitis= data['diseasedic']['Cellulitis']
        UTI= data['diseasedic']['UTI']
        Osteomyelitis= data['diseasedic']['Osteomyelitis']
        Meningitis= data['diseasedic']['Meningitis']

        for question_id in data:
            print ("key",question_id)
            print ("value",data[question_id])
            answer_id = data[question_id]
            print("Viral_Fever",Viral_Fever)
            print("COVID",COVID)
            print("Pneumonia",Pneumonia)
            print("Cholangitis",Cholangitis)
            print("Endocarditis",Endocarditis)
            print("Cellulitis",Cellulitis)
            print("UTI",UTI)
            print("Osteomyelitis",Osteomyelitis)
            print("Meningitis",Meningitis)


            if question_id =="7":
                for answer_id in answer_id:
                    if answer_id =="10":
                        Endocarditis+=1
            ####k
            if question_id =="8":
                for answer_id in answer_id:
                    if answer_id == "11":
                        # Viral_Fever+=1
                        # COVID+=0.5
                        Pneumonia+=1
                        Cholangitis+=1
                        Endocarditis+=1
                        Cellulitis+=1
                        UTI+=1
                        Osteomyelitis+=1
                        Meningitis+=1
            ### L M
            if question_id == "9":
                for answer_id in answer_id:
                    if answer_id == "12":
                        Osteomyelitis+=1
                        COVID+=1
                    if answer_id == "13":
                        Pneumonia+=1
                        Osteomyelitis+=1
            ### N
            if question_id =="10":
                for answer_id in answer_id:
                    if answer_id =="14":
                        Cholangitis+=1
                        Endocarditis+=1

            ### P
            if question_id =="12":
                for answer_id in answer_id:
                    if answer_id =="16":
                        Cholangitis+=1
                        Endocarditis+=1



            ####Q
            if question_id =="13":
                for answer_id in answer_id:
                    if answer_id =="17":
                        UTI+=1

            ####R
            if question_id =="14":
                for answer_id in answer_id:
                    if answer_id =="18":
                        UTI+=1
        context ={
                "Viral_Fever":Viral_Fever,
                "COVID":COVID,
                "Pneumonia":Pneumonia,
                "Cholangitis":Cholangitis,
                "Endocarditis":Endocarditis,
                "Cellulitis":Cellulitis,
                "UTI":UTI,
                "Osteomyelitis":Osteomyelitis,
                "Meningitis":Meningitis,
            }

        return JsonResponse({"Details":context},safe=False)



@csrf_exempt
def abdominal_question1(request):
    if request.method == 'GET':
        questions = abdominal_questions.objects.all()
        final_data1=[]
        for l in questions:
            options=[]
            all_option=abdominal_options_questions.objects.filter(question=l.id)
            for data in all_option:
                options.append({
                    "options_id":data.id,
                    "options_data":data.option1,
                })
            final_data1.append({
                        "question_data":l.Question,
                        "question_id":l.id,
                        "MultiValue":False,
                        "option":options,

                    })

        return JsonResponse({"Details":final_data1},safe=False)

    if request.method == 'POST':
        print('POST', request.POST)
        print('BODY', request.body)
        print('JSON', json.loads(request.body))
        data =  json.loads(request.body)
        print ("length of data",len(data))

        Appendicitis= 0
        Cholecystitis= 0
        Cystitis= 0
        Pyelonephritis= 0
        Renal_Calculi= 0
        Diverticulitis= 0
        Inflammatory_Bowel= 0
        Irritable_Bowel= 0

        Pancreatitis= 0
        Endometriosis= 0
        Gastritis = 0

        for question_id in data:
            print ("key",question_id)
            print ("value",data[question_id])
            answer_id = data[question_id]
            if question_id == "1":
                for answer_id in answer_id:

                # (VB1, BP.25, A.5, CHF-1, CLD-1, LC-1, PE.75)
                    if answer_id == "1":
                        Appendicitis+=1
                        Cholecystitis+=0.5
                        Cystitis+=0.5
                        Pyelonephritis+=0.5
                        Renal_Calculi+=1
                        Diverticulitis+=0.25
                        Inflammatory_Bowel+=0.5
                        Irritable_Bowel+=0

                        Pancreatitis+=0.5
                        Endometriosis+=0
                        Gastritis +=0.5
                    #  (VB-.5, BP1, A.5, CHF0, CLD0, LC0, PE.25)
                    if answer_id == "2":
                        Appendicitis-=0.5
                        Cholecystitis+=0.5
                        Cystitis+=0.5
                        Pyelonephritis+=0.5
                        Renal_Calculi-=1
                        Diverticulitis+=0.75
                        Inflammatory_Bowel+=0.5
                        Irritable_Bowel+=1

                        Pancreatitis+=0.5
                        Endometriosis+=1
                        Gastritis +=0.5

            if question_id == "2":
                for answer_id in answer_id:
                # (VB1, BP.25, A.5, CHF-1, CLD-1, LC-1, PE.75)
                    if answer_id == "3":
                        Appendicitis+=0.75
                        Cholecystitis+=1
                        Cystitis+=0
                        Pyelonephritis+=0.75
                        Renal_Calculi+=0.5
                        Diverticulitis+=1
                        Inflammatory_Bowel+=0.5
                        Irritable_Bowel+=0.5

                        Pancreatitis+=1
                        Endometriosis+=0
                        Gastritis +=0.5

            if question_id =="3" :
                for answer_id in answer_id:

                    if answer_id == "5":
                        Appendicitis+=0.75
                        Cholecystitis+=1
                        Cystitis+=0.5
                        Pyelonephritis+=1
                        Renal_Calculi+=0
                        Diverticulitis+=0.75
                        Inflammatory_Bowel+=0.75
                        Irritable_Bowel-=1

                        Pancreatitis+=0.5
                        Endometriosis-=1
                        Gastritis-=1

            if question_id =="4":
                for answer_id in answer_id:
                    if answer_id == "7":
                        Appendicitis-=1
                        Cholecystitis-=1
                        Cystitis+=1
                        Pyelonephritis+=1
                        Renal_Calculi+=1
                        Diverticulitis+=0
                        Inflammatory_Bowel+=0
                        Irritable_Bowel+=0
                        Pancreatitis-=1
                        Endometriosis+=0.5
                        Gastritis-=1

            if question_id == "5":
                for answer_id in answer_id:
                    if answer_id == "9":
                        Appendicitis-=1
                        Cholecystitis-=1
                        Cystitis+=1
                        Pyelonephritis+=1
                        Renal_Calculi+=1
                        Diverticulitis-=1
                        Inflammatory_Bowel-=1
                        Irritable_Bowel-=1
                        Pancreatitis-=1
                        Endometriosis-=1
                        Gastritis-=1

            if question_id =="6":
                for answer_id in answer_id:
                    if answer_id == "11":
                        Appendicitis+=0.5
                        Cholecystitis+=0.5
                        Cystitis+=0.5
                        Pyelonephritis+=0.5
                        Renal_Calculi+=0.5
                        Diverticulitis+=1
                        Inflammatory_Bowel+=1
                        Irritable_Bowel+=1
                        Pancreatitis+=0.5
                        Endometriosis+=0.5
                        Gastritis-=1

            if question_id=="7":
                for answer_id in answer_id:
                    if answer_id == "13":
                        Appendicitis-=0.5
                        Cholecystitis-=0.5
                        Cystitis-=1
                        Pyelonephritis-=1
                        Renal_Calculi-=1
                        Diverticulitis+=0.75
                        Inflammatory_Bowel+=1
                        Irritable_Bowel-=1
                        Pancreatitis+=0
                        Endometriosis-=1
                        Gastritis-=1

            if question_id=="8":
                for answer_id in answer_id:
                    if answer_id == "15":
                        Appendicitis+=0.25
                        Cholecystitis+=0
                        Cystitis-=1
                        Pyelonephritis-=1
                        Renal_Calculi-=1
                        Diverticulitis+=0.5
                        Inflammatory_Bowel+=1
                        Irritable_Bowel-=1
                        Pancreatitis+=0.5
                        Endometriosis-=1
                        Gastritis-=1

            if question_id=="9":
                for answer_id in answer_id:
                # •	Yes (VB.25, BP.5, A.5, CHF1, CLD1, LC1, PE1)
                    if answer_id == "17":
                        Appendicitis-=1
                        Cholecystitis-=1
                        Cystitis-=1
                        Pyelonephritis-=1
                        Renal_Calculi-=1
                        Diverticulitis-=1
                        Inflammatory_Bowel-=1
                        Irritable_Bowel-=1
                        Pancreatitis-=1
                        Endometriosis+=1
                        Gastritis-=1

            if question_id=="10":
                for answer_id in answer_id:
                    if answer_id == "19":
                        Appendicitis-=1
                        Cholecystitis-=0.5
                        Cystitis-=1
                        Pyelonephritis-=1
                        Renal_Calculi-=1
                        Diverticulitis+=0.5
                        Inflammatory_Bowel+=1
                        Irritable_Bowel-=1
                        Pancreatitis+=0.75
                        Endometriosis-=1
                        Gastritis-=1

            if question_id=="11":
                for answer_id in answer_id:
                # •	Yes (VB.25, BP.5, A.5, CHF1, CLD1, LC1, PE1)
                    if answer_id == "21":
                        Appendicitis+=0.5
                        Cholecystitis+=0.5
                        Cystitis+=0.25
                        Pyelonephritis+=0.25
                        Renal_Calculi+=0.25
                        Diverticulitis+=1
                        Inflammatory_Bowel+=1
                        Irritable_Bowel+=1
                        Pancreatitis+=0.5
                        Endometriosis+=0.5
                        Gastritis+=0.5

            if question_id=="12":
                for answer_id in answer_id:
                    if answer_id == "23":
                        Appendicitis-=1
                        Cholecystitis-=1
                        Cystitis-=1
                        Pyelonephritis-=1
                        Renal_Calculi-=1
                        Diverticulitis+=0
                        Inflammatory_Bowel+=0
                        Irritable_Bowel+=0
                        Pancreatitis+=0
                        Endometriosis-=1
                        Gastritis+=1

            if question_id=="13":
                for answer_id in answer_id:
                    if answer_id == "25":
                        Appendicitis+=0
                        Cholecystitis+=0.5
                        Cystitis+=0
                        Pyelonephritis+=0
                        Renal_Calculi+=0
                        Diverticulitis+=0
                        Inflammatory_Bowel+=0
                        Irritable_Bowel+=0
                        Pancreatitis+=1
                        Endometriosis+=0
                        Gastritis+=0.5

            if question_id=="14":
                for answer_id in answer_id:
                    if answer_id == "27":
                        Appendicitis-=1
                        Cholecystitis+=1
                        Cystitis-=1
                        Pyelonephritis+=0.5
                        Renal_Calculi+=0.5
                        Diverticulitis-=1
                        Inflammatory_Bowel-=1
                        Irritable_Bowel-=1
                        Pancreatitis+=1
                        Endometriosis+=1
                        Gastritis+=1

            if question_id=="15":
                for answer_id in answer_id:
                    if answer_id == "29":
                        Appendicitis+=1
                        Cholecystitis-=1
                        Cystitis+=1
                        Pyelonephritis+=0.5
                        Renal_Calculi+=0.5
                        Diverticulitis+=1
                        Inflammatory_Bowel+=1
                        Irritable_Bowel+=1
                        Pancreatitis-=0.5
                        Endometriosis+=1
                        Gastritis-=1


        context ={

            "Appendicitis":Appendicitis,
            "Cholecystitis":Cholecystitis,
            "Cystitis":Cystitis,
            "Pyelonephritis":Pyelonephritis,
            "Renal_Calculi":Renal_Calculi,
            "Diverticulitis":Diverticulitis,
            "Inflammatory_Bowel":Inflammatory_Bowel,
            "Irritable_Bowel":Irritable_Bowel,
            "Pancreatitis":Pancreatitis,
            "Endometriosis":Endometriosis,
            "Gastritis":Gastritis
        }

        x = sorted(((v,k) for k,v in context.items() ))
        # print ("len of x",len(x))
        # if len(x) == 0:
        #     return JsonResponse({"Details":"No Disease Found "},safe=False)



        first_name = x[-1][1]
        first_value = x[-1][0]
        second_name = x[-2][1]
        second_value = x[-2][0]
        third_name = x[-3][1]
        third_value = x[-3][0]
        fourth_name = x[-4][1]
        fourth_value = x[-4][0]

        print("first_value",first_value)
        print("second_value",second_value)
        print("third_value",third_value)
        print("fourth_value",fourth_value)
        context2 = {
            "bloodrep": "blood/questions/abdominal/",
        }

        return JsonResponse({"Details":context,"Extra_modules":context2},safe=False)

@csrf_exempt
def blood_abdominal_question1(request):
    if request.method == 'GET':
        questions = blood_questions.objects.all()
        final_data1=[]
        for l in questions:
            options=[]
            all_option=blood_options_questions.objects.filter(question=l.id)
            for data in all_option:
                options.append({
                    "options_id":data.id,
                    "options_data":data.option1,
                })
            final_data1.append({
                        "question_data":l.Question,
                        "question_id":l.id,
                        "MultiValue":False,
                        "option":options,

                    })

        return JsonResponse({"Details":final_data1},safe=False)

    if request.method == 'POST':
        print('POST', request.POST)
        print('BODY', request.body)
        print('JSON', json.loads(request.body))
        data =  json.loads(request.body)
        print ("length of data",len(data))
        Appendicitis= data['diseasedic']['Appendicitis']
        Cholecystitis= data['diseasedic']['Cholecystitis']
        Cystitis= data['diseasedic']['Cystitis']
        Pyelonephritis= data['diseasedic']['Pyelonephritis']
        Renal_Calculi= data['diseasedic']['Renal_Calculi']
        Diverticulitis= data['diseasedic']['Diverticulitis']
        Inflammatory_Bowel= data['diseasedic']['Inflammatory_Bowel']
        Irritable_Bowel= data['diseasedic']['Irritable_Bowel']
        Pancreatitis= data['diseasedic']['Pancreatitis']
        Endometriosis= data['diseasedic']['Endometriosis']
        Gastritis= data['diseasedic']['Gastritis']

        for question_id in data:
            print("Appendicitis",Appendicitis)
            print("Cholecystitis",Cholecystitis)
            print("Cystitis",Cystitis)
            print("Pyelonephritis",Pyelonephritis)
            print("Renal_Calculi",Renal_Calculi)
            print("Diverticulitis",Diverticulitis)
            print("Inflammatory_Bowel",Inflammatory_Bowel)
            print("Irritable_Bowel",Irritable_Bowel)

            print("Pancreatitis",Pancreatitis)
            print("Endometriosis",Endometriosis)
            print("Gastritis",Gastritis)
            answer_id = data[question_id]

            if question_id =="8":
                for answer_id in answer_id:
                    if answer_id == "11":
                        # Appendicitis-=1
                        #     Cholecystitis-=1
                        #     Cystitis+=1
                        Pyelonephritis+=1
                        Renal_Calculi+=1
                        Diverticulitis+=1
                        Inflammatory_Bowel+=1
                        #     Irritable_Bowel+=0

                        #     Pancreatitis+=0
                        #     Endometriosis-=1
                        Appendicitis+=1
                        Cholecystitis+=1
                        Cystitis+=1
            ### L M
            if question_id == "9":
                for answer_id in answer_id:
                    if answer_id == "13":
                        Appendicitis+=1
            ### U V
            ### N
            if question_id =="10":
                for answer_id in answer_id:
                    if answer_id =="14":
                        Cholecystitis+=1
                        Pancreatitis+=1
            ### O
            if question_id =="11":
                for answer_id in answer_id:
                    if answer_id =="15":
                        Inflammatory_Bowel+=1
                        Pancreatitis+=1

            ### P
            if question_id =="12":
                for answer_id in answer_id:
                    if answer_id =="16":
                        Cholecystitis+=1
            ####Q
            if question_id =="13":
                for answer_id in answer_id:
                    if answer_id =="17":
                        Pyelonephritis+=1
                        Renal_Calculi+=1
            ####R
            if question_id =="14":
                for answer_id in answer_id:
                    if answer_id =="18":
                        Renal_Calculi+=1
                        Pyelonephritis+=1
        context ={

                    "Appendicitis":Appendicitis,
                    "Cholecystitis":Cholecystitis,
                    "Cystitis":Cystitis,
                    "Pyelonephritis":Pyelonephritis,
                    "Renal_Calculi":Renal_Calculi,
                    "Diverticulitis":Diverticulitis,
                    "Inflammatory_Bowel":Inflammatory_Bowel,
                    "Irritable_Bowel":Irritable_Bowel,

                    "Pancreatitis":Pancreatitis,
                    "Endometriosis":Endometriosis,
                    "Gastritis":Gastritis
                }

        return JsonResponse({"Details":context},safe=False)




@csrf_exempt
def blood_question1(request):
    if request.method == 'GET':
        questions = blood_questions.objects.all()
        final_data1=[]
        for l in questions:
            options=[]
            all_option=blood_options_questions.objects.filter(question=l.id)
            for data in all_option:
                options.append({
                    "options_id":data.id,
                    "options_data":data.option1,
                })
            final_data1.append({
                        "question_data":l.Question,
                        "question_id":l.id,
                        "MultiValue":False,
                        "option":options,

                    })

        return JsonResponse({"Details":final_data1},safe=False)

    if request.method == 'POST':
        for key, value in request.POST.items():
            print ("key",key)
            print ("value",value)
        for question_id in request.POST:
            print ("question_id",question_id)
        return JsonResponse({"Questions":"in post request"},safe=False)



@csrf_exempt
def apisignup(request):

    if request.method == 'POST':
        print('POST', request.POST)
        print('BODY', request.body)
        print('JSON', json.loads(request.body))
        data =  json.loads(request.body)
        print ("length of data",len(data))

        print ("type of data",type(data))
        print ("post",data['username'])
        check = User.objects.filter(username=data['username'])
        if len(check)==1:

            return JsonResponse({"errorMessage":"user already exists"},status=400)



        try :
            height_in_meter = round((int(data['heigh'])/100),2)
            print ("height_in_meter",height_in_meter)
            BMI = round((int(data['weigth']) / (height_in_meter * height_in_meter)),2)
        except:
            BMI =" "

        try:
            x = data['dob'].split("-")
            print ("x",x)
            def ageCalculator(years, months, days,year,month,date):
                global age
                import datetime
                today = datetime.date(years,months,days)
                dob = datetime.date(year, month, date)
                years= ((today-dob).total_seconds()/ (365.242*24*3600))
                yearsInt=int(years)
                months=(years-yearsInt)*12
                monthsInt=int(months)
                days=(months-monthsInt)*(365.242/12)
                daysInt=int(days)
                print('You are {0} years, {1} months, {2} days old.'.format(yearsInt,monthsInt,daysInt))
                age = str(yearsInt) + " years " + str(monthsInt) + " Months " + str(daysInt) + " Days"
                print ("age=",age)
            b_year = int(x[0])
            b_month = int(x[1])
            b_date = int(x[2])
            now = datetime.datetime.now()
            # get year from date
            c_year = int(now.strftime("%Y"))
            # get month from date
            c_month = int(now.strftime("%m"))
            # get day from date
            c_date =int( now.strftime("%d"))
            ageCalculator(c_year,c_month,c_date,b_year,b_month,b_date)
        except:
            pass
        # #creating user

        usr = User.objects.create_user(username=data['username'],email=data['email'],password=data['password'])
        usr.save()
        #creating objec
        detail = user_detail(user=usr,dob=data['dob'],Age=age,sex=data['sex'],heigh=data['heigh'],weigth=data['weigth'],activity=data['activity'],Diabetes=data['Diabetes'],Hypertension=data['Hypertension'],CurrentSmoker=data['CurrentSmoker'],PastSmoker=data['PastSmoker'],BMI=BMI)
        detail.save()

        return JsonResponse({"Message":"Signed Up"},safe=False)
    return JsonResponse({"Message":"Not Signed Up"},safe=False)



# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)


class chest_Condition1(APIView):
    print ("in function")
    def post(self, request, format=None):
        try:
            try:
                file = request.data.get('fileup')
                print ("file",file)
                dicti = request.data.get('diseasedic')
                print ("dicti",dicti)
                print ("dicti",type(dicti))
                data= json.loads(dicti)
                print ("dicti",type(dicti))

                Viral_Bronchitis= data['Viral_Bronchitis']
                Bacterial_Pneumonia= data['Bacterial_Pneumonia']
                Asthma= data['Asthma']
                Chronic_Heart_Failure= data['Chronic_Heart_Failure']
                Chronic_Lung_Disease= data['Chronic_Lung_Disease']
                Lung_Cancer= data['Lung_Cancer']
                Pleural_Embolism= data['Pleural_Embolism']
                covid= data['covid']
                print ("Viral_Bronchitis",data['Viral_Bronchitis'])
            except Exception as e:
                print (e)
            staticPrefix = "static"
            filename = str(file)
            print ("filename",filename)

            filepath = 'images/' + filename
            print ("filepath",filepath)
            with default_storage.open(filepath, 'wb+') as destination:
                for chunk in file.chunks():
                    # print ("chunk",chunk)
                    destination.write(chunk)
                    print ("desdestination",destination )

            # getting results
            results = model_cxr('media/'+filepath)
            print ("results",results)
            # for croping

            _, result_dir = results.crop(save=True)
            print ("result_dir",result_dir)
            # converting detection result to json format
            data = results.pandas().xyxy[0].to_json(orient="records")
            print ("previous data",data)

            try :
                # normalizing result_dir
                tmp = finders.find(result_dir)
                print ("tmp",tmp)
            except Exception as e:
                print ("normalizing result_dir",e)

            searched_loc = finders.searched_locations
            print ("searched_loc",searched_loc)

            modified_res_loc = os.path.relpath(tmp, searched_loc[0])
            print ("modified_res_loc",modified_res_loc)

            result_dir = str(result_dir.as_posix())
            print ("result_dir",result_dir)


            data = json.loads(data)
            print ("here is the complete data",len(data))

            unique_fruits = {}
            for fruit in data:
                unique_fruits[fruit.get('name')] = []
                print ("unique_fruits",unique_fruits)


            for fruit in unique_fruits:
                file_list = os.listdir(result_dir+'/crops/'+fruit)
                unique_fruits[fruit] = file_list
                print ("file_list",file_list)


            name_confidence = []
            final_data = []
            # i  = 0
            for record in data:
                name_confidence.append({
                    "name": record.get('name'),
                    "confidence": record.get('confidence')
                })
                final_data.append({
                    "name": record.get('name'),
                    "confidence": record.get('confidence'),
                    "image_url": staticPrefix+'/' + modified_res_loc + '/crops/' + record.get('name') + '/' + unique_fruits[record.get('name')].pop(0)
                })
                break
            print ("first type",type(name_confidence))
            print ("name_confidence",name_confidence)

            if name_confidence[0]["name"] == "Effusion":
                Chronic_Heart_Failure+=1
                Chronic_Lung_Disease+=1
                Lung_Cancer+=0.5
                print ("in if Effusion")
            if name_confidence[0]["name"] == "Pneumonia":
                Bacterial_Pneumonia+=1
                Chronic_Lung_Disease+=1
                Lung_Cancer+=0.5
                covid+=1

                print ("in if Pneumonia")
            if name_confidence[0]["name"] == "Nodules":
                Lung_Cancer+=1

                print ("in if Nodules")
            if name_confidence[0]["name"] == "Normal":
                print ("in if Normal")
                Viral_Bronchitis+=0.5
                Asthma+=0.75
                Pleural_Embolism+=0.5
                covid+=0.5

            resultant_data = {
                "data": final_data,
                "actual_image_url": staticPrefix + '/'+modified_res_loc+'/'+filename
            }
            context ={

            "Viral_Bronchitis":Viral_Bronchitis,
            "Bacterial_Pneumonia":Bacterial_Pneumonia,
            "Asthma":Asthma,
            "Chronic_Heart_Failure":Chronic_Heart_Failure,
            "Chronic_Lung_Disease":Chronic_Lung_Disease,
            "Lung_Cancer":Lung_Cancer,
            "Pleural_Embolism":Pleural_Embolism,
            "covid":covid
        }
            # saving_data=user_cxr_disease_images.objects.create(user="haseeb",disease_name="Chest",detected_disease=name_confidence,uploaded_image=file)
            # saving_data.save()
            return JsonResponse({"Details":context},safe=False)
        except Exception as e:
            print ("error in exception",e)
            dicti = request.data.get('diseasedic')
            print ("dicti",dicti)
            print ("dicti",type(dicti))
            data= json.loads(dicti)
            print ("dicti",type(dicti))

            Viral_Bronchitis= data['Viral_Bronchitis']
            Bacterial_Pneumonia= data['Bacterial_Pneumonia']
            Asthma= data['Asthma']
            Chronic_Heart_Failure= data['Chronic_Heart_Failure']
            Chronic_Lung_Disease= data['Chronic_Lung_Disease']
            Lung_Cancer= data['Lung_Cancer']
            Pleural_Embolism= data['Pleural_Embolism']
            covid= data['covid']
            context ={

            "Viral_Bronchitis":Viral_Bronchitis,
            "Bacterial_Pneumonia":Bacterial_Pneumonia,
            "Asthma":Asthma,
            "Chronic_Heart_Failure":Chronic_Heart_Failure,
            "Chronic_Lung_Disease":Chronic_Lung_Disease,
            "Lung_Cancer":Lung_Cancer,
            "Pleural_Embolism":Pleural_Embolism,
            "covid":covid
        }
            return JsonResponse({"Details":context},safe=False)



class skin_Condition1(APIView):
    print ("in function")
    def post(self, request, format=None):
        try:
            try:

                file = request.data.get('fileup')
                print ("data",request.data.get('username'))
                check = User.objects.get(username=request.data.get('username'))
                email1=check.email
                print ("email",email1)
                print ("file",file)
            except Exception as e:
                print (e)
            staticPrefix = "static"
            filename = str(file)
            print ("filename",filename)

            filepath = 'images/skinimages/' + filename
            print ("filepath",filepath)
            with default_storage.open(filepath, 'wb+') as destination:
                for chunk in file.chunks():
                    # print ("chunk",chunk)
                    destination.write(chunk)
                    print ("desdestination",destination )

            # getting results
            results = model_skin('media/'+filepath)
            print ("results",results)
            # for croping

            _, result_dir = results.crop(save=True)
            print ("result_dir",result_dir)
            # converting detection result to json format
            data = results.pandas().xyxy[0].to_json(orient="records")
            print ("previous data",data)

            try :
                # normalizing result_dir
                tmp = finders.find(result_dir)
                print ("tmp",tmp)
            except Exception as e:
                print ("normalizing result_dir",e)

            searched_loc = finders.searched_locations
            print ("searched_loc",searched_loc)

            modified_res_loc = os.path.relpath(tmp, searched_loc[0])
            print ("modified_res_loc",modified_res_loc)

            result_dir = str(result_dir.as_posix())
            print ("result_dir",result_dir)


            data = json.loads(data)
            print ("here is the complete data",len(data))

            if len (data) == 0 :
                # user_diesease_update = top_disease_user_overall_with_user.objects.create(analysistype="Skin",disease1="No Disease",p1="0",email=email1,verified="Yes",userfrom="Mobile Application", last_date_of_analysis=datetime.datetime.now(),imagepath=filepath)
                # user_diesease_update.save()



                return JsonResponse({"Details":"No Disease Found"},safe=False)
            unique_fruits = {}
            for fruit in data:
                unique_fruits[fruit.get('name')] = []
                print ("unique_fruits",unique_fruits)


            for fruit in unique_fruits:
                file_list = os.listdir(result_dir+'/crops/'+fruit)
                unique_fruits[fruit] = file_list
                print ("file_list",file_list)


            name_confidence = []
            final_data = []
            # i  = 0
            for record in data:
                name_confidence.append({
                    "name": record.get('name'),
                    "confidence": record.get('confidence')
                })
                final_data.append({
                    "name": record.get('name'),
                    "confidence": record.get('confidence'),
                    "image_url": staticPrefix+'/' + modified_res_loc + '/crops/' + record.get('name') + '/' + unique_fruits[record.get('name')].pop(0)
                })

                break
            for record in name_confidence:
                # user_diesease_update = top_disease_user_overall_with_user.objects.create(analysistype="Skin",disease1=record['name'],p1=record['confidence'],email=email1,verified="Yes",userfrom="Mobile Application", last_date_of_analysis=datetime.datetime.now(),imagepath=filepath)
                # user_diesease_update.save()
                break
            print ("first type",type(name_confidence))
            print ("name_confidence",name_confidence)

            resultant_data = {
                "data": final_data,
                "actual_image_url": staticPrefix + '/'+modified_res_loc+'/'+filename
            }
            # saving_data=user_skin_disease_images.objects.create(user="haseeb",disease_name="Skin",detected_disease=name_confidence,uploaded_image=file)
            # saving_data.save()
            return JsonResponse({"Details":final_data},safe=False)
        except Exception as e:
            print ("error in exception",e)
            context={
                "Status":"400",
                "Error":"Upload File is incorrect"
            }
            return JsonResponse({"Details":context},safe=False)


class Food_Analysis1(APIView):
    print ("in function")
    def post(self, request, format=None):
        try:
            try:
                file = request.data.get('fileup')
                print ("file",file)
            except Exception as e:
                print (e)
            staticPrefix = "static"
            filename = str(file)
            print ("filename",filename)

            filepath = 'images/' + filename
            print ("filepath",filepath)
            with default_storage.open(filepath, 'wb+') as destination:
                for chunk in file.chunks():
                    # print ("chunk",chunk)
                    destination.write(chunk)
                    print ("desdestination",destination )

            # getting results
            results = model_food('media/'+filepath)
            print ("results",results)
            # for croping

            _, result_dir = results.crop(save=True)
            print ("result_dir",result_dir)
            # converting detection result to json format
            data = results.pandas().xyxy[0].to_json(orient="records")
            print ("previous data",data)

            try :
                # normalizing result_dir
                tmp = finders.find(result_dir)
                print ("tmp",tmp)
            except Exception as e:
                print ("normalizing result_dir",e)

            searched_loc = finders.searched_locations
            print ("searched_loc",searched_loc)

            modified_res_loc = os.path.relpath(tmp, searched_loc[0])
            print ("modified_res_loc",modified_res_loc)

            result_dir = str(result_dir.as_posix())
            print ("result_dir",result_dir)


            data = json.loads(data)
            print ("here is the complete data",len(data))
            if len (data) == 0 :

                return JsonResponse({"Details":"No Food Found"},safe=False)

            unique_fruits = {}
            for fruit in data:
                unique_fruits[fruit.get('name')] = []
                print ("unique_fruits",unique_fruits)


            for fruit in unique_fruits:
                file_list = os.listdir(result_dir+'/crops/'+fruit)
                unique_fruits[fruit] = file_list
                print ("file_list",file_list)


            name_confidence = []
            final_data = []
            # i  = 0
            for record in data:
                name_confidence.append({
                    "name": record.get('name'),
                    "confidence": record.get('confidence')
                })
                final_data.append({
                    "name": record.get('name'),
                    "confidence": record.get('confidence'),
                    "image_url": staticPrefix+'/' + modified_res_loc + '/crops/' + record.get('name') + '/' + unique_fruits[record.get('name')].pop(0)
                })
                break
            print ("first type",type(name_confidence))
            print ("name_confidence",name_confidence)

            resultant_data = {
                "data": final_data,
                "actual_image_url": staticPrefix + '/'+modified_res_loc+'/'+filename
            }
            # saving_data=user_food_disease_images.objects.create(user="haseeb",disease_name="Food",detected_disease=name_confidence,uploaded_image=file)
            # saving_data.save()
            return JsonResponse({"Details":final_data},safe=False)
        except Exception as e:
            print ("error in exception",e)
            context={
                "Status":"400",
                "Error":"Upload File is incorrect"
            }
            return JsonResponse({"Details":context},safe=False)


@csrf_exempt
def chest_pain1(request):

    global Cardiac_Ischemia
    global PE
    global Cardiac_Ischemia
    global Costochondritis
    global Pneumonia


    # if request.user.is_authenticated:
    #     user = request.user
    if request.method == 'GET':



        questions = chest_questions.objects.all()
        final_data1=[]
        for l in questions:
            options=[]
            all_option=chest_options_questions.objects.filter(question=l.id)
            for data in all_option:
                options.append({
                    "options_id":data.id,
                    "options_data":data.option1,
                })
            final_data1.append({
                        "question_data":l.Question,
                        "question_id":l.id,
                        "MultiValue":False,
                        "option":options,

                    })

        return JsonResponse({"Details":final_data1},safe=False)

    if request.method == 'POST':
        print('POST', request.POST)
        print('BODY', request.body)
        # print('JSON', json.dump(request.body))
        data =  json.loads(request.body)
        print ("data",data)
        print ("length of data",len(data))



        Cardiac_Ischemia=0
        Pleurisy=0
        Costochondritis=0
        PE=0
        Pneumonia=0

        for question_id in data:
            print ("key",question_id)
            print ("value",data[question_id])
            answer_id = data[question_id]



            if question_id == "1":
                for answer_id in answer_id:
                    if answer_id == "1":
                        Cardiac_Ischemia+=1
                        PE+=1
                        Pleurisy+=0.5
                        Costochondritis+=0.5
                        Pneumonia-=1

                    if answer_id == "2":
                        Cardiac_Ischemia+=0.25
                        PE-=0.5
                        Pleurisy+=0.5
                        Costochondritis+=0.5
                        Pneumonia+=1

            if question_id == "2":
                for answer_id in answer_id:

                    if answer_id == "3":
                        Cardiac_Ischemia-=1
                        PE-=1
                        Pleurisy+=0.5
                        Costochondritis+=1
                        Pneumonia+=0.5


            if question_id =="3" :
                for answer_id in answer_id:

                    if answer_id == "5":
                        Cardiac_Ischemia-=1
                        PE-=1
                        Pleurisy+=0.5
                        Costochondritis+=0.5
                        Pneumonia+=1

            if question_id =="4":
                for answer_id in answer_id:
                    if answer_id == "7":
                        Cardiac_Ischemia-=1
                        PE+=1
                        Pleurisy-=1
                        Costochondritis-=1
                        Pneumonia+=0.5

            if question_id == "5":
                for answer_id in answer_id:
                    if answer_id == "9":
                        Cardiac_Ischemia-=1
                        PE+=1
                        Pleurisy+=1
                        Costochondritis+=0.5
                        Pneumonia+=0.5

            if question_id =="6":
                for answer_id in answer_id:
                    if answer_id == "11":
                        Cardiac_Ischemia+=1
                        PE-=1
                        Pleurisy-=1
                        Costochondritis-=1
                        Pneumonia-=1

            if question_id=="7":
                for answer_id in answer_id:

                    if answer_id == "13":
                        Cardiac_Ischemia+=1
                        PE+=0.5
                        Pleurisy+=0.25
                        Costochondritis-=0.5
                        Pneumonia+=1


        context ={
            "Cardiac_Ischemia":Cardiac_Ischemia,
            "Pleurisy":Pleurisy,
            "Pneumonia":Pneumonia,
            "Costochondritis":Costochondritis,
            "Pleural_Embolism":PE,
        }
        print (context)

        x = sorted(((v,k) for k,v in context.items() if v > 0))
        print ("len of x",len(x))
        if len(x) == 0:
            return JsonResponse({"Details":"No Disease Found "},safe=False)

        return JsonResponse({"Details":context},safe=False)

