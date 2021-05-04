from django.contrib import admin
from django.urls import path,include
from measures import views
from todo import views1
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('user/', include("user.urls")),
    path('measures/',include("measures.urls")),
    path('todos/',include("todo.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)