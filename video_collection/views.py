from django.shortcuts import render

#views process requests and send whatever responses to where they are pointed to go?

def home(request):
    app_name = 'Starcraft Remastered' # theme of the app
    return render(request, 'video_collection/home.html', {'app_name': app_name})# name of the template to display template














