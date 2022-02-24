# Tayyip Güney 21.02.2022

# Requests

# General Information:
# I want to choose random information with the requests module.

# Acceptance Criteria
# * Get the name, surname, city and country information of a random person by using the requests module.
# (Example=> name:Amber, surname: Murray, city: Salisbury, country: United Kingdom)
# * Make lowercase and adjacent by removing the spaces.
# (Example=> ambermurraysalisburyunitedkingdom)
# * Then randomly shuffle the location of all the characters.
# (Example=> mberarrumasyarubsiluniydetmdoingk)
# * Apply this process for 100 different people and write in a list.
# * Find that has the most characters and print it.


from datetime import datetime
import random
import requests


req = requests.get('https://randomuser.me/api/')

z_list=[]
list_user=[]
check_lenght=0

s_time= datetime.now()

for i in range(100):
    
    req = requests.get('https://randomuser.me/api/')
    name=req.json()["results"][0]["name"]["first"]
    surname=req.json()["results"][0]["name"]["last"]
    city=req.json()["results"][0]["location"]["city"]
    county=req.json()["results"][0]["location"]["country"]
    
    str_lower=(name+surname+city+county).lower()
    norm_w=""
    shuf_w=""
    
    for j in str_lower:             # without space
        if j!=" ":
            z_list.append(j)
    for k in z_list:          # normal word
        norm_w+=k  
        
    random.shuffle(z_list)
    for m in z_list:          # shuffle word
        shuf_w+=m 
        
    list_length=len(z_list)     
    if list_length>check_lenght: # find longest word
        check_lenght=len(z_list)   
        list_user=[name,surname,city,county,norm_w,shuf_w]   # result list for longest word    

    z_list=[]

print(f"Name    : {list_user[0]}\nSurname : {list_user[1]}\nCity    : {list_user[2]}")
print(f"Country : {list_user[3]}\n\nLowercase and Adjacent : {list_user[4]}")   
print(f"Randomly Shuffle       : {list_user[5]}\n") 
  
e_time=datetime.now()

print("Process Duration :",int((e_time-s_time).seconds),"seconds")

# print(list_user)
