from django.db import models

class Slotes(models.Model):
	slotes=models.CharField(max_length=100,unique=True)
	def __str__(self):
		return str(self.slotes)
class Bookings(models.Model):
	slote=models.ForeignKey(Slotes,on_delete=models.CASCADE)
	date=models.DateField()
	name=models.CharField(max_length=100)
	contact=models.CharField(max_length=100)
	def __str__(self):
		return str(self.name)
class Schedules(models.Model):
	schedule=models.CharField(max_length=100,unique=True)
	def __str__(self):
		return str(self.schedule)
class Days(models.Model):
	day=models.CharField(max_length=100,unique=True)
	def __str__(self):
		return str(self.day)		

class ScheduleSlotes(models.Model):
	schedule=models.ForeignKey(Schedules,on_delete=models.CASCADE)
	slote=models.ForeignKey(Slotes,on_delete=models.CASCADE)	
	def __str__(self):
		return str(self.schedule)	

class DaySchedule(models.Model):
	day=models.ForeignKey(Days,on_delete=models.CASCADE)
	schedule=models.ForeignKey(Schedules,on_delete=models.CASCADE)	
	def __str__(self):
		return str(self.day)



