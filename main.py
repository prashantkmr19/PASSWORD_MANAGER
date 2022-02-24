from tkinter import *
from tkinter import messagebox
import random
from random import choice,randint,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        
    password_letters =[choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers)for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)

    input3.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input1.get()
    email = input2.get()
    password = input3.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo('Please make sure you have not left any feild empty')

    else:
        is_ok = messagebox.showinfo(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                           f"\nPassword: {password}\n is it ok to save? ")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                input1.delete(0, END)
                input2.delete(0, END)





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
bg = PhotoImage(file = "logo.png")
canvas.create_image(80,80,image = bg)
canvas.grid(column=2,row=1)

#label1
website_label = Label(text='Website',font=('Arial',10,'bold'))
website_label.grid(column= 1,row=2)

#label2
email_label = Label(text='Email/Username',font=('Arial',10,'bold'))
email_label.grid(column= 1,row=3)

#label3
password_label = Label(text='Password',font=('Arial',10,'bold'))
password_label.grid(column= 1,row=4)

#button1
generatepassword_button = Button(text="Generate Password",command=generate_password)
generatepassword_button.grid(column=3,row=4,)

#button2
add_button = Button(text="Add",command=save)
add_button.grid(column=2,row=5,columnspan=3)

#entry1
input1 = Entry(width=40)
print(input1.get())
input1.focus()
input1.grid(column=2,row=2,columnspan=3)

#entry2
input2 = Entry(width=40)
print(input2.get())
input2.grid(column=2,row=3,columnspan=3)
input2.insert(0,'prashant@gmail.com')

#entry3
input3 = Entry(width=22)
print(input3.get())
input3.grid(column=2,row=4)










window.mainloop()