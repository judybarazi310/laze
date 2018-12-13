from django.test import TestCase
from .forms import PinForm

# Create your tests here.
class Setup_Class(TestCase):
    def setUp(self):
        self.Pin = Pin.objects.create(title = "Cubical", 
            description = "Open cubicals" ,
            num_votes = 12,
            time_created = 0,
            time_updated = 0,
            category = "Study", 
            latitude = 80.5263, 
            longitude = 43.4724,
            created_by = "TestMan")

class Pin_Form_Test(TestCase):
    # Invalid Form Data #1 (no creator)
    def test_PinForm_valid(self):
        form = PinForm(data={'title': "Cubical", 
            'description': "Open cubicals", 
            'num_votes': 12,
            'time_created': 0,
            'time_updated': 0,
            'category': "Study", 
            'latitude': 80.5263,
            'longitude': 43.4724})
        self.assertFalse(form.is_valid())

    # Invalid Form Data #2 (invalid latitude/longitude)
    def test_PinForm_invalid(self):
        form = PinForm(data={'title': "Cubical", 
            'description': "Open cubicals", 
            'num_votes': 12,
            'time_created': 0,
            'time_updated': 0,
            'category': "Study", 
            'latitude': "",
            'longitude': "",
            'created_by': "TestMan"})
        self.assertFalse(form.is_valid())

class Map_Views_Test(TestCase): #Esnure proper responses and redirects from buttons
    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200) #200 is the HTTP status code for "OK"

    def test_register(self):
        response = self.client.get('/accounts/register')
        self.assertEqual(response.status_code, 301) #301 is the HTTP status code for "Moved Permanently", this is good since no back button exists anyway
        
    def test_login(self):
        response = self.client.get('/accounts/login')
        self.assertEqual(response.status_code, 301) #301 is the HTTP status code for "Moved Permanently"
    
    def test_logout(self):
        response = self.client.get('/accounts/logout', follow = True)
        self.assertRedirects(response, "/accounts/login/", status_code=301)

    #Testing delete requires response = self.client.get('/delete/Pin #')

    