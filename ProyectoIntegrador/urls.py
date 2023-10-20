from django.contrib import admin
from django.urls import path, include
from movie import views as movieViews

from django.conf.urls.static import static
from django.conf import settings
from movie import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movieViews.home, name='home'),
    path('about/', movieViews.about),
    path('news/', include('news.urls')),
    path('login/', views.login_view, name='login'),
    path('home/<str:username>/', views.home, name='home')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
