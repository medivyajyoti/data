from django.urls import path
from admin_form import views

urlpatterns = [
    path('',views.Home.as_view(), name = 'administrator_home'),
    path('profile/',views.AdminUserProfile.as_view(), name = 'admin_user_profile'),
    path('operator/',views.UserParam.as_view(), name = 'view_operator_profile'),
    path('operator/download',views.UserParamDownload.download_view, name = 'data_download'),
    path('user/',views.UsersProfile.as_view(), name = 'users_profile'),
]
