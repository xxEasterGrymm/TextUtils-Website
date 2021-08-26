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
    removechar = request.GET.get('removechar', 'off')
    fullcaps = request.GET.get('capitalizeall', 'off')
    firstcaps = request.GET.get('capitalizefirst', 'off')
    remline = request.GET.get('newlineremove', 'off')
    charcount = request.GET.get('charcount', 'off')
    analyzed = text
    params = {
        'purpose': '',
        'analyzedText': ''
    }

    if removechar == 'on':
        analyzed = ""
        specialcharacters = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for character in text:
            if character not in specialcharacters:
                analyzed = analyzed + character
            params['purpose'] = 'with Special Characters removed '

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

    if charcount == 'on':
        analyzed = analyzed\
                   + ' | Character Count of Original Text - %s' % len(text)\
                   + ' | Character Count of Analyzed Text - %s' % len(analyzed)

    params['analyzedText'] = analyzed
    return render(request, 'analyze.html', params)