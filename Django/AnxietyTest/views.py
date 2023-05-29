from django.shortcuts import render
from glob import glob
from multiprocessing import context
import re
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
# from app1.models import 
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
import ast
from django.template.loader import render_to_string

from twilio.rest import Client
import random



from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
# from knox.views import LoginView as KnoxLoginView


# Create your views here.

def home_Anxiety(request):
    return render (request,"anxiety_apnamdai_home.html")
    
@csrf_exempt
def anxiety_test(request):
    score=0
    if request.method=='POST':
        print("POST request accepeted and post data is", request.POST)

        try:
            print ("In try")
            print ("In try data",request.body)
            form_data_str = str(request.body)
            form_data_str = form_data_str[2:-1]
            print(form_data_str)
            form_dict = json.loads(form_data_str)

            score=0

            try:
                if form_dict["an_1"]=="Several days":
                    score+=1
                if form_dict["an_1"]=="More than half the days":
                    score+=2
                if form_dict["an_1"]=="Nearly every day":
                    score+=3

                print("score is", score)

            except :
                pass  

            try:
                if form_dict["an_2"]=="Several days":
                    score+=1
                if form_dict["an_2"]=="More than half the days":
                    score+=2
                if form_dict["an_2"]=="Nearly every day":
                    score+=3
                print("score is", score)

            except :
                pass

            try:
                if form_dict["an_3"]=="Several days":
                    score+=1
                if form_dict["an_3"]=="More than half the days":
                    score+=2
                if form_dict["an_3"]=="Nearly every day":
                    score+=3
                print("score is", score)

            except :
                pass

            try:
                if form_dict["an_4"]=="Several days":
                    score+=1
                if form_dict["an_4"]=="More than half the days":
                    score+=2
                if form_dict["an_4"]=="Nearly every day":
                    score+=3
                print("score is", score)

            except :
                pass

            try:
                if form_dict["an_5"]=="Several days":
                    score+=1
                if form_dict["an_5"]=="More than half the days":
                    score+=2
                if form_dict["an_5"]=="Nearly every day":
                    score+=3
                print("score is", score)

            except :
                pass

            try:
                if form_dict["an_6"]=="Several days":
                    score+=1
                if form_dict["an_6"]=="More than half the days":
                    score+=2
                if form_dict["an_6"]=="Nearly every day":
                    score+=3
                print("score is", score)

            except :
                pass

            try:
                if form_dict["an_7"]=="Several days":
                    score+=1
                if form_dict["an_7"]=="More than half the days":
                    score+=2
                if form_dict["an_7"]=="Nearly every day":
                    score+=3
                print("score is", score)
            except :
                pass


            score_data={
                "context1":score,
            }

            print("YOUR FINAL TOTAL SCORE IS", score)

            if score<5 and score>=0: 
                Risk_assesment={
                   "Risk_Assessment" : "Your overall risk assessment for anxiety is Normal"
                }
               

            if score>=5 and score<10:
                Risk_assesment={
                    "Risk_Assessment" : "Your overall risk assessment for anxiety is Mild"
                }

            if score>=10 and score<15:
                Risk_assesment={
                    "Risk_Assessment" : "Your overall risk assessment for anxiety is Moderate"
                }

            if score>=15:
                Risk_assesment={
                        "Risk_Assessment" : "Your overall risk assessment for anxiety is Moderately Severe"
                }

            return JsonResponse({"status":Risk_assesment})
        
        except Exception as e:
            print("Error Receiving Form Data", e)
          



@csrf_exempt
def sendotp_AnxietyTest(request):
    if request.method =="GET":

        print ("data",request.GET)
        otpnumber = request.GET["num"]
        request.session['otpnumber']=otpnumber

        # otpnumber=request.session.get('otpnumber')
        print("your otp number is",otpnumber)

        user_diesease_update = request.session.get('user_diesease_update')
        Anxiety_Diagnosis = request.session.get('Diagnosis')
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
                body=f'{Anxiety_Diagnosis}' )
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


    return render(request,"Anxiety_result_updated.html")


def Anxiety_thanks(request):
    if request.user.is_authenticated:
        usr = request.user
        email1 = usr.email
        # user_diesease_update = top_disease_user_overall_with_user.objects.create(analysistype="Anxiety test",disease1=request.session.get('Diagnosis'), p1=request.session.get('P1_score'),email=email1,verified="Yes",userfrom="Web Application", last_date_of_analysis=datetime.datetime.now())
        # user_diesease_update.save()

        Anxiety_Diagnosis = request.session.get('Diagnosis')
        msz =  "Hi There, Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined that your risk of anxiety disorder is {}. \n  The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses.\n Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms. \n Our most commonly visited symptoms are chest pain (https://www.apnamd.ai/ChestPain/ ) and depression (https://www.apnamd.ai/Depression/Test/). \n Kind Regards \n ApnaMD Team ".format(Anxiety_Diagnosis)

        email = EmailMessage("Apna MD (AI Diagnosis)",msz,to=[email1])
        email.send()
        # newemails_store =  newemails.objects.create(email=email1,create_Date= datetime.datetime.now())
        # newemails_store.save()
    return render(request,"afterverification_anxiety.html")


def Anxiety_contactus(request):
    print ("In contact Us page")
    if request.method =="GET":
        print ("In contact Us page get request")
        print ("data",request.GET)
        # name = request.GET["name"]

        # phone = request.GET["phone"]
        email1 = request.GET["email"]
        # message = request.GET["discription"]


        user_diesease_update = request.session.get('user_diesease_update')
        Anxiety_Diagnosis = request.session.get('Diagnosis')
        print ("user_diesease_update",user_diesease_update)



        if len(email1) == 0:
            return JsonResponse({"status":"Error"})


        msz =  "Hi There, Thank you for completing the analysis. Our AI algorithm has analyzed your answers and determined that your risk of anxiety disorder is {}. \n  The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses.\n Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms. \n Our most commonly visited symptoms are chest pain (https://www.apnamd.ai/ChestPain/ ) and depression (https://www.apnamd.ai/Depression/Test/). \n Kind Regards \n ApnaMD Team ".format(Anxiety_Diagnosis)
        try :
            email = EmailMessage("Apna MD (AI Diagnosis)",msz,to=[email1])
            email.send()
            # newemails_store =  newemails.objects.create(email=email1,create_Date= datetime.datetime.now())
            # newemails_store.save()
            # user_diesease_update = top_disease_user_overall_with_user.objects.create(analysistype="Anxiety test",disease1=request.session.get('Diagnosis'), p1=request.session.get('P1_score'),email=email1,verified="No",userfrom="Web Application", last_date_of_analysis=datetime.datetime.now())
            # user_diesease_update.save()


            return JsonResponse({"status":"sent"})
        except Exception as e:
            print ("Error in email exception",e)
            return JsonResponse({"status":"Error"})

    return redirect("HOME")



