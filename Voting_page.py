import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
from PIL import Image, ImageTk
import mysql.connector

database = mysql.connector.connect(host="localhost", user="samuel", password="password", database="e_voting")

voting = Tk()
voting.title("Voting Page")
voting.geometry("2000x800")
image = Image.open("windows.jpg")
new_image = image.resize((1500, 800))
main_windows = ImageTk.PhotoImage(new_image)
#
# label1 = tk.Label(voting, image=main_windows)
# label1.pack()
canvas = Canvas(voting, width=1500, height=800)
canvas.create_image(0,0, image=main_windows, anchor='nw')
canvas.pack(fill="both", expand=True)
# canvas.create_text(400, 100, text="Vote For Your Future")
canvas.create_text(450, 170, text="Select Your Desired Candidate", font=(('helvetica'), 15, ('bold')))
canvas.create_text((380, 230),  text="Enter Username", font=(('helvetica'), 15, ('bold')))
canvas.create_text(460, 290, text="Enter Password To Confirm Vote", font=(('helvetica'), 15, ('bold')))

result = Tk()
result.title("Result Page")
result.geometry("800x500")

def cnt_votes():

    con = pymysql.Connection(host="localhost", user="samuel", password="password", database="e_voting")
    cur = con.cursor()

    count_votes = "SELECT COUNT(votes) FROM user_informations WHERE votes = %s"
    values = ["BOLA AHMED TINUBU of the All progressive Congress (APC)", "ABUBAKAR ATIKU of the People's Democratic Party(PDP)", "ADEBAYO ADEWOLE EBENEZER of the Social Democratic Party (SDP)", "PETER OBI of the Labour Party (LP)", "NNADI CHARLES OSITA of the Action Peoples Party (APP)"]
    cur.execute(count_votes, values[0])
    cnt = cur.fetchall()

    con.commit()
    con.close()
    global a
    a = cnt
    b = 1000000
    label1 = Label(result, text= "APC: 10000000", font='Verdana 25 bold')

    label2 = Label(result, text= "PDP: 10000000", font='Verdana 25 bold' )
    label3 = Label(result, text="SDP: 10000000", font='Verdana 25 bold')
    label4 = Label(result, text="LP: 10000002", font='Verdana 25 bold')
    label5 = Label(result, text="APP: 10000000", font='Verdana 25 bold')
    label1.place(x=40, y=100)
    label2.place(x=40, y=200)
    label3.place(x=40, y=300)
    label4.place(x=40, y=400)
    label5.place(x=40, y=500)
    result.mainloop()

def close_p():
    voting.destroy()
class cast_votes():
    def __init__(self,password):
        self.password = password
    def voting_system(self):
        if candidates_Box.get() == " " or entry_password.get() == " " or entry_username.get()== " ":
            messagebox.showerror("Error",  "All fields are required")
        else:
              try:
                con = pymysql.Connection(host="localhost", user="samuel", password="password", database="e_voting")
                cur = con.cursor()

                cur.execute("select * from user_informations where username=%s and password = %s",
                            (entry_username.get(),entry_password.get()))
                row = cur.fetchone()

                if row == None:
                    messagebox.showerror("Error", "Invalid Username/password", parent=voting)

                else:
                    query = """Update user_informations set votes = %s where username = %s"""
                    values = (candidates_Box.get(), entry_username.get())

                    cur.execute(query, values)


                    messagebox.showinfo("Success", "You have successfully Cast Your Vote", parent=voting)
                    close_p()
                    cnt_votes()
                con.close()
              except Exception as es:
                  messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=voting)




candidates = tk.StringVar()
candidates_Box = ttk.Combobox(voting, width=60, textvariable=candidates ,state='readonly')
candidates_Box['values'] = [" " ,"BOLA AHMED TINUBU of the All progressive Congress (APC)", "ABUBAKAR ATIKU of the People's Democratic Party(PDP)", "ADEBAYO ADEWOLE EBENEZER of the Social Democratic Party (SDP)", "PETER OBI of the Labour Party (LP)", "NNADI CHARLES OSITA of the Action Peoples Party (APP)"]
candidates_Box.current(0)
candidates_Box.place(x=300, y=195)

def show_pass():
    global entry_password, check_pass
    if check_pass.var.get():
        entry_password.config(show= "\u25CF")
    else:
        entry_password.config(show="")
entry_username = Entry(voting, width=43, highlightthickness= 3)
entry_username.place(x=300, y=250)
entry_password = Entry(voting, width=43, show= "\u25CF", highlightthickness= 3)
entry_password.config(show= "\u25CF")
check_pass = Checkbutton(canvas, text="Show password", onvalue= False, offvalue=True, command= show_pass)
check_pass.var = BooleanVar(value=True)
check_pass["variable"] = check_pass.var
entry_password.place(x=300, y=305)
check_pass.place(x=600, y=305)

object1 = cast_votes(entry_password)

show_password = Button(voting, text= "Cast Vote", background= "aquamarine3", foreground="white", command= object1.voting_system)
show_password.place(x=600, y=335)


voting.mainloop()