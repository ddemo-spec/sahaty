import json
import base64
from .models import *
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.conf import settings
from django.core.files import File
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def userLogin(request):
	body_e=request.body.decode('utf-8')
	body=json.loads(body_e)
	passw=body['password']
	national_number=body['national_number']
	try:
		u=User.objects.get(national_number=national_number,password=passw)
		ujs=model_to_dict(u)
		del ujs['password']
		ujs['image']="http:/localhost:8000"+u.image.url
		try:
			ud=UserDoctor.objects.get(user=u)
			ujs['dr_name']=ud.doctor.dr_name
			ujs['dr_phone']=ud.doctor.phone
			ujs['specialist']=ud.doctor.specialist
		except:
			ujs['dr_name']=""
			ujs['dr_phone']=""
			ujs['dr_specialist']=""
		mimages=UserMedicalImages.objects.filter(user=u)
		l=[]
		for obj in mimages:
			l.append("http:/localhost:8000"+obj.image.url)
		ujs["medical_images"]=l
		ana=[]
		manalayses=UserMedicalAnalays.objects.filter(user=u)
		for obj in manalayses:
			dic={}
			dic["type"]=obj.type
			dic["normal"]=obj.normal
			dic["danger"]=obj.danger
			dic["result"]=obj.result
			dic["analays_date"]=obj.analays_date
			dic["dr_name"]=obj.src_name
			dic["dr_phone"]=obj.src_phone
			ana.append(dic)
		ujs["medical_analayses"]=ana	
		
		
		return JsonResponse({'response':'ok','data':ujs})
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})
		
@csrf_exempt
def clinicLogin(request):
	body_e=request.body.decode('utf-8')
	body=json.loads(body_e)
	passw=body['password']
	qr=body['qr']
	try:
		u=SectionClinic.objects.get(qr=qr,password=passw)
		ujs=model_to_dict(u)
		del ujs['password']
		return JsonResponse({'response':'ok','data':ujs})
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})
		
		
@csrf_exempt
def centerLogin(request):
	body_e=request.body.decode('utf-8')
	body=json.loads(body_e)
	passw=body['password']
	qr=body['qr']
	try:
		u=SectionCenter.objects.get(qr=qr,password=passw)
		ujs=model_to_dict(u)
		del ujs['password']
		return JsonResponse({'response':'ok','data':ujs})
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})
		
		
@csrf_exempt
def hospitalLogin(request):
	body_e=request.body.decode('utf-8')
	body=json.loads(body_e)
	passw=body['password']
	qr=body['qr']
	try:
		u=SectionHospital.objects.get(qr=qr,password=passw)
		ujs=model_to_dict(u)
		del ujs['password']
		return JsonResponse({'response':'ok','data':ujs})
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})
		
@csrf_exempt
def userProfile(request):
	body_e=request.body.decode('utf-8')
	body=json.loads(body_e)
	userId=body['user_id']
	
	try:
		u=User.objects.get(id=userId)
		ujs=model_to_dict(u)
		del ujs['password']
		ujs['image']="http:/localhost:8000"+u.image.url
		try:
			ud=UserDoctor.objects.get(user=u)
			ujs['dr_name']=ud.doctor.dr_name
			ujs['dr_phone']=ud.doctor.phone
			ujs['specialist']=ud.doctor.specialist
		except:
			ujs['dr_name']=""
			ujs['dr_phone']=""
			ujs['dr_specialist']=""
		mimages=UserMedicalImages.objects.filter(user=u)
		l=[]
		for obj in mimages:
			l.append("http:/localhost:8000"+obj.image.url)
		ujs["medical_images"]=l
		ana=[]
		manalayses=UserMedicalAnalays.objects.filter(user=u)
		for obj in manalayses:
			dic={}
			dic["type"]=obj.type
			dic["normal"]=obj.normal
			dic["danger"]=obj.danger
			dic["result"]=obj.result
			dic["analays_date"]=obj.analays_date
			dic["dr_name"]=obj.src_name
			dic["dr_phone"]=obj.src_phone
			ana.append(dic)
		ujs["medical_analayses"]=ana	
		
		
		return JsonResponse({'response':'ok','data':ujs})
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})
@csrf_exempt		
def getApplicationServices(request):
	try:
		objs=ApplicationService.objects.all()
		data=[]
		for e in objs:
			d={}
			d["id"]=e.id
			d["title"]=e.title
			d["description"]=e.description
			d["logo_image"]="http://localhost:8000"+e.logo_image.url
			data.append(d)
		return JsonResponse({'response':'ok','data':list(data)})
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})	

