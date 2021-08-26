# manually created file - xxEasterGrymm
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#    return HttpResponse('''<h1>Hello User</h1> <a href="https://www.google.com/">Click here</a>''')

# def about(request):
#   return HttpResponse("About")

def index(request):
    # a dictionary can be passed as the third parameter to be used in the html file
    return render(request, 'index.html')

def analyze(request):
    text = request.GET.get('text', 'default')
    removeChar = request.GET.get('removechar', 'off')
    analyzed = text
    params = {
        'purpose': '',
        'analyzedText': ''
    }
    if removeChar == 'on':
        analyzed = ""
        specialCharacters = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for character in text:
            if character not in specialCharacters:
                analyzed = analyzed + character
            params['purpose'] = 'with Special Characters removed '

    params['analyzedText'] = analyzed
    return render(request, 'analyze.html', params)

def capitalizeFirst(request):
    return HttpResponse("Capitalize First")

def newlineRemove(request):
    return HttpResponse("New line remove")

def spaceRemove(request):
    return HttpResponse("Space remove <a href='/'>Home</a>")

def characterCount(request):
    return HttpResponse("Character Count")