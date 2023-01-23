from tkinter import *
from PIL import Image,ImageTk
from plyer import notification
from tkinter import messagebox
import time

t=Tk()
t.title("Desktop_Notifier-app")
t.geometry("800x300")
img=Image.open("download2.jpeg")
tkimage=ImageTk.PhotoImage(img)

def get_details():
    get_title=title.get()
    get_msg = msg.get()
    get_time = time1.get()
    print(get_title,get_msg, get_time, t)

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        messagebox.showinfo("notifier set", "set notification ?")
        t.destroy()
        time.sleep(min_to_sec)

        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="Desktop Notifier",
                            app_icon=None,
                            toast=True,
                            timeout=10)

img_label=Label(t,image=tkimage).grid()

t_label=Label(t,text="ALERT",font=("poppins",10))
t_label.place(x=12,y=70)

title=Entry(t,width="25",font=("poppins",13))
title.place(x=123,y=70)

m_label=Label(t,text="Message",font=("poppins",10))
m_label.place(x=12,y=120)

msg = Entry(t,width="40",font=("poppins",13))
msg.place(x=123,height=30,y=120,)

title_label=Label(t,text="TIME ALERT",font=("poppins",10))
title_label.place(x=12,y=175)

time1=Entry(t,width="5",font=("poppins",13))
time1.place(x=123,y=175)


time_min_label=Label(t,text="Min",font=("poppins",10))
time_min_label.place(x=175,y=180)

but=Button(t,text="Set Notification ",font=("poppins",10,"bold"),fg="#ffffff",bg="#528DFF", width=20,
             relief="raised",
             command=get_details)
but.place(x=170,y=230)


t.resizable(0,0)
t.mainloop()