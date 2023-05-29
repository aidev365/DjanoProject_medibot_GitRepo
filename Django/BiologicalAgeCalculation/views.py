
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
# from app1.models import top_disease_user_overall_with_user, newemails,newnumbers, verifiednumbers,number_with_topdisease, top_disease_user_overall, disease_details, Cognition_analysis, Dementia_answer_details,Dementia_questions,Dementia_options_questions, food_detected_informations_user,  Food_detected_disease,Food_image, Skin_detected_disease,Skin_image, abdominal_answer_details,top_disease_user_abdominal, Fever_answer_details,top_disease_user_Fever,  top_disease_user_chest,top_disease_user_cough,chest_answer_details,chest_detected_disease, Chest_Xray_image, cough_answer_details,chest_questions,chest_options_questions,Nutrient_Information,user_detail, cough_options_questions,cough_questions,fever_options_questions,fever_questions,abdominal_options_questions,abdominal_questions,blood_questions,blood_options_questions
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



from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
# from knox.views import LoginView as KnoxLoginView


# Create your views here.

def home_biological_Age(request):
    return render (request,"biological_Age_home.html")

@csrf_exempt
def biological_Age_test(request):
    score=0
    if request.method=='POST':
        print("POST request accepeted and post data is", request.POST)
        # updated_data= dict(request.POST.lists())


        try:
            ba0=request.POST['bio_age0']
            print("Your ba0 is", ba0)
        except:
            ba0 =" "
            pass

        try:
            ba1=request.POST['bio_age1']
            print("Your ba1 is", ba1)
        except:
            ba1 =" "
            pass

        try:
            ba2=request.POST['bio_age2']
            print("Your ba2 is", ba2)
        except:
            ba2 =" "
            pass

        try:
            ba3=request.POST['bio_age3']
            print("Your are ba3", ba3)
        except:
            ba3 =" "
            pass

        try:
            ba4=request.POST['bio_age4']
            print("Your are ba4", ba4)

        except:
            ba4 =" "
            pass

        try:
            ba5=request.POST['bio_age5']
            print("Your are ba5", ba5)
        except:
            ba5 =" "
            pass

        try :
            ba5_wt=request.POST['bio_age5[field_3]']
            ba5_ht=request.POST['bio_age5[field_4]']

            print("Your BMI_wt is", ba5_wt)
            print("Your BMI_ht is", ba5_ht)

            weight= ba5_wt
            height= ba5_ht
            height_in_meter = round((int(height)/100),2)
            print ("height_in_meter",height_in_meter)
            BMI = round((int(weight) / (height_in_meter * height_in_meter)),2)
            print("Your calculated BMI is", BMI)
        except:
            BMI = 0
            pass

        try:
            ba6=request.POST['bio_age6']
            print("Your are ba6", ba6)
        except:
            ba6 =" "
            pass

        try:
            ba7=request.POST['bio_age7']
            print("Your are ba7", ba7)
        except:
            ba7 =" "
            pass

        try:
            ba8=request.POST['bio_age8']
            print("Your are ba8", ba8)
        except:
            ba8 =" "
            pass

        try:
            ba9=request.POST['bio_age9']
            print("Your are ba9", ba9)
        except:
            ba9 =" "
            pass

        try:
            ba10=request.POST['bio_age10']
            print("Your are ba10", ba10)
        except:
            ba10 =" "
            pass

        try:
            ba11=request.POST['bio_age11']
            print("Your are ba11", ba11)
        except:
            ba11 =" "
            pass

        try:
            ba12=request.POST['bio_age12']
            print("Your are ba12", ba12)
        except:
            ba12 =" "
            pass

        try:
            ba13=request.POST['bio_age13']
            print("Your are ba13", ba13)
        except:
            ba13 =" "
            pass



        score=0

        if ba1=="About one drink a day":
            score+=3
        if ba1=="Two or more drinks a day":
            score+=10

        print("score is", score)


        if ba2=="Get outside and go for a walk to unwind":
            score-=2
        if ba2=="Do some deep breathing and Tai Chi":
            score-=2
        if ba2=="Emotional eat, go buy your fav take away or snack":
            score+=5
        if ba2=="Do nothing just keep on going":
            score+=5
        if ba2=="Go meditation for 5-10 mins":
            score-=3
        print("score is", score)

        if ba3=="Every day":
            score+=12
        if ba3=="One or two times a week":
            score+=5
        if ba3=="Never":
            score-=5
        print("score is", score)

        if ba4=="High School":
            score+=3
        if ba4=="University":
            score-=4
        if ba4=="Higher University":
            score-=5
        print("score is", score)


        if BMI>=18 and BMI<=21 :
            score-=7
        if BMI>=22 and BMI<=24:
            score+=4
        if BMI>=25 and BMI<=30:
            score+=10
        if BMI>30:
            score+=20

        print("score is", score)


        if ba6=="I am an active member with charity, arts, other business owners, school activities and other group activities":
            score-=5
        if ba6=="I volunteer regularly or hold community events":
            score-=5
        if ba6=="I help out other community organisations once or twice a year":
            score-=1
        print("score is", score)


        if ba7=="Possibly 10 people":
            score-=2
        if ba7=="I have many friends and family, a large support network":
            score-=3
        if ba7=="I am very private person, do not want help":
            score+=2
        if ba7=="I would go through my crisis on my own":
            score+=2
        print("score is", score)


        if ba8=="Every day":
            score-=12
        if ba8=="Four or five times a week":
            score-=9
        if ba8=="One to three times per week":
            score-=4
        if ba8=="No, I don't like exercise":
            score+=5
        print("score is", score)


        if ba9=="I might sneak in a cig on weekends":
            score+=8
        if ba9=="I have quit and feel much better":
            score+=4
        if ba9=="I have quit and I still have problems with my lungs":
            score+=10
        if ba9=="I am a regular smoker":
            score+=20
        print("score is", score)


        if ba10=="I feel under the pump, maybe burger, fries & soda or dessert, don't like cooking rarely eat veggies":
            score+=3
        if ba10=="I love my veggies, give me a big plate of roasted veggies, legumes & quinoa":
            score-=5
        if ba10=="I like chicken with a side salad":
            score+=1
        if ba10=="I am a meat person":
            score+=2

        if ba11=="Yes, at least 2 or 3 cups":
            score+=3
        if ba11=="I love coffee":
            score+=3
        if ba11=="No I love my black or green tea":
            score-=1
        if ba11=="No prefer lemon juice in warm water":
            score-=3
        print("score is", score)


        if ba12=="About 6 to 7 hours nightly":
            score-=4
        if ba12=="About 8 to 10 hours nightly":
            score-=5
        if ba12=="About 4 to 5 hours nightly":
            score+=5
        if ba12=="I suffer broken sleep at least 2 to 3 times per night":
            score+=7
        print("score is", score)


        if ba13=="Yes, at least one person":
            score-=10
        print("score is", score)

        Users_age= int(ba0)
        print("user's age is",Users_age )


        Biological_age= score + Users_age


        print("Your Biological age is",Biological_age )


        score_data={
            "context1":Biological_age,
        }

        print("YOUR FINAL TOTAL SCORE IS", score)

        user_diesease_update = top_disease_user_overall.objects.create(analysistype="Biological age test", p1=score, last_date_of_analysis=datetime.datetime.now())
        user_diesease_update.save()
        request.session['P1_score']= score
        request.session['user_diesease_update']=user_diesease_update.id


        request.session['BIOLOGICAL_AGE']= Biological_age

        return render(request,"BiologicalAge_result_updated.html")



    return render(request,"BiologicalAgeTest.html")


