from os import error
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_p():
    input3.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    passwd_letters=[random.choice(letters)for _ in range(random.randint(8,10))]
    passwd_number=[random.choice(numbers)for _ in range(random.randint(2,4))]
    passwd_sym=[random.choice(symbols)for _ in range(random.randint(2,4))] 
    passd_list=passwd_letters+passwd_number+passwd_sym
    random.shuffle(passd_list)
    passwd="".join(passd_list)
    pyperclip.copy(passwd)
    input3.insert(0,passwd)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name=input1.get()
    user_name=input2.get()
    password=input3.get()
    new_data={
        website_name:{
            "email":user_name,
            "password":password
        }
    }
    if (len(website_name)<=0 or len(user_name)<=0 or len(password)<=0):
        messagebox.showinfo(title="Oops",message="dont leave anything empty")
    else:
        try:
            with open("data.json","r") as data_file:
                data=json.load(data_file)
                
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:      
            #updating new data with old data          
            data.update(new_data)
            with open("data.json","w") as data_file:    
                #saving the updated data
                json.dump(data,data_file,indent=4)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = input1.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
logo=PhotoImage(file="logo.png")
canvas=Canvas(width=200,height=200,highlightthickness=0)
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)
website_label=Label(text="Website")
website_label.grid(row=1,column=0)
input1=Entry(width=35)
input1.focus()
input1.grid(row=1,column=1,columnspan=2)
user_name_label=Label(text="User_name")
user_name_label.grid(row=2,column=0)
input2=Entry(width=35)
input2.insert(0,"vishal@123")
input2.grid(row=2,column=1,columnspan=2)
password_label=Label(text="Password")
password_label.grid(row=3,column=0)
input3=Entry(width=26)
input3.grid(row=3,column=1)
genratepass=Button(text="Generate",command=generate_p)
genratepass.grid(row=3,column=2)
save=Button(text="Save",width=30,command=save)
save.grid(row=4,column=1,columnspan=2)
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)
window.mainloop()
