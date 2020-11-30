from time import sleep
import numpy as np
import simpleaudio as sa
import turtle as tr

def sound(freq,duration):
    sample_rate=44100
    t=np.linspace(0, duration, int(duration*sample_rate), False)
    tone=np.sin(freq*t*(6)*np.pi)
    tone*=8388607/np.max(np.abs(tone))
    tone=tone.astype(np.int32)
    i=0
    byte_array=[]
    for b in tone.tobytes():
        if i%4!=3:
            byte_array.append(b)
        i+=1
    audio=bytearray(byte_array)
    play_obj=sa.play_buffer(audio,1,3,sample_rate)
    play_obj.wait_done()

def get_notes(dic, title):
    notes = dic[title]
    notes = notes.split(" ")
    return notes

def get_notes_and_type_of_duration(dic, title):
    
    notes_and_type_of_duration = []
    for i in get_notes(dic, title):
        duration = i[len(i)-1]
        i = i[0:len(i)-1]
        notes_and_type_of_duration.append(i)
        notes_and_type_of_duration.append(duration)
    return notes_and_type_of_duration

def get_notes_and_durations(dic, title):
    
    notes_and_durations = []
    for i in get_notes(dic, title):
        duration = i[len(i)-1]
        i = i[0:len(i)-1]
        notes_and_durations.append(i)
        if duration == "c":
            notes_and_durations.append("125")
        elif duration == "n":
            notes_and_durations.append("250")
        elif duration == "b":
            notes_and_durations.append("500")
        else:
            notes_and_durations.append("1000")
    return notes_and_durations

