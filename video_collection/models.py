from django.db import models
from urllib import parse#splitting pieces of urls
from django.core.exceptions import ValidationError

# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=200)#constraint
    url = models.CharField(max_length=400)#constraint
    notes = models.TextField(blank=True, null=True)#notes not required
    video_id = models.CharField(max_length=40, unique=True)#unique constraint stops duplicate videos

    def save(self, *args, **kwargs):# arguments, key word arguments? Matches to django save method?
        if not self.url.startswith('https://www.youtube.com/watch'):#does not guarantee valid url, because video id could be fake?
            raise ValidationError(f'Not a YouTube URL {self.url}')
        #pull out video id
        url_components = parse.urlparse(self.url)
        query_string = url_components.query#pull out query string, aka "?v=wtwtyrww" part of YT url
        if not query_string:
            raise ValidationError(f'Invalid YouTube URL {self.url}')
        parameters = parse.parse_qs(query_string, strict_parsing=True)#converting query string into dictionary like {v: wtwtyrww}. strict_parsing=True constraint to ensure query string is real
        v_parameters_list = parameters.get('v')#search parameters dictionary. return Noe if no key found 19:55??
        if not v_parameters_list:#Checking if None or empty list
            raise ValidationError(f'Invalid YouTube URL, missing parameters {self.url}')
        self.video_id = v_parameters_list[0]#0, or 1st elemetn in the list is the string?

        super().save(*args, **kwargs)#call django save function
    
    def __str__(self):
        return f'ID: {self.pk}, Name: {self.name}, URL: {self.url}, Video_ID: {self.video_id}, Notes: {self.notes[:200]}'#not showen to user, but in console IIRC?



