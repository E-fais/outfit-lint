import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import ImageTk,Image
from colors import dress_colors

root = ttk.Window(themename="solar")
root.geometry('400x600')
root.title('OutfitTint')
root.iconbitmap('./images/logo.ico')

colors=list(dress_colors.keys())

#show matches in new windwo

def open_new_window(user_choice):
    top=tk.Toplevel(root)
    top.title('OutfitTint')
    top.iconbitmap('./images/logo.ico')
    top.geometry('400x200')
    

    choice_color=ttk.Label(top,font=('helvetica,16'),text=f"Colors that match well with {user_choice.upper()} are :",padding=(20,10),)
    matches=dress_colors[user_choice]
    
    match_str=''
    for match in matches:
      match_str+=f" {match},"
      
    matching_colors=ttk.Label(top,text=match_str,font=('helvetica,16'))
    back_btn=ttk.Button(top,text='Close',command=top.destroy,width=20,bootstyle='success')

    choice_color.grid(row=0,padx=20)
    matching_colors.grid(row=1,padx=20)
    back_btn.grid(row=2,column=0,pady=20)
    

#create frame
frame=tk.LabelFrame(root,padx=40,pady=10) 



frame.pack(padx=20,pady=60)

#hero banner
#open image
hero_img=Image.open("./images/hero.jpg")
#resize image
resized_hero_img=hero_img.resize((220,300))
#create pillow image for resized
new_hero=ImageTk.PhotoImage(resized_hero_img)


#color drop down menu
def get_match():
    user_inp=user_selection.get()
    open_new_window(user_inp)

user_selection=ttk.StringVar()
drop_colors=ttk.Combobox(frame,values=colors,textvariable=user_selection)
drop_colors.set(colors[0])

match_button=ttk.Button(frame,text='Go!',width=20,bootstyle='success',command=get_match)




ttk.Label(frame,text='Outfit Tint',font=("Helvetica", 20),bootstyle='success').grid(row=0,column=0)
ttk.Label(frame,image=new_hero).grid(row=1,column=0,pady=10)
ttk.Label(frame,text='Choose color to match:',font=('helvetica',10),).grid(row=2,column=0)
drop_colors.grid(row=3, pady=3, column=0)  
match_button.grid(row=4,  column=0,columnspan=3,pady=3,padx=30) 




root.mainloop()
