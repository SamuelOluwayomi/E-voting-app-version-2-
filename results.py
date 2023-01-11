from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
from PIL import Image, ImageTk
import mysql.connector
# from Voting_page import candidates_Box



def cnt_votes():
    result = Tk()
    result.title("Result Page")
    result.geometry("800x500")
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


# result.mainloop()