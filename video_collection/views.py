from django.shortcuts import render, redirect
from .forms import VideoForm
from django.contrib import messages
from .models import Video
from django.core.exceptions import ValidationError
from django.db import IntegrityError


#views process requests and send whatever responses to where they are pointed to go?

def home(request):
    app_name = 'Starcraft Remastered' # theme of the app
    return render(request, 'video_collection/home.html', {'app_name': app_name})# name of the template to display template

def add(request):#how is data getting back from the add.html?
    if request.method == 'POST':#.method is from the form in add.html?
        new_video_form = VideoForm(request.POST)#assigning variable the
        if new_video_form.is_valid():#django validation IIRC?
            try:
                new_video_form.save() #django save method
                # messages.info(request, 'New video saved!')#django temporary messages sent to template
                return redirect('video_list')
            except ValidationError:
                messages.warning(request, 'Invalid YouTube URL')
            except IntegrityError:
                messages.warning(request, 'You already added that video')
        messages.warning(request, 'Please check the data entered.')#django temporary messages sent to template
        return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})




    new_video_form = VideoForm()#structure of the new objects?
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})# send the new_video_form to the template?

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_collection/video_list.html', {'videos': videos})






