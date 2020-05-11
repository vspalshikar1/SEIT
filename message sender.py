import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror


def send_sms(number,message):
    url='https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization': 'eXECR2MnEgWheVCS6QpvimFFYvgArGFrQx9XApiSHFzHfZQKV7uGC4j7PmLa',
        'sender_id': 'FSTSMS',
        'message':message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }
    response = requests.get(url, params=params)

    dic = response.json()
    print(dic)
    return dic.get('return')

def btn_click():
    num = textNumber.get()
    msg = textMsg.get("1.0",END)
    r= send_sms(num, msg)
    if r==r:
        showinfo("send success","successfully sent")
    else:
        showerror("error","oopssomething went wrong..")


#creating GUI
root = Tk()
root.title("Message sender")
root.geometry("400x550")
font=("helvetica", 22, "bold")

textNumber=Entry(root, font=font)
textNumber.pack(fill=X,pady=20)

textMsg=Text(root)
textMsg.pack(fill=X)

sendBtn=Button(root, text= "SEND SMS",command=btn_click)
sendBtn.pack()

root.mainloop()