@csrf_exempt		
def getApplicationServiceSections(request):
	try:
		body_e=request.body.decode('utf-8')
		body=json.loads(body_e)
	
		application_service_id=body['application_service_id']
		objs=Section.objects.filter(application_service=ApplicationService.objects.get(id=application_service_id))
				
		
		data=[]
		for e in objs:
			d={}
			d["id"]=e.id
			d["title"]=e.title
			d["logo_image"]="http://localhost:8000"+e.logo_image.url
			data.append(d)
		return JsonResponse({'response':'ok','data':data})
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})

@csrf_exempt		
def getsectionAdmin(request):
	try:
		# body_e=request.body.decode('utf-8')
		# body=json.loads(body_e)
	
		
		objs=Section.objects.all()
				
		
		data=[]
		for e in objs:
			d={}
			d["id"]=e.id
			d["title"]=e.title
			d["logo_image"]="http://localhost:8000"+e.logo_image.url
			data.append(d)
		return JsonResponse({'response':'ok','data':data})
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})	

@csrf_exempt		
def getSectionClinicsCentersHospitals(request):
	try:
		body_e=request.body.decode('utf-8')
		body=json.loads(body_e)		
		section_id=body['section_id']
		sec=Section.objects.get(id=section_id)
		services=SectionService.objects.filter(section=sec)
		clinics=SectionClinic.objects.filter(section=sec)
		centers=SectionCenter.objects.filter(section=sec)
		hospitals=SectionHospital.objects.filter(section=sec)
		data={'response':'ok','data':{"services":[],"clinics":[],"centers":[],"hospitals":[]}}
		lista=[]
		for e in services:
			lista.append(e.text)
		data['data']["services"]=lista
		lista=[]
		for e in clinics:
			d={}
			d["id"]=e.id
			d["name"]=e.dr_name
			d["location"]=e.location
			d["specialist"]=e.specialist
			d["phone"]=e.phone
			d["qr"]=e.qr
			d['type']="clinics"
			lista.append(d)	
		data['data']["clinics"]=lista
		lista=[]
		for e in centers:
			d={}
			d["id"]=e.id
			d["specialist"]=e.description
			d["name"]=e.name
			d["location"]=e.location
			d["phone"]=e.phone
			d["qr"]=e.qr
			d['type']="centers"
			lista.append(d)	
		data['data']["centers"]=lista
		lista=[]
		for e in hospitals:
			d={}
			d["id"]=e.id
			d["name"]=e.name
			d["specialist"]=e.location
			d["location"]=e.location
			d["phone"]=e.phone
			d["qr"]=e.qr
			d['type']="hospitals"
			lista.append(d)	
		data['data']["hospitals"]=lista
		return JsonResponse(data)
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})	




@csrf_exempt		
def getSectionClinicBooking(request):
	try:
		body_e=request.body.decode('utf-8')
		body=json.loads(body_e)		
		year=body['year']
		month=body['month']
		day=body['day']
		typ=body['type']
		id=body['id']
		hours=list(range(9,22))
		if typ=="clinics":
			bookings=SectionClinicBooking.objects.filter(section_clinic=SectionClinic.objects.get(id=id),year=year,day=day,month=month)
		if typ=="hospitals":
			bookings=SectionHospitalBooking.objects.filter(section_hospital=SectionHospital.objects.get(id=id),year=year,day=day,month=month)
		if typ=="centers":
			bookings=SectionCenterBooking.objects.filter(section_center=SectionCenter.objects.get(id=id),year=year,day=day,month=month)
		for obj in bookings:
			hours.remove(int(obj.hour))
		print(hours)
		# if day==22:
		# 	hours=[1,2,10,12,14]
		# else:
		# 	hours=[1,2,10,12,14,15]
		return JsonResponse({'response':'ok','data':hours}) 
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})	
	

