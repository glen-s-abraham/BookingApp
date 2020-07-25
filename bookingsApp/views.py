from django.shortcuts import render,redirect
import datetime 
import calendar
import random
from django.core.mail import send_mail

from .models import Slotes,Bookings,Days,DaySchedule,ScheduleSlotes


#redirect and validations pending

def listSlotes(request):
	slotes=[]
	freeSlotes=[]
	context={}
	if request.method=='GET':
		freeSlotes=[]
		if 'Find' in request.GET:
			date=request.GET['date']
			
			day = datetime.datetime.strptime(date,'%Y-%m-%d').weekday()
			bookedSlotes=Bookings.objects.filter(date=date,status='confirmed')
			
			dayid=Days.objects.get(day=calendar.day_name[day])
			
			schedule=DaySchedule.objects.get(day=dayid)

			schedule=ScheduleSlotes.objects.filter(schedule=schedule.schedule)
			for si in schedule:
				print(si.slote)
				slotes.append(si.slote)
			print(slotes)
			if bookedSlotes:
				
				bookedIds=[]
				for b in bookedSlotes:
					bookedIds.append(b.slote.id)
				

				for s in slotes:
					if s.id in bookedIds:
						print(s, 'is booked')	
					else:
						print(s, 'is free')		
						freeSlotes.append(s)	
			else:
				freeSlotes=slotes;
			context['slotes']=freeSlotes
			if date:
				context['date']=date
	if request.method=='POST':
		if 'Book' in request.POST:
			sloteid=request.POST['slote']

			name=request.POST['name']
			bookingdate=request.POST['bdate']
			contact=request.POST['contact']
			otp=random.randint(1000,9999)
			print(sloteid,bookingdate,name,contact)		
			bookedSlote=Slotes.objects.get(pk=sloteid)
			booking=Bookings()
			booking.slote=bookedSlote
			booking.date=bookingdate
			booking.name=name
			booking.contact=contact
			booking.otp=otp
			booking.save()		
			#sendmail to recepient
			fromAddr='service@site.com'
			toAdrr=[contact]
			subject='Confirm Your booking'
			message='your Confirmation otp is:'+str(otp)

			send_mail(subject,message,fromAddr,toAdrr,fail_silently=False,)
    
			return redirect('confirmBooking',booking.id)
		

	
	
	return render(request,'listSlotes.html',context)

def confirmBooking(request,id=-1):
	msg=None
	if id>-1:
		if request.method=='POST':
			if 'Confirmation' in request.POST:
				userid=request.POST['id']
				userotp=request.POST['otp']
				user=Bookings.objects.get(id=userid)
				print(userid,userotp,user.otp)
				if int(userotp)==user.otp:
					user.status='confirmed'
					user.save()
					fromAddr='service@site.com'
					toAdrr=[user.contact]
					subject='Booking details'
					message='Booking name:'+str(user.name)+"Booking id:"+str(user.id)

					send_mail(subject,message,fromAddr,toAdrr,fail_silently=False,)
					return redirect('successRegistration',user.id)

				else:
					msg='wrong otp'
					print('wrong otp')	

	context={'id':id}
	if msg:
		context['msg']=msg				

				
	return render(request,'confirmBooking.html',context)


	

def successRegistration(request,id=-1):
	if id>0:
		user=Bookings.objects.get(pk=id)
		return render(request,'successRegistration.html',{'name':user.name})

def cancelBooking(request):
	msg=""
	if request.method=='POST':
		
		if 'Cancel' in request.POST:
			bookingid=request.POST['id']
			print(bookingid)
			try:
				booking=Bookings.objects.get(pk=bookingid)
				id=booking.id
				booking.delete()
				return redirect('successCancelation',id)
			except:
				msg="Invalid id"
				
				
	return render(request,'cancelBooking.html',{'msg':msg})

def successCancelation(request,id=-1):
	if id>0:
		
		return render(request,'successCancelation.html')	



