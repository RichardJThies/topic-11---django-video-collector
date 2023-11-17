from django.test import TestCase
from django.urls import reverse #converting name of url into the full path

class TestHomePageMessage(TestCase):
    def test_app_title_message_shown_on_home_page(self):#self always needed in a method that is part of a class
        #Arrange?
        url = reverse('home')#0:00-4:30?
        #Act?
        response = self.client.get(url)
        #Assert?
        self.assertContains(response, 'Starcraft Remastered')
