@csrf_exempt		
def addSectionClinicBooking(request):
	try:
		body_e=request.body.decode('utf-8')
		body=json.loads(body_e)		
		year=body['year']
		month=body['month']
		day=body['day']
		hour=body['hour']
		typ=body['type']
		user_id=body['user_id']
		type_id=body['type_id']
		if typ=="clinics":
			SectionClinicBooking(hour=hour,section_clinic=SectionClinic.objects.get(id=type_id),year=year,day=day,month=month,user=User.objects.get(id=user_id),commited=0).save()
		if typ=="hospitals":
			SectionHospitalBooking(hour=hour,section_hospital=SectionHospital.objects.get(id=type_id),year=year,day=day,month=month,user=User.objects.get(id=user_id),commited=0).save()
		if typ=="centers":
			SectionCenterBooking(hour=hour,section_center=SectionCenter.objects.get(id=type_id),year=year,day=day,month=month,user=User.objects.get(id=user_id),commited=0).save()
		return JsonResponse({'response':'ok'})	
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})	

@csrf_exempt		
def getUserBookings(request):
	try:
		body_e=request.body.decode('utf-8')
		body=json.loads(body_e)		
		user_id=body['user_id']

		clinics=SectionClinicBooking.objects.filter(user=User.objects.get(id=user_id))
		centers=SectionCenterBooking.objects.filter(user=User.objects.get(id=user_id))
		hospitals=SectionHospitalBooking.objects.filter(user=User.objects.get(id=user_id))
		data={'response':'ok','data':[]}
		for e in clinics:
			d={}
			d["booking_id"]=e.id
			d["commited"]=e.commited
			d["section_name"]=e.section_clinic.dr_name
			d["section_location"]=e.section_clinic.location
			d['typeId']=e.section_clinic.id
			d["year"]=e.year
			d["month"]=e.month
			d["day"]=e.day
			d["hour"]=e.hour
			d["type"]="clinics"
			data['data'].append(d)
		for e in centers:
			d={}
			d["booking_id"]=e.id
			d["commited"]=e.commited
			d["section_name"]=e.section_center.name
			d["section_location"]=e.section_center.location
			d["year"]=e.year
			d['typeId']=e.section_center.id
			d["month"]=e.month
			d["day"]=e.day
			d["hour"]=e.hour
			d["type"]="centers"
			data['data'].append(d)
		for e in hospitals:
			d={}
			d["booking_id"]=e.id
			d["commited"]=e.commited
			d["section_name"]=e.section_hospital.name
			d["section_location"]=e.section_hospital.location
			d["year"]=e.year
			d["month"]=e.month
			d['typeId']=e.section_hospital.id
			d["day"]=e.day
			d["hour"]=e.hour
			d["type"]="hospitals"
			data['data'].append(d)			
		return JsonResponse(data)
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})	

@csrf_exempt		
def cancelUserBookings(request):
	try:
		body_e=request.body.decode('utf-8')
		body=json.loads(body_e)		
		booking_id=body['booking_id']
		typ=body['type']
		if typ=="clinics":
			SectionClinicBooking(id=booking_id).delete()
		if typ=="hospitals":
			SectionHospitalBooking(id=booking_id).delete()
		if typ=="centers":
			SectionCenterBooking(id=booking_id).delete()
		return JsonResponse({'response':'ok'})
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})

@csrf_exempt		
def updateuserBooking(request):
	try:
		body_e=request.body.decode('utf-8')
		body=json.loads(body_e)		
		year=body['year']
		month=body['month']
		day=body['day']
		hour=body['hour']
		typ=body['type']
		# user_id=body['user_id']
		# type_id=body['type_id']
		booking_id=body['booking_id']
		if typ=="clinics":
			updatebooking=SectionClinicBooking.objects.get(id=booking_id)
			updatebooking.year=year
			updatebooking.hour=hour
			updatebooking.month=month
			updatebooking.day=day
			
			updatebooking.save()
		if typ=="hospitals":
			
			updatebooking=SectionHospitalBooking.objects.get(id=booking_id)
			updatebooking.year=year
			updatebooking.hour=hour
			updatebooking.month=month
			updatebooking.day=day
			
			updatebooking.save()
		if typ=="centers":
			updatebooking=SectionCenterBooking.objects.get(id=booking_id)
			updatebooking.year=year
			updatebooking.hour=hour
			updatebooking.month=month
			updatebooking.day=day
			updatebooking.save()
		return JsonResponse({'response':'ok'})	
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})	


