# manually created file - xxEasterGrymm

from django.shortcuts import render

def index(request):
    # a dictionary can be passed as the third parameter to be used in the html file
    return render(request, 'index.html')

def analyze(request):
    text = request.GET.get('text', 'default')
    removechar = request.GET.get('removechar', 'off')
    fullcaps = request.GET.get('capitalizeall', 'off')
    firstcaps = request.GET.get('capitalizefirst', 'off')
    remline = request.GET.get('newlineremove', 'off')
    remspace = request.GET.get('spaceremove', 'off')
    analyzed = text
    params = {
        'analyzedText': '',
        'originalCount': '',
        'analyzedCount': ''
    }

    if removechar == 'on':
        analyzed = ""
        specialcharacters = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for character in text:
            if character not in specialcharacters:
                analyzed = analyzed + character

    if firstcaps == 'on':
        analyzed = analyzed[0].upper() + analyzed[1:len(analyzed)]

    if fullcaps == 'on':
        analyzed = analyzed.upper()

    if remline == 'on':
        temp = ""
        for character in analyzed:
            if character != "\n":
                temp = temp + character
            analyzed = temp

    if remspace == 'on':
        temp = ""
        for character in analyzed:
            if character != " ":
                temp = temp + character
            analyzed = temp

    params['analyzedText'] = analyzed
    params['originalCount'] = len(text)
    params['analyzedCount'] = len(analyzed)
    return render(request, 'analyze.html', params)