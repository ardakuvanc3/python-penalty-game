import random
import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Penaltı Oyunu")
root.configure(background="SpringGreen3")

photo = tk.PhotoImage(file="soccer-ball.png")
root.wm_iconphoto(False, photo)

header = tk.Label(root, text="Penaltı Oyunu", font="Bold",background="SpringGreen3")
header.pack()

score = 0

score_label = tk.Label(root, text="Skor: " + str(score), background="SpringGreen3", font="Bold")
score_label.place(x=400, y=10)

result_label = tk.Label(root, text="",background="SpringGreen3")
result_label.place(x=140,y=100)

def ballfunc(result):
    global score
    
    ai_quest = random.randint(0, 2)
    
    if ai_quest == result:
        result_label.config(text="GOOOOLL!", background="SpringGreen3", font=("Arial",25, "bold"))
        score += 1
    else:
        result_label.config(text="Başarısız Atış!",font=("Arial", 25, "bold"),background="SpringGreen3")
    
    score_label.config(text="Skor: " + str(score))

def left_kick():
    result_label.config(text="")
    ballfunc(0)

def middle_kick():
    result_label.config(text="")
    ballfunc(1)

def right_kick():
    result_label.config(text="")
    ballfunc(2)

left_btn = tk.Button(root, text="Sola", command=left_kick, font="Bold",height= 2, width=7)
left_btn.place(x=20, y=200)

middle_btn = tk.Button(root, text="Ortaya At", command=middle_kick,font="Bold",height= 2, width=9)
middle_btn.place(x=200, y=200)

right_btn = tk.Button(root, text="Sağa At", command=right_kick,font="Bold",height= 2, width=7)
right_btn.place(x=400, y=200)

root.mainloop()