@csrf_exempt
def getUserAnalyses(request):
	body_e=request.body.decode('utf-8')
	body=json.loads(body_e)
	user_id=body['user_id']
	try:
		u=User.objects.get(id=user_id)
		ana=[]
		manalayses=UserMedicalAnalays.objects.filter(user=u)
		for obj in manalayses:
			dic={}
			dic["analysis_id"]=obj.id
			dic["type"]=obj.type
			dic["normal"]=obj.normal
			dic["danger"]=obj.danger
			dic["result"]=obj.result
			dic["analays_date"]=obj.analays_date
			dic["dr_name"]=obj.src_name
			dic["dr_phone"]=obj.src_phone
			ana.append(dic)		
		
		return JsonResponse({'response':'ok','data':ana})
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})
	
@csrf_exempt
def getUserRecords(request):
	try:
		body_e=request.body.decode('utf-8')
		body=json.loads(body_e)		
		user_id=body['user_id']

		clinics=UserRecordsClinic.objects.filter(user=User.objects.get(id=user_id))
		centers=UserRecordsCenter.objects.filter(user=User.objects.get(id=user_id))
		hospitals=UserRecordsHospital.objects.filter(user=User.objects.get(id=user_id))
		data={'response':'ok','data':[]}
		for e in clinics:
			d={}
			d["date"]=e.date
			d["hour"]=e.hour
			d["section_name"]=e.section_clinic.dr_name
			d["section_specialist"]=e.section_clinic.location
			d["dr_name"]=e.section_clinic.dr_name
			d["review_date"]=e.review_date
			d['description']=e.description
			cl_images=UserRecordsClinicImages.objects.filter(record=e)
			lista=[]
			for im in cl_images:
				lista.append("http://localhost:8000"+im.image.url)
			d["images"]=lista
			cl_medicin=UserRecordsClinicMedicine.objects.filter(record=e)
			listam=[]
			for im in cl_medicin:
				listam.append(im.title)
			d["mediciens"]=listam
			data['data'].append(d)
		for e in centers:
			d={}
			d["date"]=e.date
			d["hour"]=e.hour
			d["section_name"]=e.section_center.name
			d["section_specialist"]="لايوجد"
			d["dr_name"]="لايوجد"
			d["review_date"]=e.review_date
			d['description']=e.description
			cl_images=UserRecordsCenterImages.objects.filter(record=e)
			lista=[]
			for im in cl_images:
				lista.append("http://localhost:8000"+im)
			d["images"]=lista	
			cl_medicin=UserRecordsCenterMedicine.objects.filter(record=e)
			listam=[]
			for im in cl_medicin:
				listam.append(im.title)
			d["mediciens"]=listam		
			data['data'].append(d)
		
		
		
		for e in hospitals:
			d={}
			d["date"]=e.date
			d["hour"]=e.hour
			d["section_name"]=e.section_hospital.name
			d["section_specialist"]=e.section_hospital.specialist 
			d["dr_name"]="لايوجد"
			d["review_date"]=e.review_date
			d['description']=e.description
			cl_images=UserRecordsHospitalImages.objects.filter(record=e)
			lista=[]
			for im in cl_images:
				lista.append("http://localhost:8000"+im.image.url)
			d["images"]=lista	
			cl_medicin=UserRecordsHospitalMedicine.objects.filter(record=e)
			listam=[]
			for im in cl_medicin:
				listam.append(im.title)
			d["mediciens"]=listam			
			data['data'].append(d)			
		
		
		
		return JsonResponse(data)
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})	

#######################################
@csrf_exempt		
def addNewSection(request):
	try:
		body_e=request.body.decode('utf-8')
		body=json.loads(body_e)		
		s=Section()
		typ=body['type']
		type_id=body['type_id']
		is_new=body['is_new']

		if is_new == "yes":
			title=body['title']
			logo_image=body['logo_image']
			logo_image_data=  ContentFile(base64.b64decode(logo_image), name='service.jpg')
			application_service_id=body['application_service_id']
			s=Section(title=title,logo_image=logo_image_data,application_service_id=application_service_id)
			s.save()
		else:
			section_id=body['section_id']
			s=Section.objects.get(id=section_id)
		
		if typ=="clinics":
			sc=SectionClinic.objects.get(id=type_id)
			sc.section=s
			sc.save()
		if typ=="hospitals":
			sc=SectionHospital.objects.get(id=type_id)
			sc.section=s
			sc.save()		
		if typ=="centers":
			sc=SectionCenter.objects.get(id=type_id)
			sc.section=s
			sc.save()		
		return JsonResponse({'response':'ok'})	
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})	
	


