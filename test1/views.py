from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def testOne(request):
    #return HttpResponse("this is a test. If you are reading this... idk that's good for you")
    template = loader.get_template('instrument.html')
    return HttpResponse(template.render())
