from email.headerregistry import Address
from tkinter import CASCADE
from tokenize import Number
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model 



########### COUGH ############
class top_disease_user_cough(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    disease1= models.CharField(max_length=100,blank=True)
    p1 =  models.CharField(max_length=5,blank=True)
    disease2= models.CharField(max_length=100,blank=True)
    p2 =  models.CharField(max_length=5,blank=True)
    disease3= models.CharField(max_length=100,blank=True)
    p3 =  models.CharField(max_length=5,blank=True)
    disease4= models.CharField(max_length=100,blank=True)
    p4 =  models.CharField(max_length=5,blank=True)

    last_date_of_analysis = models.DateTimeField()

    def __str__(self):
        return str(self.user.username)


class Chest_Xray_image(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    last_date_of_analysis = models.DateTimeField()
    uploaded_image = models.ImageField(upload_to='images/')
    def __str__(self):
        return str(self.id)


class chest_detected_disease(models.Model):
    chestimageid = models.ForeignKey(Chest_Xray_image,on_delete=models.CASCADE)
    disease_name = models.CharField(max_length=50)
    confidence = models.CharField(max_length=50)
    last_date_of_analysis = models.DateTimeField()
    def __str__(self):
        return str(self.disease_name)

class cough_questions(models.Model):
    Question= models.CharField(max_length=1000)
    def __str__(self):
        return str(self.id)


class  cough_options_questions(models.Model):
    option1= models.CharField(max_length=100)
    question= models.ForeignKey(cough_questions,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

class cough_answer_details(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    Question_id =  models.IntegerField(blank=True)
    Answer_id =  models.IntegerField(blank=True)
    Diagnosis_name = models.CharField(max_length=100,blank=True)
    last_date_of_analysis = models.DateTimeField()
   
    def __str__(self):
        return str(self.user)
###################################


############ Chest pain #############


class chest_questions(models.Model):
    Question= models.CharField(max_length=1000)
    def __str__(self):
        return str(self.id)


class  chest_options_questions(models.Model):
    option1= models.CharField(max_length=100)
    question= models.ForeignKey(chest_questions,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)



class chest_answer_details(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    Question_id =  models.IntegerField(blank=True)
    Answer_id =  models.IntegerField(blank=True)
    Diagnosis_name = models.CharField(max_length=100,blank=True)
    last_date_of_analysis = models.DateTimeField()
   
    def __str__(self):
        return str(self.user)


class top_disease_user_chest(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    disease1= models.CharField(max_length=100,blank=True)
    p1 =  models.CharField(max_length=5,blank=True)
    disease2= models.CharField(max_length=100,blank=True)
    p2 =  models.CharField(max_length=5,blank=True)
    disease3= models.CharField(max_length=100,blank=True)
    p3 =  models.CharField(max_length=5,blank=True)
    disease4= models.CharField(max_length=100,blank=True)
    p4 =  models.CharField(max_length=5,blank=True)

    last_date_of_analysis = models.DateTimeField()

    def __str__(self):
        return str(self.user.username)
#######################################################


############## Fever #############

class fever_questions(models.Model):
    Question= models.CharField(max_length=1000)
    def __str__(self):
        return str(self.id)


class  fever_options_questions(models.Model):
    option1= models.CharField(max_length=100)
    question= models.ForeignKey(fever_questions,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)



class Fever_answer_details(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    Question_id =  models.IntegerField(blank=True)
    Answer_id =  models.IntegerField(blank=True)
    Diagnosis_name = models.CharField(max_length=100,blank=True)
    last_date_of_analysis = models.DateTimeField()
   
    def __str__(self):
        return str(self.user)


class top_disease_user_Fever(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    disease1= models.CharField(max_length=100,blank=True)
    p1 =  models.CharField(max_length=5,blank=True)
    disease2= models.CharField(max_length=100,blank=True)
    p2 =  models.CharField(max_length=5,blank=True)
    disease3= models.CharField(max_length=100,blank=True)
    p3 =  models.CharField(max_length=5,blank=True)
    disease4= models.CharField(max_length=100,blank=True)
    p4 =  models.CharField(max_length=5,blank=True)

    last_date_of_analysis = models.DateTimeField()

    def __str__(self):
        return str(self.user.username)
##########################################



############# Abdominal ################
class abdominal_questions(models.Model):
    Question= models.CharField(max_length=1000)
    def __str__(self):
        return str(self.id)


class  abdominal_options_questions(models.Model):
    option1= models.CharField(max_length=100)
    question= models.ForeignKey(abdominal_questions,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)


class abdominal_answer_details(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    Question_id =  models.IntegerField(blank=True)
    Answer_id =  models.IntegerField(blank=True)
    Diagnosis_name = models.CharField(max_length=100,blank=True)
    last_date_of_analysis = models.DateTimeField()
   
    def __str__(self):
        return str(self.user)


class top_disease_user_abdominal(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    disease1= models.CharField(max_length=100,blank=True)
    p1 =  models.CharField(max_length=5,blank=True)
    disease2= models.CharField(max_length=100,blank=True)
    p2 =  models.CharField(max_length=5,blank=True)
    disease3= models.CharField(max_length=100,blank=True)
    p3 =  models.CharField(max_length=5,blank=True)
    disease4= models.CharField(max_length=100,blank=True)
    p4 =  models.CharField(max_length=5,blank=True)

    last_date_of_analysis = models.DateTimeField()

    def __str__(self):
        return str(self.user.username)
####################################



############# Blood ############
class blood_questions(models.Model):
    Question= models.CharField(max_length=1000)
    def __str__(self):
        return str(self.id)


class  blood_options_questions(models.Model):
    option1= models.CharField(max_length=100)
    question= models.ForeignKey(blood_questions,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

##########################################


################## Skin #################


class Skin_image(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    last_date_of_analysis = models.DateTimeField()
    uploaded_image = models.ImageField(upload_to='images/')
    def __str__(self):
        return str(self.id)


class Skin_detected_disease(models.Model):
    skinimageid = models.ForeignKey(Skin_image,on_delete=models.CASCADE)
    disease_name = models.CharField(max_length=50)
    confidence = models.CharField(max_length=50)
    last_date_of_analysis = models.DateTimeField()
    def __str__(self):
        return str(self.disease_name)
#################################################

######### Food ###############
class Food_image(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    last_date_of_analysis = models.DateTimeField()
    uploaded_image = models.ImageField(upload_to='images/')
    def __str__(self):
        return str(self.id)


class Food_detected_disease(models.Model):
    foodimageid = models.ForeignKey(Food_image,on_delete=models.CASCADE)
    disease_name = models.CharField(max_length=50)
    confidence = models.CharField(max_length=50)
    last_date_of_analysis = models.DateTimeField()
    def __str__(self):
        return str(self.disease_name)

class food_detected_informations_user(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    foodimageid = models.ForeignKey(Food_image,on_delete=models.CASCADE)
    Total_Calorie= models.FloatField(null=True, blank=True)
    Processed_Food_Percentage= models.FloatField(null=True, blank=True)
    Ultra_Processed_Food_Percentage= models.FloatField(null=True, blank=True) 
    Unprocessed_Food_Percentage= models.FloatField(null=True, blank=True)
     
    Total_Carb_percentage= models.FloatField(null=True, blank=True)
    Total_Protein_percentage= models.FloatField(null=True, blank=True)
    Total_Fat_percentage= models.FloatField(null=True, blank=True)
    Swimming_Exercise_time_to_burn_calories= models.FloatField(null=True, blank=True)
    Jogging_Exercise_time_to_burn_calories= models.FloatField(null=True, blank=True)
    Cycling_Exercise_time_to_burn_calories= models.FloatField(null=True, blank=True)
    Walking_Exercise_time_to_burn_calories= models.FloatField(null=True, blank=True)

    last_date_of_analysis = models.DateTimeField()


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
        return str(self.id)

#######################################

############ Dementia ############

class Dementia_questions(models.Model):
    Question= models.CharField(max_length=1000)
    def __str__(self):
        return str(self.id)


class  Dementia_options_questions(models.Model):
    option1= models.CharField(max_length=100)
    question= models.ForeignKey(Dementia_questions,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.option1)

class Dementia_answer_details(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    Question_id =  models.IntegerField(blank=True)
    Answer_id =  models.CharField(max_length=50, blank=True)
    last_date_of_analysis = models.DateTimeField()
   
    def __str__(self):
        return str(self.user)

class Cognition_analysis(models.Model):
    user_name= models.ForeignKey(User, on_delete=models.CASCADE)
    Orientation_Score_out_of_12=models.IntegerField()
    Memory_Score_out_of_3 =models.IntegerField()
    Attention_and_recall_Score_out_of_5 =models.IntegerField()
    N_Score_out_of_2=models.IntegerField()
    Total_Score_out_of_22 =models.IntegerField()
    

    def __str__(self):
        return str(self.id)

#####################################
class user_detail(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    dob = models.DateField()
    sex =  models.CharField(max_length=15)
    heigh =  models.CharField(max_length=5)
    weigth =  models.CharField(max_length=15)
    activity = models.CharField(max_length=50)
    Diabetes = models.TextField(max_length=5)
    Hypertension = models.CharField(max_length=5)
    CurrentSmoker = models.CharField(max_length=5)
    PastSmoker= models.CharField(max_length=15)
    BMI = models.CharField(max_length=5)
    Age = models.CharField(max_length=100)


    def __str__(self):
        return str(self.user)

########### Common #########


class disease_details(models.Model):
    disease_name= models.CharField(max_length=100)
    disease_description= models.TextField(max_length=2000)
    def __str__(self):
        return str(self.disease_name)



class top_disease_user_overall(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    disease1= models.CharField(max_length=100,blank=True)
    p1 =  models.CharField(max_length=5,blank=True)
    disease2= models.CharField(max_length=100,blank=True)
    p2 =  models.CharField(max_length=5,blank=True)
    disease3= models.CharField(max_length=100,blank=True)
    p3 =  models.CharField(max_length=5,blank=True)
    disease4= models.CharField(max_length=100,blank=True)
    p4 =  models.CharField(max_length=5,blank=True)
    analysistype =models.CharField(max_length=100,blank=True)
    last_date_of_analysis = models.DateTimeField()

    def __str__(self):
        return str(self.id)

class number_with_topdisease(models.Model):
    phonenumber= models.CharField(max_length=100)
    topdisease= models.CharField(max_length=100)
    def __str__(self):
        return str(self.phonenumber)