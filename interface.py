from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
from PIL import Image, ImageTk
import mysql.connector




# mydb = mysql.connector.connect(hostname = "localhost", username = "samuel", password = "password")

win = Tk()
win.title("E-voting App")
win.geometry("2000x800")
image = Image.open("main_windows.jpg")
new_image = image.resize((2000, 800))
main_windows = ImageTk.PhotoImage(new_image)

label1 = tk.Label(win, image=main_windows)
label1.pack()



l1 = tk.Label(win, width=70, height=15, bg="gainsboro")
l1.place(x=400, y=150)
heading = Label(win, text="Login", font='Verdana 25 bold', bg = "gainsboro")
heading.place(x=480, y=200)
username = Label(win, text="User Name :", font='Verdana 10 bold', bg = "gainsboro")
username.place(x=480, y=250)
userpass = Label(win, text="Password :", font='Verdana 10 bold', bg = "gainsboro")
userpass.place(x=480, y=300)
user_name = StringVar()
password = StringVar()
userentry = Entry(win, width=40, textvariable=user_name)
userentry.focus()
userentry.place(x=575, y=250)
passentry = Entry(win, width=40, show="*", textvariable=password)
passentry.place(x=575, y=300)


# button login and clear
def clear():
    userentry.delete(0,END)
    passentry.delete(0,END)

def close():
    win.destroy()

def dashboard():
    import Voting_page
