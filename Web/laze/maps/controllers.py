import math

def calculate_nearby(locations, pins):
	distance_in_meters = 10

	for pin in pins:
		for location in locations:
			if distance(location, pin) < distance_in_meters:
				pin.people_nearby += 1

		pin.save(update_fields=['people_nearby'])

def distance(location, pin):
	radius = 6371000

	phi1 = math.radians(float(pin.latitude))
	phi2 = math.radians(float(location.latitude))
	phi_diff = math.radians(float(pin.latitude) - float(location.latitude))
	lambda_diff = math.radians(float(pin.longitude) - float(location.longitude))

	a = math.sin(phi_diff / 2.)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(lambda_diff / 2.)**2

	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

	d = radius * c

	return d