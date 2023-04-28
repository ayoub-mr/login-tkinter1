from tkinter import *
from PIL import ImageTk
def singup():
    Login_window.destroy()
    import signup
def user_enter(event):
    if Username.get()=='Username':
        Username.delete(0,END)
def pass_enter(event):
    if Password.get()=='Password':
        Password.delete(0,END)
Login_window=Tk()
Login_window.geometry('990x660+50+50')
Login_window.resizable(0,0)
Login_window.title('Login')
bgImage=ImageTk.PhotoImage(file='bg.jpg')
bglabel=Label(Login_window,image=bgImage)
bglabel.place(x=0,y=0)
heading=Label(Login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold'),bg='#C7B7D2',fg='#6F448E')
heading.place(x=430,y=100)
Username=Entry(Login_window,width=25,font=('Microsoft Yahei UI Light',15,'bold'),bd=0,fg='#6F448E',bg='#C3C3C3')
Username.place(x=400,y=200)
Username.insert(0,'Username')
Username.bind('<FocusIn>',user_enter)
frame1=Frame(Login_window,width=250,height=2,bg='#6F448E')
frame1.place(x=420,y=228)

Password=Entry(Login_window,width=25,show="*",font=('Microsoft Yahei UI Light',15,'bold'),bd=0,fg='#6F448E',bg='#C3C3C3')
Password.place(x=400,y=260)
Password.insert(0,'Password')
Password.bind('<FocusIn>',pass_enter)
frame2=Frame(Login_window,width=250,height=2,bg='#6F448E')
frame2.place(x=420,y=288)
forgetButton=Button(Login_window,text='Forgot password',bd=0,bg='#D0DAE2',activebackground='#C3C2C3',cursor='hand2' )
forgetButton.place(x=600,y=295)
loginbutton=Button(Login_window,text='Login',font=( 'Onen Sans',16,'bold') ,fg='white',bg='#864893',activebackground='#C3C2C3',cursor='hand2',bd=0,width=23)
loginbutton.place(x=397,y=328)
signupLabel=Label(Login_window,text='Dont have an account?',font=( 'Onen Sans',7,'bold') ,fg='#6F448E',bg='#D0DAE2')
signupLabel.place(x=600,y=370) 
singupbutton=Button(Login_window,text='Creat New One',font=( 'Onen Sans',7,'bold underline') ,fg='blue',bg='#C3C3C3',activeforeground='blue',cursor='hand2',bd=0,width=23,command=singup)
singupbutton.place(x=580,y=390)
Login_window.mainloop()