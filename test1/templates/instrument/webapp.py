from django.shortcuts import render

def button(request):

    return render(request, 'instrument.html')

def output(request):

    thing_to_say = "this is a test. If you are reading this... idk that's good for you"

    return render(request, "instrument.html", {"thing_to_say":thing_to_say})
