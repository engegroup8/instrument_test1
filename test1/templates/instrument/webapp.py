from django.shortcuts import render

#def button(request):

#    return render(request, 'instrument.html')

#def output(request):

#    thing_to_say = "this is a test. If you are reading this... idk that's good for you"

#    return render(request, "instrument.html", {"thing_to_say":thing_to_say})

import cv2
import time
import numpy as np
import copy
from pysinewave import SineWave

def showthis(request):

    cap = cv2.VideoCapture(0)

    upper_threshold = [82, 82, 82]

    pitches = []

    for n in range(25):
        pitches.append(SineWave(pitch = n-12, decibels=-100, decibels_per_second=1000))

    for wave in pitches:
        wave.play()
    old_notes = set()
    while True:
        ret, frame = cap.read()
        #image = cap.imread(frame)
        height, width, _ = frame.shape
        #put here: logic for determining the dark spots on a certain row (what Leila is writing)
        dark = []
        notes = set()
        y = height//2

        for i in range(width):
            pixel = frame[y,i,:]
            # all(p < t for p, t in zip(pixel, upper_threshold))
            if pixel[0] <= upper_threshold[0] and pixel[1] <= upper_threshold[1] and pixel[2] <= upper_threshold[2]:

                dark.append(i)

        for horizontal_pos in dark:
            notes.add(int(horizontal_pos/(width/25)))
        turn_on = notes-old_notes
        turn_off = old_notes-notes
        for idx in turn_on:
            pitches[idx].set_volume(10)
        for idx in turn_off:
            pitches[idx].set_volume(-100)

        #figure out how to convert array with indices for dark spots into corresponding frequencies

        cv2.line(img=frame, pt1=(0,height//2), pt2=(width,height//2), color=(0,0,255),thickness=5, lineType=8, shift=0)
        cv2.imshow('Input', frame)

        c = cv2.waitKey(1)
        if c == 27:
            break

        old_notes = copy.deepcopy(notes)

        return render(request, "instrument.html")

    cap.release()
    cv2.destroyAllWindows


