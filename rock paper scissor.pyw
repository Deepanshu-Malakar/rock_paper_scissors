from tkinter import *
from customtkinter import *
from PIL import Image
import random
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
CTkLabel(game_frame,text="You").grid(row=1,column=0)
CTkLabel(game_frame,text="Computer").grid(row=1,column=1)
computer=CTkFrame(game_frame)
computer.grid(row=0,column=1,padx=10,pady=10)


play_frame=CTkFrame(root)
play_frame.pack(padx=10,pady=10)
img=CTkImage(Image.open(r"images\rock.png"),size=(30,30))
rock=CTkButton(play_frame,text="Rock",image=img,fg_color="transparent",width=40,cursor="hand2")
rock.grid(row=0,column=0,padx=10,pady=10)
img=CTkImage(Image.open(r"images\paper.png"),size=(30,30))
paper=CTkButton(play_frame,text="paper",image=img,fg_color="transparent",width=40,cursor="hand2")
paper.grid(row=0,column=1,padx=10,pady=10)
img=CTkImage(Image.open(r"images\scissors.png"),size=(30,30))
scissors=CTkButton(play_frame,text="scissors",image=img,fg_color="transparent",width=40,cursor="hand2")
scissors.grid(row=0,column=2,padx=10,pady=10)
# CTkLabel(play_frame,text="Your Choice").grid(row=1,column=1)
root.mainloop()