@csrf_exempt		
def addNewService(request):
	try:
		body_e=request.body.decode('utf-8')
		body=json.loads(body_e)		
		title=body['title']
		description=body['description']
		logo_image=body['logo_image']
		logo_image_data=  ContentFile(base64.b64decode(logo_image), name='service.jpg')
		ApplicationService(logo_image=logo_image_data,title=title,description=description).save()
		return JsonResponse({'response':'ok'})	
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})	
	
@csrf_exempt		
def getTypeUsers(request):
	try:
		body_e=request.body.decode('utf-8')
		body=json.loads(body_e)		
		typ=body['type']
		type_id=body['type_id']
		data={'response':'ok','data':[]}
		if typ=="clinics":
			dataa=UserRecordsClinic.objects.filter(section_clinic=SectionClinic.objects.get(id=type_id))
			
			for user in dataa:
				# print(User.objects.get(id=1))
				usersp=SectionClinic.objects.get(id=user. section_clinic_id)
				ud=UserDoctor.objects.get(user=usersp.id)
				
				d={}
				d['id']=user.id
				d['date']=user.date
				d['hour']=user.hour
				d['section_clinic_id']=usersp.specialist
				d['review_date']=user.review_date
 
    
           
				userdata=User.objects.get(id=user.user.id)
				us=model_to_dict(userdata)
				us['dr_name']=ud.doctor.dr_name
				us['dr_phone']=ud.doctor.phone
				us['specialist']=ud.doctor.specialist
				us['image']=""
				del us['password']
				d['user']=us
				d["medical_images"]=[""]
				d['medical_analayses']=[]	
		
				data['data'].append(d)
			    
				
				
		if typ=="hospitals":
			dataa=UserRecordsHospital.objects.filter(section_hospital=SectionHospital.objects.get(id=type_id))
			for user in dataa:
				# print(User.objects.get(id=1))
				usersp=SectionHospital.objects.get(id=user. section_hospital.id)
				

				d={}
				d['id']=user.id
				d['date']=user.date
				d['hour']=user.hour
				d['section_clinic_id']=usersp. specialist
				d['review_date']=user.review_date
 
    
           
				userdata=User.objects.get(id=user.user.id)
				us=model_to_dict(userdata)
				us['image']=""
				us['dr_name']="لا يوجد"
				us['dr_phone']="لايوجد"
				us['specialist']=usersp. specialist
				
				us["medical_images"]=[]
				us['medical_analayses']=[]
				d['user']=us	
				data['data'].append(d)
		if typ=="centers":
			dataa=UserRecordsCenter.objects.filter(section_center=SectionCenter.objects.get(id=type_id))
			for user in dataa:
				# print(User.objects.get(id=1))
				usersp=SectionCenter.objects.get(id=user. section_center.id)
				d={}

				d['id']=user.id
				d['date']=user.date
				d['hour']=user.hour
				d['section_clinic_id']=usersp.name
				d['review_date']=user.review_date
 
    
           
				userdata=User.objects.get(id=user.user.id)
				us=model_to_dict(userdata)
				us['dr_name']="لا يوجد"
				us['dr_phone']="لايوجد"
				us['specialist']=usersp. name
				
				us['image']=""
				d['user']=us
				us["medical_images"]=[]
				us['medical_analayses']=[]	
				data['data'].append(d)
		return JsonResponse(data)	
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})	
	
@csrf_exempt		
def addNewAnalyses(request):
	try:
		body_e=request.body.decode('utf-8')
		body=json.loads(body_e)		
		type=body['type']
		normal=body['normal']
		danger=body['danger']
		result=body['result']
		src_phone=body['dr_phone']
		src_name=body['dr_name']
		user=body['user_id']
		date=body['analysis_date']

		UserMedicalAnalays(analays_date=date,type=type,normal=normal,danger=danger,result=result,src_phone=src_phone,src_name=src_name,user=User.objects.get(id=user)).save()
		return JsonResponse({'response':'ok'})	
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})	


