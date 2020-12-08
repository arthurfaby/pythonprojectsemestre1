from time import sleep
from initdics import *
import turtle as tr
import simpleaudio as sa
import numpy as np

dic_numerical_notes = {}
partitions = open("partitions.txt", "r", encoding="utf-8")



def get_titles(dic_partitions):
    titles = []
    for i in dic_partitions.keys():
        titles.append(i)
    dic_titles = titles
    return titles

def get_notes(dic_partitions):
    notes = []
    for i in dic_partitions.keys():
        notes.append(dic_partitions[i])
    return notes


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


def add_partition(title, notes):
    partitions = open("partitions.txt", "a", encoding="utf-8")
    partitions.write("\n" + title + "\n")
    partitions.write(notes)


def get_freq_and_duration(dic_numerical_to_frequency, dic_coding_notes, dic_duration, dic_notes,dic_titles,title):
    if title in dic_titles:
        key = dic_titles.index(title)
        all_notes = dic_notes[key]
        separated_notes = []
        separated_notes = all_notes.split(" ")

        notes_seq = []
        index = 0
        n_of_p = 0
        for i in separated_notes:
            if i == "p":
                notes_seq[index-(1+n_of_p)] = notes_seq[index-(1+n_of_p)] + "p"
                n_of_p += 1
            else:
                notes_seq.append(i[0:-1])
            index+=1

        type_seq = []
        for i in separated_notes:
            if i != "p":
                type_seq.append(i[-1])

        duration_seq = []
        index = 0
        for i in type_seq:
            if "p" in notes_seq[index]:
                duration_seq.append(dic_duration[i]*1.5)
                notes_seq[index] = notes_seq[index][0:-1]
            else:
                duration_seq.append(dic_duration[i])
            index += 1

        num_notes = []
        for i in notes_seq:
            num_notes.append(dic_coding_notes[i])
            

        freq_seq = []
        for i in num_notes:
            freq_seq.append(dic_numerical_to_frequency[i])

    else:
        print("This title does not exist in the database.")
    
    return freq_seq, duration_seq

def play_sound(dic_numerical_to_frequency, dic_coding_notes, dic_duration, dic_notes, dic_titles,title):
    freq_seq, duration_seq = get_freq_and_duration(dic_numerical_to_frequency, dic_coding_notes, dic_duration, dic_notes, dic_titles,title)
    for i in range(len(freq_seq)):
        if freq_seq[i] == -1:
            sleep(duration_seq[i])
        else:
            sound(freq_seq[i], duration_seq[i])

def test(g):
    print(g)