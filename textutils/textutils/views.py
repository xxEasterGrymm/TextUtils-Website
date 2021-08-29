from django.shortcuts import render

def index(request):
    # a dictionary can be passed as the third parameter to be used in the html file
    return render(request, 'index.html')

def analyze(request):
    text = request.POST.get('text', 'default')
    removechar = request.POST.get('removechar', 'off')
    fullcaps = request.POST.get('capitalizeall', 'off')
    firstcaps = request.POST.get('capitalizefirst', 'off')
    remline = request.POST.get('newlineremove', 'off')
    remspace = request.POST.get('spaceremove', 'off')
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