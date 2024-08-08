from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(UserMedicalImages)
admin.site.register(UserMedicalAnalays)
admin.site.register(ApplicationService)
admin.site.register(Section)
admin.site.register(SectionService)
admin.site.register(SectionClinic)
admin.site.register(SectionCenter)
admin.site.register(SectionHospital)
admin.site.register(SectionClinicBooking)
admin.site.register(SectionCenterBooking)
admin.site.register(SectionHospitalBooking)
admin.site.register(UserRecordsClinic)
admin.site.register(UserRecordsClinicImages)
admin.site.register(UserRecordsHospital)
admin.site.register(UserRecordsHospitalImages)
admin.site.register(UserRecordsCenter)
admin.site.register(UserRecordsCenterImages)
admin.site.register(UserDoctor)
admin.site.register(UserRecordsCenterMedicine)
admin.site.register(UserRecordsClinicMedicine)
admin.site.register(UserRecordsHospitalMedicine)


