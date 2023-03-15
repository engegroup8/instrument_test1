#from django.shortcuts import render

from django.http import HttpResponse

def testOne(request):
    return HttpResponse("this is a test. If you are reading this... idk that's good for you")

#def button(request):

#    return render(request, 'instrument.html')

#def output(request):

#    thing_to_say = "this is a test. If you are reading this... idk that's good for you" 

#    return render(request, "geniusvoice.html", "thing_to_say":thing_to_say)

