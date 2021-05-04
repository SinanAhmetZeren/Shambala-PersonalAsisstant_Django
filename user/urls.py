from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ProfileListView

app_name = "user"

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),   
    path('profile/', views.view_profile, name="profile"),   
    path('update_profile/<int:id>', views.update_profile, name="update_profile"),
    path('public_profile/<int:id>', views.public_profile, name="public_profile"),
    path('update_image/<int:id>', views.update_image, name="update_image"),
    path('friends/', views.friends_invites, name="friends"),
    #path('allprofiles/', views.allprofiles, name="allprofiles"),
    path("allprofiles/", ProfileListView.as_view(), name="allprofiles"),
    path('inviteprofiles/', views.inviteprofiles, name="inviteprofiles"),
    path("send-invite/", views.send_invitation, name="send-invite"),
    path("remove-friend/",views.remove_from_friends, name="remove-friend"),
    path("accept-invitation/",views.accept_invitation, name="accept-invitation"),
    path("reject-invitation/",views.reject_invitation, name="reject-invitation"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)