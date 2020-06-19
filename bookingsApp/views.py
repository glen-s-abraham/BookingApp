from django.shortcuts import render,redirect

from .models import Slotes,Bookings

#redirect and validations pending

def listSlotes(request):
	slotes=Slotes.objects.all()
	freeSlotes=[]
	context={}
	if request.method=='GET':
		freeSlotes=[]
		if 'Find' in request.GET:
			date=request.GET['date']
			bookedSlotes=Bookings.objects.filter(date=date)

			if bookedSlotes:
				
				bookedIds=[]
				for b in bookedSlotes:
					bookedIds.append(b.slote.id)
				

				for s in slotes:
					if s.id in bookedIds:
						print(s.id, 'is booked')	
					else:
						print(s.id, 'is free')		
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
			print(sloteid,bookingdate,name,contact)		
			bookedSlote=Slotes.objects.get(pk=sloteid)
			booking=Bookings()
			booking.slote=bookedSlote
			booking.date=bookingdate
			booking.name=name
			booking.contact=contact
			booking.save()		
			print(booking.id)	
			return redirect('successRegistration',booking.id)
		

	
	
	return render(request,'listSlotes.html',context)

def successRegistration(request,id=-1):
	if id>0:
		return render(request,'successRegistration.html',{'id':id})
def cancelBooking(request):
	if request.method=='POST':
		if 'Cancel' in request.POST:
			bookingid=request.POST['id']
			print(bookingid)
			try:
				booking=Bookings.objects.get(pk=bookingid)
				booking.delete()
				return redirect('listSlotes')
			except:
				return redirect('listSlotes')
				
	return render(request,'cancelBooking.html')


