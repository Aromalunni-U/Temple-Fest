from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('festicon.urls')),
    path('account', include('account.urls')),


    path('reset_password',auth_views.PasswordResetView.as_view(),name="reset_password"),

    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),

    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),

    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




# admin.site.index_title="name"
admin.site.site_header="Festi Connect"
admin.site.site_title="Festicon"

