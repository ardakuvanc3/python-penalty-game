import random
import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Penaltı Oyunu")

photo = tk.PhotoImage(file="soccer-ball.png")
root.wm_iconphoto(False, photo)

header = tk.Label(root, text="Penaltı Oyunu", font="Bold")
header.pack()

score = 0

score_label = tk.Label(root, text="Skor: " + str(score))
score_label.place(x=400, y=10)

result_label = tk.Label(root, text="")
result_label.pack()

def ballfunc(result):
    global score
    
    ai_quest = random.randint(0, 2)
    
    if ai_quest == result:
        result_label.config(text="GOOOOLL!")
        score += 1
    else:
        result_label.config(text="Başarısız Atış!")
    
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

left_btn = tk.Button(root, text="Sola", command=left_kick)
left_btn.pack()

middle_btn = tk.Button(root, text="Ortaya At", command=middle_kick)
middle_btn.pack()

right_btn = tk.Button(root, text="Sağa At", command=right_kick)
right_btn.pack()

root.mainloop()
