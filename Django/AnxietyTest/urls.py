from django.contrib import admin
# from apiforallmodules import settings
from django.conf import settings
from django.conf.urls.static import static

from AnxietyTest import views
from django.urls import path


# from knox import views as knox_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('Test/',views.anxiety_test, name="anxiety_test"),
    path('sendotp_Anxiety/',views.sendotp_AnxietyTest, name="sendotp_AnxietyTest"),
    path('Anxiety_thankyou/',views.Anxiety_thanks, name="Anxiety_thanks"),
    path('Anxiety_contactus/',views.Anxiety_contactus, name="Anxiety_contactus"),
    path('home/',views.home_Anxiety, name="home_Anxiety"),



]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)