@csrf_exempt		
def addNewRecord(request):
	try:
		body_e=request.body.decode('utf-8')
		body=json.loads(body_e)		
		type=body['type']
		
		date=body['date']
		hour=body['hour']
		user = body['user_id']
		section_clinic=body['type_id']
		review_date = body['review_date']
		description=body['description']
		imagesrecorde=body['images']
		medicinrecorde=body['mediciens']
		
		if type=="clinics":
			UserRecordsClinic(description=description,date=date,user=User.objects.get(id=user),section_clinic=SectionClinic.objects.get(id=section_clinic),hour=hour,review_date=review_date).save()
			imagesdata=UserRecordsClinic.objects.filter(user=user,section_clinic=section_clinic).last()
			


			print(imagesdata.id)
			for images in imagesrecorde:
				image_data=  ContentFile(base64.b64decode(images), name='record.jpg')
				UserRecordsClinicImages(record=UserRecordsClinic.objects.get(id=imagesdata.id),image=image_data).save()
			for medicin in medicinrecorde:
				UserRecordsClinicMedicine(record=UserRecordsClinic.objects.get(id=imagesdata.id),title=medicin).save()
		if type=="hospitals":
			UserRecordsHospital(date=date,user=User.objects.get(id=user),section_hospital=SectionHospital.objects.get(id=section_clinic),hour=hour,review_date=review_date).save()
			imagesdata=UserRecordsHospital.objects.filter(user=user,section_hospital=section_clinic).last()

			print(imagesdata.id)
			for images in imagesrecorde:
				image_data=  ContentFile(base64.b64decode(images), name='record.jpg')
				UserRecordsHospitalImages(record=UserRecordsHospital.objects.get(id=imagesdata.id),image=image_data).save()
			for medicin in medicinrecorde:
				UserRecordsHospitalMedicine(record=UserRecordsHospital.objects.get(id=imagesdata.id),title=medicin).save()	
		if type=="centers":
			UserRecordsCenter(date=date,user=User.objects.get(id=user),section_center=SectionCenter.objects.get(id=section_clinic),hour=hour,review_date=review_date).save()
			imagesdata=UserRecordsCenter.objects.filter(user=user,section_center=section_clinic).last()
			for medicin in medicinrecorde:
				UserRecordsCenterMedicine(record=UserRecordsCenter.objects.get(id=imagesdata.id),title=medicin).save()
			print(imagesdata.id)
			for images in imagesrecorde:
				image_data=  ContentFile(base64.b64decode(images), name='record.jpg')
				UserRecordsCenterImages(record=UserRecordsCenter.objects.get(id=imagesdata.id),image=image_data).save()
		return JsonResponse({'response':'ok'})	
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})	


@csrf_exempt		
def addNewUser(request):
	try:
		body_e=request.body.decode('utf-8')
		body=json.loads(body_e)		

		name =body['name']
		national_number =body['national_number']
		phone = body['phone']
		image = body['image']
		password =body['password']
		bdate=body['bdate']
		gender=body['gender']
		weight=body['weight']
		age = body['age']
		blood=body['blood']
		print(image)
		qr=body['qr']
		if image==None:
			User(name =name,national_number =national_number,phone = phone,image ="",password =password,bdate=bdate,gender=gender,weight=weight,age = age,blood=blood,qr=qr).save()

		else:
			imagedata=ContentFile(base64.b64decode(image), name='useriamge.jpg')
			User(name =name,national_number =national_number,phone = phone,image =imagedata,password =password,bdate=bdate,gender=gender,weight=weight,age = age,blood=blood,qr=qr).save()
	
		return JsonResponse({'response':'ok'})	
		
	except Exception as e:
		print(e)
		return JsonResponse({'response':'error'})	



