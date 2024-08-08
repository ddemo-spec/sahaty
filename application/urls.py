from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path("userLogin/", views.userLogin, name="userLogin"),
	path("clinicLogin/", views.clinicLogin, name="clinicLogin"),
	path("centerLogin/", views.centerLogin, name="centerLogin"),
	path("hospitalLogin/", views.hospitalLogin, name="hospitalLogin"),
	path("userProfile/", views.userProfile, name="userProfile"),
	path("getsectionAdmin/", views.getsectionAdmin, name="getsectionAdmin"),
    
    
    

	
	path("getApplicationServices/", views.getApplicationServices, name="getApplicationServices"),
	path("getApplicationServiceSections/", views.getApplicationServiceSections, name="getApplicationServiceSections"),
	path("getSectionClinicsCentersHospitals/", views.getSectionClinicsCentersHospitals, name="getSectionClinicsCentersHospitals"),
	path("getSectionClinicBooking/", views.getSectionClinicBooking, name="getSectionClinicBooking"),
	path("addSectionClinicBooking/", views.addSectionClinicBooking, name="addSectionClinicBooking"),

	path("getUserBookings/", views.getUserBookings, name="getUserBookings"),
	path("cancelUserBookings/", views.cancelUserBookings, name="cancelUserBookings"),
	path("updateuserBooking/", views.updateuserBooking, name="updateuserBooking"),

	path("getUserAnalyses/", views.getUserAnalyses, name="getUserAnalyses"),
	path("getUserRecords/", views.getUserRecords, name="getUserRecords"),
	path("getTypeUsers/", views.getTypeUsers, name="getTypeUsers"),
	path("addNewAnalyses/", views.addNewAnalyses, name="addNewAnalyses"),
	path("addNewRecord/", views.addNewRecord, name="addNewRecord"),
	path("addNewUser/", views.addNewUser, name="addNewUser"),
	path("addNewSection/", views.addNewSection, name="addNewSection"),
	path("addNewService/", views.addNewService, name="addNewService"),
    
    


	path("getDoctorBookings/", views.getDoctorBookings, name="getDoctorBookings"),
	path("confirmBooking/", views.confirmBooking, name="confirmBooking"),
	path("cancellBooking/", views.cancellBooking, name="cancellBooking"),
	path("laterBookings/", views.laterBookings, name="laterBookings"),




	

	



    
	]
	