from tkinter import *
import random as r

tk = Tk()
tk.title("교실 자리 배치")
tk.geometry("800x600")
tk.config(bg='white')

excluded = set()
candidate_buttons = []
seat_buttons = []
selected = []

def toggle_exclude(num, button):
    if num in excluded:
        excluded.remove(num)
        button.config(bg='lightgray')
    else:
        excluded.add(num)
        button.config(bg='red')

def generate_candidate_buttons():
    global excluded, candidate_buttons, seat_buttons

    for widget in frame.winfo_children():
        widget.destroy()
    excluded.clear()
    candidate_buttons.clear()
    seat_buttons.clear()

    try:
        nums = int(entry1.get())
        cols = int(entry2.get())
    except ValueError:
        return

    rows = (nums + cols - 1) // cols

    for i in range(rows):
        for j in range(cols):
            idx = i * cols + j + 1
            if idx > nums:
                break
            btn = Button(frame, text='', width=5, height=2, font=('Arial', 14),
                         bg='lightgray', relief='ridge')
            btn.grid(row=i, column=j, padx=5, pady=5)
            # 여기서 b=btn, num=idx로 현재 버튼과 번호 고정
            btn.config(command=lambda b=btn, num=idx: toggle_exclude(num, b))
            candidate_buttons.append(btn)


def select_seat(i, j):
    global selected
    selected.append((i, j))
    seat_buttons[i][j].config(bg='yellow')

    if len(selected) == 2:
        i1, j1 = selected[0]
        i2, j2 = selected[1]

        temp = seat_buttons[i1][j1]['text']
        seat_buttons[i1][j1].config(text=seat_buttons[i2][j2]['text'], bg='lightblue')
        seat_buttons[i2][j2].config(text=temp, bg='lightblue')
        selected = []

def generate_seats():
    global seat_buttons, selected
    for widget in frame.winfo_children():
        widget.destroy()
    seat_buttons = []
    selected = []

    try:
        nums = int(entry1.get())
        cols = int(entry2.get())
    except ValueError:
        return

    l = [i for i in range(1, nums + 1) if i not in excluded]
    r.shuffle(l)

    rows = (len(l) + cols - 1) // cols
    seats = [[] for _ in range(rows)]

    for i, student in enumerate(l):
        row = i // cols
        seats[row].append(student)

    for i in range(rows):
        row_buttons = []
        for j in range(len(seats[i])):
            btn = Button(frame, text=str(seats[i][j]), width=5, height=2, font=('Arial', 14),
                         bg='lightblue', command=lambda i=i, j=j: select_seat(i, j))
            btn.grid(row=i, column=j, padx=5, pady=5)
            row_buttons.append(btn)
        seat_buttons.append(row_buttons)

label1 = Label(tk, text='학생 수', bg='white', fg='black', font=('Arial', 14))
label1.grid(row=0, column=0, padx=10, pady=10)
entry1 = Entry(tk, width=20, font=('Arial', 14))
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = Label(tk, text='열 수', bg='white', fg='black', font=('Arial', 14))
label2.grid(row=1, column=0, padx=10, pady=10)
entry2 = Entry(tk, width=20, font=('Arial', 14))
entry2.grid(row=1, column=1, padx=10, pady=10)

btn_generate_candidates = Button(tk, text='자리 생성', command=generate_candidate_buttons, font=('Arial', 12))
btn_generate_candidates.grid(row=1, column=2, padx=10, pady=10)

btn_generate_seats = Button(tk, text='자리 배치', command=generate_seats, font=('Arial', 12))
btn_generate_seats.grid(row=2, column=2, padx=10, pady=10)

frame = Frame(tk, bg='white')
frame.grid(row=4, column=0, columnspan=3)

tk.mainloop()
