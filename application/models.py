from django.db import models

class User(models.Model):
	name = models.CharField(max_length=100)
	national_number = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	image = models.ImageField(upload_to='users/',null=True)
	password = models.CharField(max_length=100)
	bdate=models.CharField(max_length=100)
	gender=models.CharField(max_length=10)
	weight=models.IntegerField()
	age = models.IntegerField()
	blood=models.CharField(max_length=10)
	qr=models.CharField(max_length=100,null=True)


class UserDoctor(models.Model):
	user = models.ForeignKey("User", on_delete=models.CASCADE)
	doctor = models.ForeignKey("SectionClinic", on_delete=models.CASCADE)
	
class UserMedicalImages(models.Model):
	image = models.ImageField(upload_to='UserMedicalImages/')
	user = models.ForeignKey("User", on_delete=models.CASCADE)

class UserMedicalAnalays(models.Model):
	type = models.CharField(max_length=100)
	normal=models.IntegerField()
	danger=models.IntegerField()
	result=models.IntegerField()
	# date=models.CharField(max_length=14,null=True)
	analays_date=models.CharField(max_length=100)
	src_name=models.CharField(max_length=100)
	src_phone=models.CharField(max_length=100)
	user = models.ForeignKey("User", on_delete=models.CASCADE)

class UserRecordsClinic(models.Model):
	date = models.CharField(max_length=100)
	hour=models.CharField(max_length=100)
	user = models.ForeignKey("User", on_delete=models.CASCADE)
	section_clinic=models.ForeignKey("SectionClinic", on_delete=models.CASCADE)
	review_date = models.CharField(max_length=100)
	description=models.CharField(max_length=200,null=True)

class UserRecordsClinicMedicine(models.Model):
	title = models.CharField(max_length=100)
	record = models.ForeignKey("UserRecordsClinic", on_delete=models.CASCADE)

class UserRecordsClinicImages(models.Model):
	image = models.ImageField(upload_to='UserRecordsClinic/')
	record = models.ForeignKey("UserRecordsClinic", on_delete=models.CASCADE)

class UserRecordsHospital(models.Model):
	date = models.CharField(max_length=100)
	hour=models.CharField(max_length=100)
	user = models.ForeignKey("User", on_delete=models.CASCADE)
	section_hospital=models.ForeignKey("SectionHospital", on_delete=models.CASCADE)
	review_date = models.CharField(max_length=100)
	description=models.CharField(max_length=200,null=True)

class UserRecordsHospitalMedicine(models.Model):
	title = models.CharField(max_length=100)
	record = models.ForeignKey("UserRecordsHospital", on_delete=models.CASCADE)

class UserRecordsHospitalImages(models.Model):
	image = models.ImageField(upload_to='UserRecordsHospital/')
	record = models.ForeignKey("UserRecordsHospital", on_delete=models.CASCADE)

class UserRecordsCenter(models.Model):
	date = models.CharField(max_length=100)
	hour=models.CharField(max_length=100)
	user = models.ForeignKey("User", on_delete=models.CASCADE)
	section_center=models.ForeignKey("SectionCenter", on_delete=models.CASCADE)
	review_date = models.CharField(max_length=100)
	description=models.CharField(max_length=200,null=True)

class UserRecordsCenterMedicine(models.Model):
	title = models.CharField(max_length=100)
	record = models.ForeignKey("UserRecordsCenter", on_delete=models.CASCADE)

class UserRecordsCenterImages(models.Model):
	image = models.ImageField(upload_to='UserRecordsCenter/')
	record = models.ForeignKey("UserRecordsCenter", on_delete=models.CASCADE)

class ApplicationService(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	logo_image = models.ImageField(upload_to='services_logos/')

	
class Section(models.Model):
	title = models.CharField(max_length=100)
	logo_image = models.ImageField(upload_to='sections_logos/')
	application_service=models.ForeignKey("ApplicationService", on_delete=models.CASCADE)

class SectionService(models.Model):
	text = models.CharField(max_length=100)
	section=models.ForeignKey("Section", on_delete=models.CASCADE)
	

class SectionClinic(models.Model):
	dr_name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	specialist = models.CharField(max_length=100)
	section=models.ForeignKey("Section", on_delete=models.CASCADE)
	phone=models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	qr=models.CharField(max_length=100,null=True)
	
class SectionCenter(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	section=models.ForeignKey("Section", on_delete=models.CASCADE)	
	phone=models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	qr=models.CharField(max_length=100,null=True)
	
class SectionHospital(models.Model):
	name = models.CharField(max_length=100)
	specialist = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	section=models.ForeignKey("Section", on_delete=models.CASCADE)	
	phone=models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	qr=models.CharField(max_length=100,null=True)
	
class SectionClinicBooking(models.Model):
	year=models.CharField(max_length=100)
	month=models.CharField(max_length=100)
	day=models.CharField(max_length=100)
	hour=models.CharField(max_length=100)
	section_clinic=models.ForeignKey("SectionClinic", on_delete=models.CASCADE)
	user=models.ForeignKey("User", on_delete=models.CASCADE)
	commited=models.IntegerField()
	
class SectionCenterBooking(models.Model):
	year=models.CharField(max_length=100)
	month=models.CharField(max_length=100)
	day=models.CharField(max_length=100)
	hour=models.CharField(max_length=100)
	section_center=models.ForeignKey("SectionCenter", on_delete=models.CASCADE)
	commited=models.IntegerField()
	user=models.ForeignKey("User", on_delete=models.CASCADE)

class SectionHospitalBooking(models.Model):
	year=models.CharField(max_length=100)
	month=models.CharField(max_length=100)
	day=models.CharField(max_length=100)
	hour=models.CharField(max_length=100)
	section_hospital=models.ForeignKey("SectionHospital", on_delete=models.CASCADE)
	commited=models.IntegerField()
	user=models.ForeignKey("User", on_delete=models.CASCADE)