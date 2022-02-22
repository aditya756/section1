from django.urls import path
from . import views
urlpatterns = [
    path('',views.demo),
    
    
    #path('admin/', admin.site.urls),
]
