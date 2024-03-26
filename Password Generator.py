from tkinter import *
import string
import random
import pyperclip

def generator():
    small_alpha=string.ascii_lowercase
    cap_alpha=string.ascii_uppercase
    num=string.digits
    char=string.punctuation

    med=small_alpha+cap_alpha+num
    all=small_alpha+cap_alpha+num+char
    password_len=int(length_Box.get())

    if choice.get()==1:
        passField.insert(0, random.sample(small_alpha+cap_alpha,password_len))
    

    if choice.get()==2:
        passField.insert(0, random.sample(med,password_len))
    

    if choice.get()==3:
        passField.insert(0, random.sample(all,password_len))
    
    # password=random.sample(all, password_len)
    # passField.insert(0,password)


def copy():
    pass_store=passField.get()
    pyperclip.copy(pass_store)




root =Tk()
root.config(bg='gray20')

choice=IntVar()
Font=('arial', 13, 'bold')

passwordLabel1=Label(root, text='Joyboys Password Generator',font=('times new roman', 20,'bold'), bg='gray20',fg='white')
passwordLabel1.grid(pady=10)

weakradioButton=Radiobutton(root,text='Weak',value=1, variable=choice, font=Font)
weakradioButton.grid(pady=10)

mediumradioButton=Radiobutton(root,text='Medium',value=2, variable=choice, font=Font)
mediumradioButton.grid(pady=10)

strongradioButton=Radiobutton(root,text='Strong',value=3, variable=choice, font=Font)
strongradioButton.grid(pady=10)

lengthLabel=Label(root, text='Password Length', font = Font, bg='gray20', fg='white')
lengthLabel.grid(pady=10)

length_Box=Spinbox(root, from_=5, to_=18, width=5, font=Font)
length_Box.grid(pady=10)

btnGenerate=Button(root, text='Generate', font=Font, command=generator)
btnGenerate.grid(pady=10)

passField=Entry(root, width=25, bd=2, font=Font)
passField.grid(pady=10)

btnCopy=Button(root, text='Copy', font=Font, command=copy)
btnCopy.grid(pady=10)

root.mainloop()