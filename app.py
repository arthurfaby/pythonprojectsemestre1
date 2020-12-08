from functions import *
from initdics import *
import tkinter


dic_partitions = init_dic_partitions()
dic_notes = get_notes(dic_partitions)
dic_titles = get_titles(dic_partitions)
dic_coding_notes = init_dic_coding_notes()
dic_numerical_to_frequency = {1:264,2:297,3:330,4:352,5:396,6:440,7:495, 8:-1}
dic_duration = {"c":0.125, "n":0.250, "b":0.500, "r":1}

list_notes = init_list_notes()


#play_sound(dic_numerical_to_frequency, dic_coding_notes, dic_duration, dic_notes, dic_titles, "Vive le vent")


# Parameters and window 
app = tkinter.Tk()
app.geometry("640x480")
app.title("Tuto menu")


# Widgets

mainmenu = tkinter.Menu(app)

play_menu = tkinter.Menu(mainmenu, tearoff=0)
for i in dic_titles:
    play_menu.add_command(label=i, command=lambda i=i: play_sound(dic_numerical_to_frequency, dic_coding_notes, dic_duration, dic_notes, dic_titles, i))

quit_menu = tkinter.Menu(mainmenu, tearoff=0)
quit_menu.add_command(label="Quit", command=app.quit)

mainmenu.add_cascade(label="Play", menu=play_menu)
mainmenu.add_cascade(label="Quit", menu=quit_menu)




# Principal loop
app.config(menu=mainmenu)
app.mainloop()


