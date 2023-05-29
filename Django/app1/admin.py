from django.contrib import admin
from app1.models import *
# Register your models here.





class doctorbelongto_data(admin.ModelAdmin):
    list_display=[ "docname","belongto" ]

admin.site.register(doctorbelongto,doctorbelongto_data)

class feedbackdata_data(admin.ModelAdmin):
    list_display=[ "docname","dateandtime" ]

admin.site.register(feedbackdata,feedbackdata_data)


class appointmentdata_data(admin.ModelAdmin):
    list_display=[ "user","dateandtime" ]

admin.site.register(appointmentdataNew,appointmentdata_data)

# class BMIDatadetail_data(admin.ModelAdmin):
#     list_display=[ "user" ]

# admin.site.register(BMIData,BMIDatadetail_data)

# class whatsapp_medical_detail_data(admin.ModelAdmin):
#     list_display=[ "user" ]

# admin.site.register(whatsapp_medical_detail,whatsapp_medical_detail_data)

# class personaldetail_data(admin.ModelAdmin):
#     list_display=[ "user" ,"email"]

# admin.site.register(personaldetail,personaldetail_data)

# class ID_Dec_details(admin.ModelAdmin):
#     list_display=[ "sender_id" ,"Email","dateandtime"]
# admin.site.register(ID_Dec,ID_Dec_details)

class modules_details_data(admin.ModelAdmin):
    list_display=[ "user","uniqueis" ,"Qn","Ans","module_name","dateandtime"]

admin.site.register(modules_details,modules_details_data)


# class Medibot_modules_details_data(admin.ModelAdmin):
#     list_display=[ "user","uniqueis" ,"Qn","Ans","module_name","dateandtime"]

# admin.site.register(Medibot_modules_details, Medibot_modules_details_data)




admin.site.register(Nutrient_Information)
admin.site.register(Disease_explaination)

# class feedbackdata(admin.ModelAdmin):
#     list_display=[ "senderid" ,"DiagnosticAccuracy","UserExperience","Likelihoodtorecommend"]
# admin.site.register(feedbackupdated,feedbackdata)

class disease_detail_with_id_dat(admin.ModelAdmin):
    list_display=[ "user" ,"module_name","dateandtime"]
admin.site.register(Diagnosis_Dec,disease_detail_with_id_dat)

# class Medibot_disease_detail_with_id_dat(admin.ModelAdmin):
#     list_display=[ "user" ,"module_name","dateandtime"]
# admin.site.register(Medibot_Diagnosis_Dec, Medibot_disease_detail_with_id_dat)

# class Diet_Image_details(admin.ModelAdmin):
#     list_display=["id", "dateandtime"]
    
# admin.site.register (Diet_Image,Diet_Image_details)



# class SurgeryDta_details(admin.ModelAdmin):
#     list_display=["id","user" ,"dateandtime"]
    
# admin.site.register (SurgeryDta,SurgeryDta_details)


# class Skin_Image_details(admin.ModelAdmin):
#     list_display=["id", "dateandtime"]
    
# admin.site.register (Skin_Image,Skin_Image_details)

class pdffile_details(admin.ModelAdmin):
    list_display=[ "id", "dateandtime","filedata","uniqueis"]
admin.site.register(pdffile,pdffile_details)

# class AppointmentData_details(admin.ModelAdmin):
#     list_display=["email","appointment","from_number", "dateandtime"]
    
# admin.site.register (AppointmentData,AppointmentData_details)

class whatsappdata_details(admin.ModelAdmin):
    list_display=["email","discussion_point","from_number", "dateandtime"]
    
admin.site.register (whatsappdata,whatsappdata_details)