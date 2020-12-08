from functions import *

partitions = open("partitions.txt", "r", encoding="utf-8")



def init_dic_partitions():
    dic_partitions = {}
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
            dic_partitions[title_init] = notes_init
    return dic_partitions

def init_list_notes():
    return ["DO","RE","MI","FA","SOL","LA","SI","Z"]

def init_dic_coding_notes():
    dic_coding_notes = {}
    notes = init_list_notes()
    for i in range(len(notes)):
        dic_coding_notes[notes[i]] = i+1
    return dic_coding_notes
