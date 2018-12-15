from django.db import models
from django.conf import settings

class Pin(models.Model):
	PIN_CATEGORIES = (
		('INFO', 'Info'),
		('FOOD', 'Food'),
		('VEHP', 'Parking'),
		('STY', 'Study'),
		('Entertainment', (
			('T', 'Theater'),
			('M', 'Mall'),
		)
		 ),
		('Recreational', (
			('GYM', 'Gym'),
			('POOL', 'Swimming Pool'),
			('SQUA', 'Squash Court'),
			('BSKT', 'Basketball Court'),
			('PARK', 'Parks'),

		)
		 )
	)
	title = models.CharField(max_length=64, blank=False, null=False)
	description = models.TextField(max_length=1000,null=False, blank=True)
	num_votes = models.IntegerField(blank=False, default=0)
	time_created = models.DateTimeField(auto_now_add=True)
	time_updated = models.DateTimeField(auto_now=True)
	category = models.CharField(max_length=4, choices=PIN_CATEGORIES, default= "INFO", null=False)
	latitude = models.TextField(null=False)
	longitude = models.TextField(null=False)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	people_nearby = models.IntegerField(blank=False, default=0)

	@property
	def votes(self):
		return 5
	def __str__(self):
		return self.title

class UserLocation(models.Model):
	latitude = models.TextField(null=False)
	longitude = models.TextField(null=False)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)