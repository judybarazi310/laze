from django.db import models


# Create your models here.
class Pin(models.Model):
    PIN_CATEGORIES = (
        ('FOOD', 'Food'),
        ('Entertainment', (
            ('T', 'Theater'),
            ('M', 'Mall'),
        )
         ),
        ('VEHP', 'Parking'),
        ('STY', 'Study'),
        ('Recreational', (
            ('GYM', 'Gym'),
            ('POOL', 'Swimming Pool'),
            ('SQUA', 'Squash Court'),
            ('BSKT', 'Basketball Court'),
            ('PARK', 'Parks'),

        )
         ),
    )
    # automatic models.AutoField(primary_key = True)
    title = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField(null=False, blank=True)
    num_votes = models.IntegerField(blank=False, default=0)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=4, choices=PIN_CATEGORIES, null=False)
    latitude = models.DecimalField(decimal_places=10, max_digits=10, null=True)#TODO change null to false
    longitude = models.DecimalField(decimal_places=10, max_digits=10, null=True)#TODO change null to false

    @property
    def votes(self):
        return 5
