"""apiforallmodules URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from apiforallmodules import settings
from django.conf import settings
from django.conf.urls.static import static

from app1 import views
from django.urls import path, include
from app1.views import SurgeryData, Message2WhatAppView,chest_Condition,Food_Recognition,Skin_Condition,chest_Condition1,Food_Analysis1,skin_Condition1
from AnxietyTest import views as ax
# from knox import views as knox_views



urlpatterns = [
    

    path('doc/list/', views.docbelongtodetail,name="docbelongtodetail"),



    path('feedback/data/', views.feedbackdatafun,name="feedbackdatafun"),
    path('appointment/data/', views.appointmentdata,name="appointmentdata"),

    # path('Telegram/data/', views.Telegram_data,name="Telegram_data"),
    # path('Telegram/diagnosis/', views.Telegram_data_diagnosis,name="Telegram_data_diagnosis"),
    path('certificate/generate/', views.Certificategen,name="Certigen"),
    path('user/dash/board/',views.dashhome,name="dashhome" ),


    path('update-profile',views.updateprofile,name="updateprofile" ),
    path('sendotp/',views.sendotpnew,name="sendotpnew" ),
    path('user/profile/new/',views.userprofilenew,name="userprofilenew" ),
    path('login/',views.newlogin,name="login" ),



    path('report/generate/',views.reportgen,name="reportgen" ),
    path('get/pdf/url/',views.pdfurls,name="pdfurls" ),


    path('TH/Patients', views.TH_patients_test,name="TH_patients_test"),
    path('appointment/data/api/',views.Appointment_Data,name="Appointment_Data" ),

    path('surgery/images/api/',SurgeryData.as_view(),name="SurgeryData" ),

    
    path('surgery/data/', views.surgerydata,name="surgerydata"),
    path('NH/Patients', views.NH_patients_test,name="NH_patients_test"),
    path('combined/module/', views.combined_module_joint,name="combined_module_joint"),
    path('shoulder/combined/module/', views.shoulderelbow,name="shoulderelbow"),
    path('backpain/combined/module/', views.backpain,name="backpain"),
    path('whatsapp/data/', views.whatsappdata_fun,name="whatsappdata_fun"),

    path('Joint/Pain', views.Joint_pain_rasa,name="Joint_pain_rasa"),
    path('Back/Pain', views.Back_pain_rasa,name="Back_pain_rasa"),
    path('whatsapp', views.whatsapp,name="whatsapp"),

    path('db_to_csv', views.db_to_csv,name="db_to_csv"),
    path('message2whatapp', Message2WhatAppView.as_view(), name="message2whatapp"),

    path('bilogical/updated/rasa/', views.updated_biological_rasa,name="updated_biological_rasa"),
    path('feedback/updated/rasa/', views.feedback,name="feedback"),


    path('gastro/updated/rasa', views.updated_gastro_rasa,name="updated_gastro_rasa"),

    path('fever/updated/rasa', views.updated_fever_rasa,name="updated_fever_rasa"),

    path('depression/updated/rasa/', views.depression_rasa_updated,name="depression_rasa_updated"),
    path('anxiety/updated/rasa/', views.anxiety_rasa_updated,name="anxiety_rasa_updated"),
    

    path('rasa/cvd/', views.cvd_rasa_updated,name="cvd_rasa_updated"),
    path('rasa/diabets/', views.Diabetes_updated,name="Diabetes_updated"),
    path('rasa/chestpain/', views.chestpain_updated,name="chestpain_updated"),

    path('General/basic/details/', views.basic_details_id,name="basic_details_id"),
    path('updated/Respiratory/', views.updated_respiratory, name="updated_respiratory"),

    
    path('data/fever/', views.fever_data,name="fever_data"),


    path('Abdominal/updated/', views.abdominal_update,name="abdominal_update"),
    path('Respiratory/', views.respiratory, name="respiratory"),


    path('admin/', admin.site.urls),
    path('home/contact/us/', views.contactus_home,name="contactus_home"),
    path('home/contactus/', views.contactushome,name="contactushome"),

    path('feedback/Form/', views.feedbackForm ,name="feedbackForm"),
    path('General/rasachatbot/', views.basic_details_user,name="General_rasachatbot"),
   
    path('general/doc/detail/', views.generaldoc ,name="generaldoc"),
    path('special/doc/detail/', views.specialdoc ,name="specialdoc"),
    path('fever/rasa/', views.fever_rasa ,name="fever_rasa"),
    path('cough/rasa/', views.cough_rasa ,name="cough_rasa"),
    path('abdominal/rasa/', views.abdominal_rasa ,name="abdominal_rasa"),
    path('depression/rasa/', views.depression_rasa ,name="depression_rasa"),
    
    path('cough/rasachatbot/', views.rasachatbot,name="cough_rasachatbot"),
    path('new/form/', views.all_modules,name="newform"),
    path('CCF/form/', views.CCF_module,name="CCF_module"),
    path('Cobmined/form/', views.combined_module,name="combined_module"),
    path('Cobmined/Low/Mood/', views.combined_Low_mood_frontend,name="combined_Low_mood_frontend"),
    path('Cobmined/Low/Mood/Result', views.combined_low_mood_result,name="combined_low_mood_result"),

    path('Fever/Abdominal_1/', views.fever_abd_part1,name="fever_abdominal_frontend"),
    path('Fever/Abdominal_2/', views.fever_abd_part1_result,name="fever_abd_part1_result"),
    path('Fever/Abdominal_Final/', views.fever_abd_final_set,name="fever_abd_final_set"),

    path('Questions_1/', views.fever_abd_updated,name="fever_abd_updated"),
    path('Questions_1/Result1/', views.fever_abd_updated_result,name="fever_abd_updated_result"),
    path('Questions_1/Result2/', views.pnemonia_VB_qns_result,name="pnemonia_VB_qns_result"),
    path('Questions_2/', views.pnemonia_VB_qns,name="pnemonia_VB_qns"),
  
   
    path('surveysparrow/api/', views.api_survey,name="api_survey"),

    path('general/thankyou/page/',views.generalthankupage, name="generalthankupage"),


    path('Anxiety/', include('AnxietyTest.urls')),
    path('BiologicalAge/', include('BiologicalAgeCalculation.urls')),

     ########google and fb login###################

    path('GoogleLogin/', views.google_login,name="GoogleLogin"),
    path('accounts/profile/', ax.anxiety_test, name="redirectTo"),
    path('accounts/facebook/', ax.anxiety_test, name="fbLogin"),
    path('accounts/', include('allauth.urls')),




    path('cough/question/', views.cough_question,name="questionscough"),
    path('fever/question/', views.fever_question,name="questionsfever"),
    path('abdominal/question/', views.abdominal_question,name="questionsabddominal"),
    path('blood/question/', views.blood_question,name="blood_question"),

    path('chest/images/',chest_Condition.as_view(),name="chest_Condition" ),

    path ('food/analysis/',views.Food_analysis,name="Food_analysis"),
    path('food/images/',Food_Recognition.as_view(),name="Food_Recognition" ),


    path ('disease/skin/',views.skin_disease,name="skin_disease"),
    path('email/skin/', views.emailskin,name="emailskin"),
    path('skin/thank/you/', views.skinthankyou,name="skinthankyou"),
    path('skin/images/',Skin_Condition.as_view(),name="Skin_Condition" ),
    path('chest/images/',views.chest_Condition1,name="chest_Condition" ),
    path('resendotp/skinDiagnosis/otp/',views.resendotp_skin_diagnosis,name="skinDiagnosis_resendotp"),
    path('send/skinDiagnosis/otp/',views.sendotp_skin_diagnosis,name="skinDiagnosis_sendotp"),
    path('skin/optverification/',views.skin_otp, name="skin_optverification"),




    path('cough/answer/', views.cough_answer,name="cough_answer"),



    ########## Front-end Development #######
    path('', views.index,name="HOME"),
    path('signin/', views.signin,name="signin"),
    path('signup/', views.signup,name="signup"),
    path('disease/slection/', views.disease_selection,name="disease_selection"),

    path('logout/', views.logout,name="LOGOUT"),


    path('user/profile/details/', views.userprofile,name="userprofile"),
    path('disease/blood/detail', views.blood_description,name="blood_description"),
    path('disease/cxr/detail', views.cxr_description,name="cxr_description"),
    # path('disease/cognition/', views.Dementia,name="Dementia"),
    path('disease/selction/', views.disease_selectin1,name="DISEASE_SELECTION1"),


    path ('disease/chest/xray/',views.chest_xray,name="chest_xray"),
    path('questions/blood/report/cough/', views.blood_Report_cough,name="blood_Report_cough"),


    path('questions/blood/report/fever/', views.blood_Report_fever,name="blood_Report_fever"),
    path('questions/blood/report/abdominal/', views.blood_Report_abdominal,name="blood_Report_abdominal"),


    path('questions/chest/pain/', views.chest_pain,name="question_chest"),

    path('disease/cognition/', views.Dementia,name="Dementia"),

    path('Pregnancy/check/', views.Pregnancy,name="Pregnancy"),

    path('all/chest/xray/', views.previousdataforcxry,name="allchestxray"),
    path('all/blood/reports/', views.allbloodreport,name="allbloodreport"),

    path('choose/abdominal/blood/test', views.Choose_Abdominal_blood_test,name="Choose_Abdominal_blood_test"),
    path('Abdominal_blood/', views.Abdominal_blood,name="Abdominal_blood"),
    path('Abdominal_options/', views.Abdominal_options,name="Abdominal_options"),

    path('fever_options/', views.fever_options,name="fever_options"),
    path('Choose_fever_blood_test/', views.Choose_fever_blood_test,name="Choose_fever_blood_test"),
    path('fever_blood/', views.fever_blood,name="fever_blood"),

    path('cough_blood/', views.cough_blood,name="cough_blood"),
    path('cough_options/', views.cough_options,name="cough_options"),
    path('Choose_cough_blood_test/', views.Choose_cough_blood_test,name="Choose_cough_blood_test"),
    path('cough_chest_xray/', views.cough_chest_xray,name="cough_chest_xray"),
    path('cough_result/', views.cough_result,name="cough_result"),
    path('Choose_cough_BT_Xray/', views.Choose_cough_BT_Xray,name="Choose_cough_BT_Xray"),
    path('Choose_cxray_blood_test/', views.Choose_cxray_blood_test,name="Choose_cxray_blood_test"),



    path('check_user/',views.check_user,name="check_user"),
    path('contactus/',views.contactus,name="contactus"),
    path('pregnancy/email/',views.pregnancyemail,name="pregnancyemail"),
    path('emailme/',views.emailme,name="emailme"),
    path('terms/conditions/',views.termsconditions,name="termsconditions"),
    path('privacy/policy/',views.privacypolicy,name="privacypolicy"),

    path('cough/check/', views.cough_check,name="cough_check"),

    path('_2_Diabetes/check/', views.Diabetes,name="Diabetes"),
    path('diabates/contactus/',views.diabates_contactus,name="diabates_contactus"),

    path('otp/optverification/',views.optverification,name="optverification"),
    path('send/otp/',views.sendotp,name="sendotp"),
    path('resendotp/otp/',views.resendotp,name="resendotp"),
    path('email/diabetes/',views.diabetes_email,name="diabetes_email"),
    path('thanku/diabetes/',views.thanku_diabetes,name="thanku_diabetes"),

    path('resendotp/general/otp/',views.General_resendotp,name="General_resendotp"),
    path('send/general/otp/',views.General_sendotp,name="General_sendotp"),
    path('general/optverification/',views.general_optverification, name="general_optverification"),
    path('general/email/',views.general_email, name="general_email"),



    path('_2_Diabetes_complications/',views.Diabetes_complications,name="Diabetes_complications"),
    path('diabets/complication/thank/you/',views.afterverification_thankyou,name="afterverification_thankyou"),
    path('sendotp_diabetes_complications/',views.sendotp_diabetes_complications, name="sendotp_diabetes_complications"),
    path('resendotp_diabetes_complications/',views.resendotp_diabetes_complications, name="resendotp_diabetes_complications"),
    path('otp_verification_diabetes_complications/',views.otp_verification_diabetes_complications, name="otp_verification_diabetes_complications"),
    path('send/email/diabets/complications/',views.email_diabetes_complications, name="email_diabetes_complications"),

    ########### home form urls #########
    ########### home form urls #########

    path('_1_check/Diabetes/form/', views.DiabetesForm,name="DiabetesForm"),
    path('_1_check/DiabetesRisk/Complex/form/', views.DiabetesRiskform,name="DiabetesRiskform"),
    path('_1_check/cvdrisk/form/', views.cvdriskfrom,name="cvdriskfrom"),


    ####################################

    path('Depression/Test/',views.depression_test, name="depression_test"),
    path('resendotp_depression/',views.resendotp_depression, name="resendotp_depression"),
    path('sendotp_depression/',views.sendotp_depression, name="sendotp_depression"),
    path('depression_optverification/',views.depression_optverification, name="depression_optverification"),
    path('depression_thankyou/',views.depression_thanks, name="depression_thanks"),
    path('depression_contactus/',views.Depression_contactus, name="depression_contactus"),


    path('cvd/email/',views.cvd_email,name="cvd_email"),
    path('_2_CVD_cal/',views.CVD_cal,name="CVD_cal"),
    path('CVD_cal/thank/you/',views.cvdthankyoupage,name="cvdthankyoupage"),
    path('sendotp_cvd_risk/',views.sendotp_cvd_risk, name="sendotp_cvd_risk"),
    path('resendotp_cvd_risk/',views.resendotp_cvd_risk, name="resendotp_cvd_risk"),
    path('otp_verification_cvd_risk/',views.otp_verification_cvd_risk, name="otp_verification_cvd_risk"),


    ################ jotform_modules################

    path('abdominalPain', views.abdominal_pain, name="abdominalPain"),
    path('ChestPain', views.ChestPain, name="ChestPain"),
    # path('fever', views.fever, name="fever"),




    ################### Apis ################
    path('neut/data/',views.nutrent_Data,name="nutrent_Data"),

    path('cough/questions/', views.cough_question1,name="cough_question1"),
    path('blood/questions/cough/', views.blood_cough_question1,name="blood_cough_question1"),


    path('fever/questions/', views.fever_question1,name="fever_question1"),
    path('blood/questions/fever/', views.blood_fever_question1,name="blood_fever_question1"),

    path('abdominal/questions/', views.abdominal_question1,name="abdominal_question1"),
    path('blood/questions/abdominal/', views.blood_abdominal_question1,name="blood_abdominal_question1"),

    path('chestpain/questions/', views.chest_pain1,name="question_chest1"),
    path('a/details/', views.datastore,name="datastore"),

    # path('chest/images/api/',chest_Condition1.as_view(),name="chest_Condition1" ),
    path('food/images/api/',Food_Analysis1.as_view(),name="Food_Analysis1" ),
    path('skin/images/api/',skin_Condition1.as_view(),name="skin_Condition1" ),

    # ########## api auth #############
    # path('api/signup/', views.apisignup,name="apisignup"),
    # path('api/login/', LoginAPI.as_view(), name='login'),
    # path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)