@csrf_exempt		
def getDoctorBookings(request):
		try:
			body_e=request.body.decode('utf-8')
			body=json.loads(body_e)		
			admin_id=body['admin_id']
			admin_type=body['admin_type']
			data={'response':'ok','data':[]}
			if admin_type=="clinics":
					clinics=SectionClinicBooking.objects.filter(section_clinic=SectionClinic.objects.get(id=admin_id))
					
					for e in clinics:
						d={}
						d["booking_id"]=e.id
						d["commited"]=e.commited
						d["section_name"]=e.user.name
						d["section_location"]=e.section_clinic.location
						d["year"]=e.year
						d["month"]=e.month
						d["day"]=e.day
						d["hour"]=e.hour
						d["type"]="clinics"
						data['data'].append(d)
			if admin_type=="centers":

				centers=SectionCenterBooking.objects.filter(section_center=SectionCenter.objects.get(id=admin_id))
						
				for e in centers:
					d={}
					d["booking_id"]=e.id
					d["commited"]=e.commited
					d["section_name"]=e.user.name
					d["section_location"]=e.section_center.location
					d["year"]=e.year
					d["month"]=e.month
					d["day"]=e.day
					d["hour"]=e.hour
					d["type"]="centers"
					data['data'].append(d)
			if admin_type=="hospitals":
				hospitals=SectionHospitalBooking.objects.filter(section_hospital=SectionHospital.objects.get(id=admin_id))

				for e in hospitals:
					d={}
					d["booking_id"]=e.id
					d["commited"]=e.commited
					d["section_name"]=e.user.name
					d["section_location"]=e.section_hospital.location
					d["year"]=e.year
					d["month"]=e.month
					d["day"]=e.day
					d["hour"]=e.hour
					d["type"]="hospitals"
					data['data'].append(d)			
			return JsonResponse(data)
		except Exception as e:
			print(e)
			return JsonResponse({'response':'error'})	
@csrf_exempt		
def confirmBooking(request):
		try:
			body_e=request.body.decode('utf-8')
			body=json.loads(body_e)		
			booking_id=body['booking_id']
			admin_type=body['admin_type']
			data={'response':'ok'}
			if admin_type=="clinics":
				clinics=SectionClinicBooking.objects.get(id=booking_id)
				clinics.commited=2
				clinics.save()
	
			if admin_type=="centers":

				centers=SectionCenterBooking.objects.get(id=booking_id)
				centers.commited=2
				centers.save()			
			if admin_type=="hospitals":
				hospitals=SectionHospitalBooking.objects.get(id=booking_id)
				hospitals.commited=2
				hospitals.save()
				
			return JsonResponse(data)
		except Exception as e:
			print(e)
			return JsonResponse({'response':'error'})	
from .service import send_topic_notification
@csrf_exempt		
def cancellBooking(request):
		try:
			body_e=request.body.decode('utf-8')
			body=json.loads(body_e)		
			booking_id=body['booking_id']
			admin_type=body['admin_type']
			data={'response':'ok'}
			if admin_type=="clinics":
				clinics=SectionClinicBooking.objects.get(id=booking_id)
				clinics.commited=1
				year = clinics.year
				month = clinics.month
				day = clinics.day
				hour = clinics.hour
				print(f"تم الغاء موعد مريض بتاريخ {day}/{month}/{year} الساعة {hour}")
				message = f"تم الغاء موعد مريض بتاريخ {day}/{month}/{year} الساعة {hour}"
				send_topic_notification('user', 'تم الغاء موعد', message)
				clinics.save()
	
			if admin_type=="centers":

				centers=SectionCenterBooking.objects.get(id=booking_id)
				centers.commited=1
				centers.save()			
			if admin_type=="hospitals":
				hospitals=SectionHospitalBooking.objects.get(id=booking_id)
				hospitals.commited=1
				hospitals.save()
				
			return JsonResponse(data)
		except Exception as e:
			print(e)
			return JsonResponse({'response':'error'})	
from datetime import datetime
@csrf_exempt		
def laterBookings(request):
		try:
			body_e=request.body.decode('utf-8')
			body=json.loads(body_e)		
			booking_id=body['booking_id']
			admin_type=body['admin_type']
			data={'response':'ok'}
			if admin_type=="clinics":
				clinics=SectionClinicBooking.objects.get(id=booking_id)
				clinics.commited=3
				clinics.save()
	
			if admin_type=="centers":

				centers=SectionCenterBooking.objects.get(id=booking_id)
				centers.commited=3
				centers.save()			
			if admin_type=="hospitals":
				hospitals=SectionHospitalBooking.objects.get(id=booking_id)
				
				attendance_time = datetime.now().hour
				
				print(attendance_time)
				booking_time = hospitals.hour
				print(booking_time)
				later_time = attendance_time - int(booking_time)
				print(f"later_time: {later_time}")
				other_bookings = SectionHospitalBooking.objects.exclude(id=booking_id)
				for booking in other_bookings:
					booking.hour = int(booking.hour)
					booking.hour += later_time
					booking.save()
				hospitals.commited=3
				hospitals.save()
				
			return JsonResponse(data)
		except Exception as e:
			print(e)
			return JsonResponse({'response':'error'})	
