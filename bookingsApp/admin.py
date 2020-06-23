from django.contrib import admin

from .models import Slotes
from .models import Bookings
from .models import Schedules
from .models import Days
from .models import ScheduleSlotes
from .models import DaySchedule
# Register your models here.
admin.site.register(Slotes)
admin.site.register(Bookings)
admin.site.register(Schedules)
admin.site.register(ScheduleSlotes)
admin.site.register(Days)
admin.site.register(DaySchedule)

