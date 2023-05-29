from django.contrib import admin
# from apiforallmodules import settings
from django.conf import settings
from django.conf.urls.static import static

from BiologicalAgeCalculation import views
from django.urls import path, include


# from knox import views as knox_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home_biological_Age, name="home_biological_Age"),
    path('Test/',views.biological_Age_test, name="BiologicalAge_test"),
    path('Biological/Age/contactus/',views.biological_Age_contactus, name="biological_Age_contactus"),
    path('thankyou/',views.biological_Age_thanks, name="biological_Age_thanks"),

    
   



]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)