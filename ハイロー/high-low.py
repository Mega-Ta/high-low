import tkinter
import random
from PIL import Image,ImageTk


trump = [[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0]]
my_num = None
my_kind = None
opp_num = None
opp_kind = None
win_cnt = 0

def btn_off():
     high_btn.configure(state="disabled")
     low_btn.configure(state="disabled")

def start_game():
     global trump, my_num, my_kind, opp_kind, opp_num, win_cnt, Tk_my_img,can_tramp_back

     my_kind, my_num = select_card()
     opp_kind, opp_num = select_card()
     
     make_high_btn()
     make_low_btn()

     global Tk_my_img, Tk_opp_img, back_img

     my_img = Image.open(f"images/tramp{my_kind}-{my_num}.png")
     my_img = my_img.resize((150,250))
     Tk_my_img = ImageTk.PhotoImage(my_img)
     

     opp_img = Image.open(f"images/tramp{opp_kind}-{opp_num}.png")
     opp_img = opp_img.resize((150,250))
     Tk_opp_img = ImageTk.PhotoImage(opp_img)

     can.create_image(1000,1000,image=Tk_back_img)
     can_tramp_back = can.create_image(750,500,image=Tk_tramp_back,tags="back")
     can.create_image(750,150,image=Tk_opp_img)
         
def select_card():
        global kind,num

        kind = random.randint(0,3)
        num = random.randint(0,12)

        while trump[kind][num] == 1:
            kind = random.randint(0,3)
            num = random.randint(0,12)
        else:
             trump[kind][num] = 1
             return kind,num

def top_game():
     global start_btn
     start_btn = tkinter.Button(can,text="Start",command=start_btn_cm,bg="white",fg="black",font=("MS明朝",18,"bold"),width=40,height=2)
     start_btn.place(x=440,y=550)

def start_btn_cm():
     start_btn.destroy()
     start_game()

def finish_game():
     if win_cnt == 0:
          create_text("0勝")
     else: 
        create_text(f"{win_cnt}連勝")

     global fin_btn

     fin_btn = tkinter.Button(can,text="Finish",command=reset_game,bg="white",fg="black",font=("MS明朝",18,"bold"),width=40,height=2)
     fin_btn.place(x=440,y=550)

def reset_game():
     global trump, my_num, my_kind, opp_kind, opp_num, win_cnt,low_btn, high_btn
     
     trump = [[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0]]
     my_num = None
     my_kind = None
     opp_num = None
     opp_kind = None
     win_cnt = 0
     can.delete("all")
     fin_btn.destroy()
     top_game()

def create_text(text):
     can.create_text(750,375,anchor="center",text=f"{text}",font=("Helbetica",250),fill="white",tags="text")

def cont_game():
     global win_cnt

     if win_cnt == 10:
          finish_game()
     else:
         start_game() 
          
        
def make_cnt_btn():
     global cnt_btn

     cnt_btn = tkinter.Button(can,text="next",command=cnt_btn_cm,bg="white",fg="black",font=("MS明朝",18,"bold"),width=15,height=2)
     cnt_btn.place(x=630,y=550)

def cnt_btn_cm():
     global cnt_btn

     can.delete("text")
     cnt_btn.destroy()
     high_btn.destroy()
     low_btn.destroy()
     cont_game()

def make_lose_btn():
     global lose_btn

     lose_btn = tkinter.Button(can,text="next",command=lose_btn_cm,bg="white",fg="black",font=("MS明朝",18,"bold"),width=15,height=2)
     lose_btn.place(x=630,y=550)

def lose_btn_cm():
     global lose_btn

     can.delete("text")
     lose_btn.destroy()
     high_btn.destroy()
     low_btn.destroy()
     finish_game()

def change_card():
     global Tk_my_img

     can.delete("back")
     can.create_image(750,500,image=Tk_my_img)

def high_judge():
     global win_cnt, my_num, opp_num
     btn_off()
     change_card()
     if my_num > opp_num:
          create_text("WIN")
          win_cnt += 1
          make_cnt_btn()

     elif my_num < opp_num:
          create_text("LOSE")
          make_lose_btn()
     else:
          create_text("DRAW")
          make_cnt_btn()
         
def low_judge():
     global win_cnt, my_num, opp_num
     btn_off()
     change_card()
     if my_num > opp_num:
          create_text("LOSE")
          make_lose_btn()
     elif my_num < opp_num:
          create_text("WIN")
          win_cnt += 1
          make_cnt_btn()
     else:
          create_text("DRAW")
          make_cnt_btn()

def make_high_btn():
     global high_btn

     high_btn = tkinter.Button(can,text="High",command=high_judge,bg="blue",fg="white",font=("MS明朝",18,"bold"),width=10,height=2)
     high_btn.place(x=830,y=640)

def make_low_btn():
     global low_btn

     low_btn = tkinter.Button(can,text="Low",command=low_judge,bg="red",fg="white",font=("MS明朝",18,"bold"),width=10,height=2)
     low_btn.place(x=515,y=640)





root = tkinter.Tk()
root.title("ハイアンドロー")
root.geometry("1500x750")
root.resizable(width=0,height=0)

back_img = Image.open("images/background.jpg")
back_img = back_img.resize((2000,2000))
Tk_back_img = ImageTk.PhotoImage(back_img)

tramp_back = Image.open("images/trampback.png")
tramp_back = tramp_back.resize((150,250))
Tk_tramp_back  = ImageTk.PhotoImage(tramp_back)

can = tkinter.Canvas(root,width=1500,height=750)
can.pack()



top_game()



root .mainloop()