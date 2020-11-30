from time import sleep
import numpy as np
import simpleaudio as sa
import turtle as tr

def set_dic_title_and_writed_notes():
    partitions = open("partitions.txt", "r", encoding="utf-8")
    dic_title_and_writed_notes = {}
    titles = []
    notes = []
    L = partitions.read()
    L = L.split("\n")
    for i in range(1,len(L)+1):
        if i%2 == 1:
            title_init = L[i-1]
            title_init = title_init[title_init.index(' ')+1:]
            titles.append(title_init)
        else:
            notes_init = L[i-1]
            notes.append(notes_init)
            dic_title_and_writed_notes[title_init] = notes_init
    return dic_title_and_writed_notes



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

def get_notes(dic_title_and_writed_notes, title):
    notes = dic_title_and_writed_notes[title]
    notes = notes.split(" ")
    return notes

def get_notes_and_type_of_duration(dic_title_and_writed_notes, title):
    
    notes_and_type_of_duration = []
    for i in get_notes(dic_title_and_writed_notes, title):
        duration = i[len(i)-1]
        i = i[0:len(i)-1]
        notes_and_type_of_duration.append(i)
        notes_and_type_of_duration.append(duration)
    return notes_and_type_of_duration

def get_notes_and_durations(dic_title_and_writed_notes, title):
    L = get_notes(dic_title_and_writed_notes, title)
    notes_and_durations = [[],[]]
    for i in get_notes(dic_title_and_writed_notes, title):
        duration = i[len(i)-1]
        note = i[0:len(i)-1]

        # We transform the note by the associated a number

        if note == "DO":
            note = 1
        elif note == "RE":
            note = 2
        elif note == "MI":
            note = 3
        elif note == "FA":
            note = 4
        elif note == "SOL":
            note = 5
        elif note == "LA":
            note = 6
        elif note == "SI":
            note = 7

        # We transform the letter by the associated time in ms


        if duration == "c":
            duration = 125
        elif duration == "n":
            duration = 250
        elif duration == "b":
            duration = 500
        else:
            duration = 1000

        notes_and_durations[0].append(note)
        notes_and_durations[1].append(duration)

    return notes_and_durations


def add_partition(title, notes):
    partitions = open("partitions.txt", "a", encoding="utf-8")
    partitions.write("\n" + title + "\n")
    partitions.write(notes)

