from tkinter import *
from customtkinter import *
from PIL import Image
import random

c_score=0
y_score=0
set_default_color_theme("green")
root=CTk()
root.title("Rock Paper Scissor")
img=CTkImage(Image.open("images\icon.png"),size=(60,60))
l=CTkLabel(root,text="Rock Paper Scissor",image=img,compound=TOP,font=("times new roman",32))
l.pack(padx=10,pady=10)

game_frame=CTkFrame(root)
game_frame.pack(padx=10,pady=10)

computer_choice=random.randint(1,3)
You=CTkFrame(game_frame)
You.grid(row=0,column=0,padx=10,pady=10)

i=CTkImage(Image.open(r"images\rock1.png"),size=(100,100))
your_choice=CTkLabel(You,text="",image=i)
your_choice.pack()
CTkLabel(game_frame,text="You").grid(row=1,column=0)
CTkLabel(game_frame,text="Computer").grid(row=1,column=1)

computer=CTkFrame(game_frame,corner_radius=5)
computer.grid(row=0,column=1,padx=10,pady=10)
i=CTkImage(Image.open(r"images\rock2.png"),size=(100,100))
computer_choice=CTkLabel(computer,text="",image=i)
computer_choice.pack()


play_frame=CTkFrame(root)
play_frame.pack(padx=10,pady=10)

score=CTkLabel(root,text=f"you: {y_score}\ncomputer: {c_score}")
score.pack(padx=10,pady=10)
def update():
    score.configure(text=f"you:{y_score}\ncomputer:{c_score}")
def generate_choice():
    c=random.randint(1,3)
    match c:
        case 1:
            return "rock"
        case 2:
            return "paper"
        case 3:
            return "scissors"

def Rock():
    computer.configure(fg_color="transparent")
    You.configure(fg_color="transparent")
    x=generate_choice()
    i=CTkImage(Image.open(r"images\rock1.png"),size=(100,100))
    your_choice.configure(image=i)
    i=CTkImage(Image.open(f"images\{x}2.png"),size=(100,100))
    computer_choice.configure(image=i)

    match x:
        case "paper":
            
            computer.configure(fg_color="dark cyan")
            You.configure(fg_color="transparent")
            global c_score
            c_score+=1
        
        case "scissors":
            
            computer.configure(fg_color="transparent")
            You.configure(fg_color="dark cyan")
            global y_score
            y_score+=1
        
        case "rock":
            
            computer.configure(fg_color="transparent")
            You.configure(fg_color="transparent")
    update()
        

    pass
img=CTkImage(Image.open(r"images\rock.png"),size=(30,30))
rock=CTkButton(play_frame,text="Rock",image=img,fg_color="transparent",width=40,cursor="hand2",command=Rock)
rock.grid(row=0,column=0,padx=10,pady=10)

def Paper():
    computer.configure(fg_color="transparent")
    You.configure(fg_color="transparent")
    x=generate_choice()
    i=CTkImage(Image.open(r"images\paper1.png"),size=(100,100))
    your_choice.configure(image=i)
    i=CTkImage(Image.open(f"images\{x}2.png"),size=(100,100))
    computer_choice.configure(image=i)

    match x:
        case "paper":
            
            computer.configure(fg_color="transparent")
            You.configure(fg_color="transparent")
            # global c_score
            # c_score+=1
        
        case "scissors":
            
            computer.configure(fg_color="dark cyan")
            You.configure(fg_color="transparent")
            global c_score
            c_score+=1
        
        case "rock":
            
            computer.configure(fg_color="transparent")
            You.configure(fg_color="dark cyan")
            global y_score
            y_score+=1
    update()
    pass
img=CTkImage(Image.open(r"images\paper.png"),size=(30,30))
paper=CTkButton(play_frame,text="paper",image=img,fg_color="transparent",width=40,cursor="hand2",command=Paper)
paper.grid(row=0,column=1,padx=10,pady=10)

def Scissors():
    computer.configure(fg_color="transparent")
    You.configure(fg_color="transparent")
    x=generate_choice()
    i=CTkImage(Image.open(r"images\scissors1.png"),size=(100,100))
    your_choice.configure(image=i)
    i=CTkImage(Image.open(f"images\{x}2.png"),size=(100,100))
    computer_choice.configure(image=i)

    match x:
        case "paper":
            
            computer.configure(fg_color="transparent")
            You.configure(fg_color="dark cyan")
            global y_score
            y_score+=1
        
        case "scissors":
            
            computer.configure(fg_color="transparent")
            You.configure(fg_color="transparent")
            # global c_score
            # c_score+=1
        
        case "rock":
            
            computer.configure(fg_color="dark cyan")
            You.configure(fg_color="transparent")
            global c_score
            c_score+=1
    update()
    pass

img=CTkImage(Image.open(r"images\scissors.png"),size=(30,30))
scissors=CTkButton(play_frame,text="scissors",image=img,fg_color="transparent",width=40,cursor="hand2",command=Scissors)
scissors.grid(row=0,column=2,padx=10,pady=10)


# CTkLabel(play_frame,text="Your Choice").grid(row=1,column=1)
root.mainloop()