def biological_Age_contactus(request):
    print ("In contact Us page")
    if request.method =="GET":
        print ("In contact Us page get request")
        print ("data",request.GET)
        # name = request.GET["name"]

        # phone = request.GET["phone"]
        email1 = request.GET["email"]
        print("email in contact us page is", email1)
        # message = request.GET["discription"]


        user_diesease_update = request.session.get('user_diesease_update')
        biological_age_cal = request.session.get('BIOLOGICAL_AGE')
        print("biological_age_cal in contact us page is", biological_age_cal)
        # print ("user_diesease_update",user_diesease_update)



        if len(email1) == 0:
            return JsonResponse({"status":"Error"})


        msz =  "Thank you for completing the analysis. Our AI algorithm has calculated your biological age and it is {} years. \n  The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses.\n Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms. \n Our most commonly visited symptoms are chest pain (https://www.apnamd.ai/_2_CVD_cal/ ) and depression (https://www.apnamd.ai/Depression/Test/). \n Kind Regards \n ApnaMD Team ".format(biological_age_cal)

        try :
            email = EmailMessage("Apna MD (AI Diagnosis)",msz,to=[email1])
            print("email in try method is", email)
            email.send()
            newemails_store =  newemails.objects.create(email=email1,create_Date= datetime.datetime.now())
            newemails_store.save()

            user_diesease_update = top_disease_user_overall_with_user.objects.create(analysistype="Biological age test", p1=request.session.get('P1_score'),email=email1,verified="No",userfrom="Web Application", last_date_of_analysis=datetime.datetime.now())
            user_diesease_update.save()


            return JsonResponse({"status":"sent"})
        except Exception as e:
            print ("Error in email exception",e)
            return JsonResponse({"status":"Error"})

    return redirect("HOME")


def biological_Age_thanks(request):
    if request.user.is_authenticated:
        usr = request.user
        email1 = usr.email
        user_diesease_update = top_disease_user_overall_with_user.objects.create(analysistype="Biological age test", p1=request.session.get('P1_score'),email=email1,verified="Yes",userfrom="Web Application", last_date_of_analysis=datetime.datetime.now())
        user_diesease_update.save()

        biological_age_cal = request.session.get('BIOLOGICAL_AGE')
        msz =  "Thank you for completing the analysis. Our AI algorithm has calculated your biological age and it is {} years. \n  The outcome has been obtained after a detailed comparison with multiple clinical trials. Please contact us if you wish to change any of your responses.\n Please visit our site https://www.apnamd.ai/ for a detailed analysis of medical symptoms. \n Our most commonly visited symptoms are chest pain (https://www.apnamd.ai/_2_CVD_cal/ ) and depression (https://www.apnamd.ai/Depression/Test/). \n Kind Regards \n ApnaMD Team ".format(biological_age_cal)

        email = EmailMessage("Apna MD (AI Diagnosis)",msz,to=[email1])
        email.send()
        newemails_store =  newemails.objects.create(email=email1,create_Date= datetime.datetime.now())
        newemails_store.save()
    return render(request,"afterverification_BiologicalAge.html")





