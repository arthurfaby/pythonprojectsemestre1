import functions as f

partitions = open("partitions.txt", "r", encoding="utf-8")

dic = {}
titles = []
notes = []




L = partitions.read()
L = L.split("\n")

partitions.close()
for i in range(1,len(L)+1):
    if i%2 == 1:
        title_init = L[i-1]
        title_init = title_init[title_init.index(' ')+1:]
        titles.append(title_init)
    else:
        notes_init = L[i-1]
        notes.append(notes_init)
        dic[title_init] = notes_init
        


print(f.get_notes_and_durations(dic,  "Au feu les pompiers"))

#dic = {}
#dic["Frère Jacques"] = "SOL"
#dic["Une souris verte"] = "FA"
#str = "1 Bonjour"
#str = str[str.index(" ")+1:]
#print(str)
