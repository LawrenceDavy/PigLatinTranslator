from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')     

def translate(req):
    original = req.GET['originaltext'].lower()

    translation = ''
    for word in original.split():
        if word[0] in ['a', 'e', 'i', 'o', 'u']:
            translation += word
            translation += 'yay '
        else:
            translation += word[1:]
            translation += word[0]
            translation += 'ay '          


    return render(req, 'translate.html', {'original': original, 'translation': translation})    

