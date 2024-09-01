from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  
    path('accounts/', include('django.contrib.auth.urls')),  
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),  
    path('logout/', LogoutView.as_view(next_page='main'), name='logout'),  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)