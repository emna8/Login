from django.urls import path
from . import views
#from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
"""router = DefaultRouter()
router.register(r'users', views.User_list)"""


# The API URLs are now determined automatically by the router.
urlpatterns = [
     #path('', include(router.urls)),
     path('users/',views.User_list),
     path('users/<int:pk>',views.User_detail),
     path("go/",views.gg_form),
    
] 