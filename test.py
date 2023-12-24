from tkinter import *
import os

show_gender = ""
def resault() :
    global show_gender
    print(f"your name is {get_user.get()} \nyour lname is {get_pass.get()}")
    if choice_gender_female.get() == 1 and choice_gender_male.get() == 1 :
        print(f"your gender is Male / Female")
        show_gender = "your gender is Male / Female"
    elif choice_gender_male.get() == 1 :
        print("your gender is Male")
        show_gender = "your gender is Male"
    elif choice_gender_female.get() == 1 :
        print(f"your gender is Female")
        show_gender = "your gender is Female"
    else :
        print(f"your gender is None")
        show_gender = "None"

    label_details.config(text=f"your name is : {get_user.get()} \nyour lname is : {get_pass.get()} \nyour gender is : {show_gender}", fg="black")
                               
window = Tk()

window.title("Milad")
window.geometry("500x500")
window.resizable(False, False)

Label(window, text="User name", bg="black", fg="white", font=("tahoma", 8)).place(x = 50, y = 50)
Label(window, text="Password", bg="black", fg="white", font=("tahoma", 8)).place(x = 50, y = 100)

get_user = Entry(window)
get_user.place(x = 110, y = 50)
get_pass = Entry(window)
get_pass.place(x = 110, y = 100)

Button(window, text="print", bg="black", fg="white", font=("tahoma", 12), command=resault).place(x = 240, y = 70)

choice_gender_male = IntVar()
choice_gender_female = IntVar()
Checkbutton(window, text="Male", variable=choice_gender_male).place(x = 340, y = 65)
Checkbutton(window, text="Female", variable=choice_gender_female).place(x = 340, y = 85)


label_details = Label(window, text="your name is :\nyour lname is :\nyour gender is :", fg="black")
label_details.place(x = 50, y = 130)

Modes = [("Student", "Student"), ("Teacher", "Teacher"), ("Retired", "Retired")]
choice = StringVar()
choice.set("Student")

for text,mode in Modes :
    Radiobutton(window, text=text, variable=choice, value=mode).place(x = 300, y = 300)
















window.mainloop()
