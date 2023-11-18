from django.test import TestCase
from django.urls import reverse #converting name of url into the full path
from .models import Video

class TestHomePageMessage(TestCase):
    def test_app_title_message_shown_on_home_page(self):#self always needed in a method that is part of a class
        #Arrange?
        url = reverse('home')#finding the url from reversing the name
        #Act?
        response = self.client.get(url)#client is a django object? Used to make requests in tests?
        #Assert?
        self.assertContains(response, 'Starcraft Remastered')#finally, compare that response to what is expected

class TestAddVideos(TestCase):
    def test_add_video(self):
        #Arrange?
        valid_video = {#POST requests need key-value pairs, in python that means creating a dictionary that contains the model fields which has valid data
            'name': 'PvZ',
            'url': 'https://www.youtube.com/watch?v=d0tbAKNor8c',
            'notes': 'very nice'
        }
        #Act?
        url = reverse('add_video')#finding the url from reversing the name
        response = self.client.post(url, data=valid_video, follow=True)#Using client to add data to test db. "follow=True" ensures test follows the redirect. Without, will return 200 instead of 302
        #Assert?
        self.assertTemplateUsed('video_collection/video_list.html')

        self.assertContains(response, 'PvZ')
        self.assertContains(response, 'very nice')
        self.assertContains(response, 'https://www.youtube.com/watch?v=d0tbAKNor8c')

        video_count = Video.objects.count()#how many videos were added? Only 1 was added above
        self.assertEqual(1, video_count)

        video = Video.objects.first()#first() method returns the 1st result, there should be only 1 object in db, so it will be returned
        self.assertEqual('PvZ', video.name)#pulling out each of the related fields of the object?
        self.assertEqual('https://www.youtube.com/watch?v=d0tbAKNor8c', video.url)
        self.assertEqual('very nice', video.notes)
        self.assertEqual('d0tbAKNor8c', video.video_id)

    def test_add_video_invalid_url_not_add(self):
        pass

class TestVideoList(TestCase):
    pass


class TestVideoSearch(TestCase):
    pass


class TestVideoModel(TestCase):
    pass



