class app():
    def __init__(self):
        pass
        # self.voter_ID = voter_ID
        # self.password = password

    def login(self):
        if user_name.get() == "" or password.get() == "":
            messagebox.showerror("Error", "Enter User Name And Password", parent=win)
        else:
            try:
                con = pymysql.Connection(host="localhost", user="samuel", password="password", database= "e_voting")
                cur = con.cursor()

                cur.execute("select * from user_informations where username=%s and password = %s",
                            (user_name.get(), password.get()))
                row = cur.fetchone()

                if row == None:
                    messagebox.showerror("Error", "Invalid User Name And Password", parent=win)

                else:
                    messagebox.showinfo("Success", "Successfully Login", parent=win)
                    close()
                    dashboard()
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=win)

    def signup(self):
        win2 = tk.Tk()
        win2.title("sign_up")
        win2.resizable(False, False)
        win2.geometry("1000x1000")
        image1 = Image.open("windows1.jpg")
        new_image1 = image1.resize((1000, 800))
        main_window1 = ImageTk.PhotoImage(new_image1, master=win2)

        label2 = tk.Label(win2, image=main_window1)
        label2.pack()

        # signup database connect
        def action():
            if first_name.get() == "" or last_name.get() == "" or age.get() == "" or city.get() == "" or NIN.get() == "" or user_name.get() == "" or password.get() == "" or very_pass.get() == "":
                messagebox.showerror("Error", "All Fields Are Required", parent=win2)
            elif password.get() != very_pass.get():
                messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=win2)
            else:
                try:

                    con = mysql.connector.connect(host= "localhost", user= "samuel", password= "password", database= "e_voting")
                    cur = con.cursor()
                    cur.execute("select * from user_informations where username= '%s'", (user_name.get()))
                    row = cur.fetchone()
                    if row != None:
                        messagebox.showerror("Error", "User Name Already Exits", parent=win2)
                    else:
                        cur.execute(
                            "insert into user_informations(first_name,last_name,age,gender,city,NIN,username,password) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                            (
                                first_name.get(),
                                last_name.get(),
                                age.get(),
                                var.get(),
                                city.get(),
                                NIN.get(),
                                user_name.get(),
                                password.get()
                            ))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success", "Ragistration Successfull", parent=win2)
                        clear()
                        switch()

                except Exception as es:
                    messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=win2)

        # close signup function
        def switch():
            win2.destroy()

        # clear data function
        def clear():
            first_name.delete(0, END)
            last_name.delete(0, END)
            age.delete(0, END)
            var.set("Male")
            city.delete(0, END)
            NIN.delete(0, END)
            user_name.delete(0, END)
            password.delete(0, END)
            very_pass.delete(0, END)

        # start Signup Window



        # heading label
        heading = Label(win2, text="Signup", font='Verdana 20 bold', bg = "white")
        heading.place(x=80, y=60)

        # form data label
        first_name = Label(win2, text="First Name :", font='Verdana 10 bold', bg = "white")
        first_name.place(x=80, y=130)

        last_name = Label(win2, text="Last Name :", font='Verdana 10 bold', bg = "white")
        last_name.place(x=80, y=160)

        age = Label(win2, text="Age :", font='Verdana 10 bold', bg = "white")
        age.place(x=80, y=190)

        Gender = Label(win2, text="Gender :", font='Verdana 10 bold', bg = "white")
        Gender.place(x=80, y=220)

        city = Label(win2, text="City :", font='Verdana 10 bold', bg = "white")
        city.place(x=80, y=260)

        NIN = Label(win2, text="NIN :", font='Verdana 10 bold', bg = "white")
        NIN.place(x=80, y=290)

        user_name = Label(win2, text="User Name :", font='Verdana 10 bold', bg = "white")
        user_name.place(x=80, y=320)

        password = Label(win2, text="Password :", font='Verdana 10 bold', bg = "white")
        password.place(x=80, y=350)

        very_pass = Label(win2, text="Verify Password:", font='Verdana 10 bold', bg = "white")
        very_pass.place(x=80, y=380)

        # Entry Box ------------------------------------------------------------------

        first_name = StringVar()
        last_name = StringVar()
        age = IntVar(win2, value=0)
        var = StringVar()
        city = StringVar()
        NIN = StringVar()
        user_name = StringVar()
        password = StringVar()
        very_pass = StringVar()

        first_name = Entry(win2, width=40, textvariable=first_name)
        first_name.place(x=200, y=133)

        last_name = Entry(win2, width=40, textvariable=last_name)
        last_name.place(x=200, y=163)

        age = Entry(win2, width=40, textvariable=age)
        age.place(x=200, y=193)

        Radio_button_male = ttk.Radiobutton(win2, text='Male', value="Male", variable=var).place(x=200, y=220)
        Radio_button_female = ttk.Radiobutton(win2, text='Female', value="Female", variable=var).place(x=200, y=238)

        city = Entry(win2, width=40, textvariable=city)
        city.place(x=200, y=263)

        NIN = Entry(win2, width=40, textvariable=NIN)
        NIN.place(x=200, y=293)

        user_name = Entry(win2, width=40, textvariable=user_name)
        user_name.place(x=200, y=323)

        password = Entry(win2, width=40, textvariable=password)
        password.place(x=200, y=353)

        very_pass = Entry(win2, width=40, show="*", textvariable=very_pass)
        very_pass.place(x=200, y=383)

        # button login and clear

        btn_signup = Button(win2, text="Signup", font='Verdana 10 bold', command=action)
        btn_signup.place(x=200, y=413)

        btn_login = Button(win2, text="Clear", font='Verdana 10 bold', command=clear)
        btn_login.place(x=280, y=413)

        sign_up_btn = Button(win2, text="Switch To Login", command=switch)
        sign_up_btn.place(x=350, y=20)
        win2.mainloop()


object1 = app()


    # ---------------------------------------------------------------------------End Singup Window-----------------------------------
btn_login = Button(win, text="Login", font='Verdana 10 bold', command=object1.login)
btn_login.place(x=575, y=330)

btn_login = Button(win, text="Clear", font='Verdana 10 bold', command=clear)
btn_login.place(x=640, y=330)

    # signup button

sign_up_btn = Button(win, text="Switch To Sign up", command=object1.signup)
sign_up_btn.place(x=700, y=330)


win.mainloop()