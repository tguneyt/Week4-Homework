# Tayyip Güney 21.02.2022
# Random Student
# Program Regulation (Problem Solving Example)

# General Information:
# I want to choose a random student in Pyton Class-2 Coursiers
# Acceptance Criteria:
# * Make changes to the random student codes that has been shared with you.
# * In current state, the program chooses a random one from the list when the button is pressed.
# * What is expected of you is to ensure that the selected person is not selected during 3 hands.

import random
import tkinter as tk
from tkinter import CENTER, END, LEFT, NO, ttk
from tkinter.ttk import Treeview

z_waiting_list=[]

std_list=["Emrullah Bey", "Ertan Bey", "Fethullah Bey", "Furkan Bey", 
"Hasan Bey", "Mehmet Bey", "Ömer Bey", "Tayyip Bey", 
"Yunus Emre Bey", "Merve Hanım", "Mustafa Bey", "Murat Bey"]

z_point=[] 
z_score=[]

for i in std_list:
    for j in range(1):
        z_point=[j,i]
        z_score.append(z_point)

def update_list():
    for i in range(len(z_score)):
        tree_list.insert(parent='',index='end',iid=i,text='',
        values=(z_score[i][1],z_score[i][0]))
        
def random_student():
  
        if len(z_waiting_list)==4:    # 4: because a person must wait 3 times
                std_list.append(z_waiting_list[0]) # first in first out 
                del z_waiting_list[0]              # first in first out 
        
        len_std=len(std_list)   # Lenght of std_list
        r_num=random.randint(0,(len_std-1)) # len_std-1) -> randint including end point
        
        str=std_list[r_num] # choose random
 
        label.config(text=str) # show on gui
        #return str
        
        z_waiting_list.append(str)  # add to waiting list
        # z_score[r_num]
        
        for i in tree_list.get_children(): # delete all list
            tree_list.delete(i)

        for i in z_score:
            for j in i:
                if j==str:
                    i[0]+=1    # count the users
                    break
            
        z_score.sort(reverse=True)   # sort from largest to smallest       
        update_list()
        del std_list[r_num]
        

window = tk.Tk()


window.title("Random Student")
window.geometry("600x600")


key_application = tk.Frame(window)
key_application.grid()


# label
# label_txt = tk.Label(key_application, text="Student name:", font="arial 15 bold")
label_txt = tk.Label(key_application, text="Student name:", font="arial 15 bold")
label_txt.grid(padx=110, pady=5)

# label
# label = tk.Label(key_application, text="Please push the botton to choose a next student ", font="arial 12")
label = tk.Label(key_application, text="Please push the button to choose a next student ", font="arial 12")
label.grid(padx=110, pady=5)


# button
# button1 = tk.Button(key_application, text=" CHOOSE ", width=50, height=5, command=random_student)
button1 = tk.Button(key_application,background="#65C7F7", text=" CHOOSE ", width=50, height=5, command=random_student)
button1.grid(padx=110, pady=30)

tree_list=ttk.Treeview(key_application,height=13)
tree_list.grid(padx=0, pady=0)

tree_list['columns'] = ('user', 'count')
tree_list.column("#0", width=0,  stretch=NO)
tree_list.column("user",anchor="w", width=100)
tree_list.column("count",anchor=CENTER,width=40)

tree_list.heading("#0",text="",anchor=CENTER)
tree_list.heading("user",text="Student",anchor=CENTER)
tree_list.heading("count",text="Count",anchor=CENTER)

update_list()

window.mainloop()