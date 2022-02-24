# Tayyip Güney 20.02.2022
# Random Password

# General Information:
# I want to use a program which can generate random password and display the result on user interface. 

# Acceptance Criteria:

# * Use tkinter package to solve the problem. (You can use the random student codes as template)
# * Password length must be 10 characters long. 
# * It must contain at least 2 upper case letter, 2 digits and 2 special symbols. 
# * You must import some required modules or packages. 
# * The GUI of program must contain at least a button and a label (customize the screen according to yourself) 
# * The result should be display on the password label when the user click the generate button.



from datetime import datetime
from logging import root
import random
from string import ascii_lowercase
import string
import tkinter as tk



def all(): # all characters
    a=random.randint(33,126)   
    return chr(a)
    
def upper(): # upper case letter
    a=random.randint(65,90)
    return chr(a)
       
def digit():
    a=random.randint(48,57)
    return chr(a)

def special():          # special symbols  
    sec=random.randint(0,1)
    if sec==0:
        c=random.randint(33,47)
    else:
        c=random.randint(58,96) 
    return chr(c)

def random_password():
        list_pass=[]
    # generate random number of random numbers
        t_dig=random.randint(2,3)  # generate 2 or 3 times 
        x=0
        while x<t_dig:         
            a=digit()
            list_pass.append(a)
            x+=1
            
    # generate a random number of random capital letters      
        t_up=random.randint(2,3)   # generate 2 or 3 times
        x=0
        while x<t_up:         
            a=upper()
            list_pass.append(a)
            x+=1
    # generate a random number of random special symbols      
        t_spe=random.randint(2,3) # generate 2 or 3 times
        x=0
        while x<t_spe:         
            a=special()
            list_pass.append(a)
            x+=1
        
    # add a lowercase
        lower_c=random.sample(list(string.ascii_lowercase),1) # add a lower case
        list_pass.append(lower_c[0])
        
    # Generating the remaining number of random characters
        rem=10-(t_dig+t_spe+t_up+1) # +1 lower case
        x=0
        while x<rem:
            a=all()
            list_pass.append(a)
            x+=1
            
        random.shuffle(list_pass)  # shuffle the list
    
        password=""
    
        for i in list_pass:
            password+=str(i)

        list_pass=[]
        
        label.config(text=password)
        
# random_student()             
window = tk.Tk()


window.title("Random Student")
window.geometry("500x300")


key_application = tk.Frame(window)
key_application.grid()


# label
label_txt = tk.Label(key_application, text="Random Password", bg = "yellow", relief = "solid", cursor = "target", font="castellar 15 bold")
label_txt.grid(padx=110, pady=10)

# label
label = tk.Label(key_application,bg="#a8ff78", text="Please push the button ", font="arial 12")
label.grid(padx=110, pady=20)


# button
# button1 = tk.Button(key_application,background="#78ffd6", text=" Generate Password ", width=50, height=5, command=random_password)

button1 = tk.Button(key_application,text=" Generate Password ",
bd=10,
bg="#78ffd6",
fg="black",
activeforeground="Orange",
activebackground="blue",
font="calibri",
height=2,
highlightcolor="purple",
justify="left",
relief="ridge",
command=random_password)

button1.grid(padx=110, pady=40)

# label_list=tk.Listbox(key_application,bg="red")
# label.grid(padx=110, pady=10)




window.mainloop()
