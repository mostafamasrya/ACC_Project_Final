from django.urls import path
from . import views
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('users-list/', views.usersList),
    # path('users-list/<str:username>', views.getUser),
    # path('users-delete/<str:username>', views.deleteUser),
    path('insertNotifications/', insertNotifications),
    # path('insertNotifications/<str:username>/<str:type>/', insertNotifications),
    path('deleteNotifications/<str:username>/<str:type>/', deleteNotifications),
    path('countNotifications/<str:username>/', countNotifications),
    path('insertServiceRequest/', insertServiceRequest),
    path('verify/<str:username>/', verify),
    path('addMedication/', addMedication),
    path('checkUserOnline/<str:username>', checkUserOnline),
    path('checkVetOnline/<str:username>', checkVetOnline),
    path('addMessage/', addMessage),
    path('getAllMessagesAssociated/<str:username>/', getAllMessagesAssociated),
    path('getAllMessages/<str:sender>/<str:receiver>', getAllMessages),
    path('logout/<str:username>', logout),
    path('logoutVet/<str:username>', logoutVet),
    path('resendEmail/<str:username>', resendEmail),
    path('checkVerified/<str:username>', checkVerified),
    path('loginVet/<str:username>/<str:password>', loginVet),
    path('loginUser/<str:username>/<str:password>', loginUser),
    path('listAnimals/<str:username>', listAnimals),
    path('insertAnimal/', insertAnimal),
    path('insertLocation/', insertLocation),
    path('insertUser/', insertuser),
    path('insertVet/', insertVet),
    path('insertRequest/', insertRequest),
    path('insertSurgry/', insertSurgry),
    path('listlocation/', listlocation),
    path('listservices/', listservices),
    path('locationDetails/<int:id>/', locationDetails),
    path('listusers/', listusers),
    path('listvets/', listVets),
    path('finduser/<str:username>/', finduser),
    path('findSurgery/<int:id>/', findSurgery),
    path('findvet/<str:username>/', findvet),
    path('findAnimals/<str:ownerusername>/', findAnimals),
    path('findRequest/<int:id>/', findRequest),
    path('updateRequestStatusUser/<int:id>/', updateRequestStatusUser),
    path('updateOperationStatusUser/<int:id>/', updateOperationStatusUser),
    path('updateSrviceStatusUser/<int:id>/', updateSrviceStatusUser),
    path('updateSrviceStatusOwner/<int:id>/', updateSrviceStatusOwner),
    path('updateRequestStatusVet/<int:id>/', updateRequestStatusVet),
    path('SurVetUpdates/<int:id>/', SurVetUpdates),
    path('updateOperationStatusVet/<int:id>/', updateOperationStatusVet),
    path('getMedication/<str:animalName>/', getMedication),
    path('getSurgery/<str:VetName>/', getSurgery),
    path('findSpecificAnimal/<str:animalName>/', findSpecificAnimal),
    path('getRequests/<str:VetUserName>/', getRequests),
    path('getRequestByUserAndAnimalAndVet/<str:user>/<str:animalName>/<str:vetname>/',
         getRequestByUserAndAnimalAndVet),
    path('getRequestByUsername/<str:user>/', getRequestByUsername),
    path('getServicesRequests/<str:locationOwner>/', getServicesRequests),
    path('getServicesResponses/<str:username>/', getServicesResponses),
    path('getSurgicalResponses/<str:owner>/', getSurgicalResponses),
    path('getSurgicalOperations/<str:owner>/', getSurgicalOperations),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
