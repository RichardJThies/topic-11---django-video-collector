from django.shortcuts import render

#views process requests and send whatever responses to where they are pointed to go?

def home(request):
    return render(request, 'video_collection/home.html')# name of the template to display template














