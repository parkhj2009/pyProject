# from tkinter import *
# import random as r

# def get():
#     # 기존 위젯의 배치 결과 제거
#     for widget in frame.winfo_children():
#         widget.destroy()

#     nums = entry1.get()
#     rows = entry2.get()
#     try:
#         ext = list(map(int, entry3.get().split(','))) if entry3.get().strip() else []
#     except ValueError:
#         ext = []
    
#     chose(nums, rows, ext)

# def chose(nums, rows, ext):
#     nums = int(nums)
#     rows = int(rows)
#     l = [i for i in range(1, nums + 1) if i not in ext]
#     r.shuffle(l)

#     cols = (len(l) + rows - 1) // rows  # 열 수 자동 계산
#     seats = [[] for _ in range(rows)]

#     for i, student in enumerate(l):
#         seats[i % rows].append(student)

#     # GUI로 결과 출력
#     for i in range(rows):
#         for j in range(len(seats[i])):
#             Label(frame, text=str(seats[i][j]), width=5, height=2, font=('Arial', 14),
#                   relief='solid', bg='lightblue').grid(row=i, column=j, padx=5, pady=5)

# # Tkinter 윈도우 생성
# tk = Tk()
# tk.title("교실 자리 뽑기 프로그램")
# tk.geometry("800x600")
# tk.resizable(True, True)
# tk.config(padx=10, pady=10, bg='white')

# # 입력 UI
# label1 = Label(tk, text='학생 수', bg='white', fg='black', font=('Arial', 14))
# label1.grid(row=0, column=0, padx=10, pady=10)
# entry1 = Entry(tk, width=20, font=('Arial', 14))
# entry1.grid(row=0, column=1, padx=10, pady=10)

# label2 = Label(tk, text='행 수', bg='white', fg='black', font=('Arial', 14))
# label2.grid(row=1, column=0, padx=10, pady=10)
# entry2 = Entry(tk, width=20, font=('Arial', 14))
# entry2.grid(row=1, column=1, padx=10, pady=10)

# label3 = Label(tk, text='제외할 번호 (쉼표로 구분)', bg='white', fg='black', font=('Arial', 14))
# label3.grid(row=2, column=0, padx=10, pady=10)
# entry3 = Entry(tk, width=20, font=('Arial', 14))
# entry3.grid(row=2, column=1, padx=10, pady=10)

# btn = Button(tk, text='자리 배치', command=get, font=('Arial', 12))
# btn.grid(row=2, column=2, padx=10, pady=10)

# # 자리 배치 결과 출력 프레임
# frame = Frame(tk, bg='white')
# frame.grid(row=3, column=0, columnspan=3, pady=20)

# tk.mainloop()

# from tkinter import *
# import random as r

# tk = Tk()
# tk.title("교실 자리 배치")
# tk.geometry("800x600")
# tk.config(bg='white')

# # 상태 저장용
# seat_buttons = []
# selected = []

# # 선택/스왑 함수
# def select_seat(i, j):
#     global selected
#     selected.append((i, j))

#     # 시각적 피드백
#     seat_buttons[i][j].config(bg='yellow')

#     if len(selected) == 2:
#         i1, j1 = selected[0]
#         i2, j2 = selected[1]
        
#         # 스왑
#         temp = seat_buttons[i1][j1]['text']
#         seat_buttons[i1][j1].config(text=seat_buttons[i2][j2]['text'], bg='lightblue')
#         seat_buttons[i2][j2].config(text=temp, bg='lightblue')
        
#         selected = []

# # 자리 생성 함수
# def generate_seats():
#     global seat_buttons, selected
#     for widget in frame.winfo_children():
#         widget.destroy()
#     seat_buttons = []
#     selected = []

#     nums = int(entry1.get())
#     rows = int(entry2.get())
#     try:
#         ext = list(map(int, entry3.get().split(','))) if entry3.get().strip() else []
#     except ValueError:
#         ext = []

#     l = [i for i in range(1, nums + 1) if i not in ext]
#     r.shuffle(l)

#     cols = int(entry2.get())  # entry2 값을 열 수로 간주
#     rows = (len(l) + cols - 1) // cols  # 자동으로 행 수 계산
#     seats = [[] for _ in range(rows)]

#     for i, student in enumerate(l):
#         row = i // cols
#         seats[row].append(student)


#     # 버튼 생성
#     for i in range(rows):
#         row_buttons = []
#         for j in range(len(seats[i])):
#             btn = Button(frame, text=str(seats[i][j]), width=5, height=2, font=('Arial', 14),
#                          bg='lightblue', command=lambda i=i, j=j: select_seat(i, j))
#             btn.grid(row=i, column=j, padx=5, pady=5)
#             row_buttons.append(btn)
#         seat_buttons.append(row_buttons)

# # 입력 UI
# label1 = Label(tk, text='학생 수', bg='white', fg='black', font=('Arial', 14))
# label1.grid(row=0, column=0, padx=10, pady=10)
# entry1 = Entry(tk, width=20, font=('Arial', 14))
# entry1.grid(row=0, column=1, padx=10, pady=10)

# label2 = Label(tk, text='열 수', bg='white', fg='black', font=('Arial', 14))
# label2.grid(row=1, column=0, padx=10, pady=10)
# entry2 = Entry(tk, width=20, font=('Arial', 14))
# entry2.grid(row=1, column=1, padx=10, pady=10)

# label3 = Label(tk, text='제외할 번호 (쉼표로 구분)', bg='white', fg='black', font=('Arial', 14))
# label3.grid(row=2, column=0, padx=10, pady=10)
# entry3 = Entry(tk, width=20, font=('Arial', 14))
# entry3.grid(row=2, column=1, padx=10, pady=10)

# btn = Button(tk, text='자리 배치', command=generate_seats, font=('Arial', 12))
# btn.grid(row=2, column=2, padx=10, pady=10)

# btn = Button(tk, text='자리 생성', command=generate_seats, font=('Arial', 12))
# btn.grid(row=1, column=2, padx=10, pady=10)

# frame = Frame(tk, bg='white')
# frame.grid(row=4, column=0, columnspan=2)

# tk.mainloop()

from tkinter import *
import random as r

tk = Tk()
tk.title("교실 자리 배치")
tk.geometry("800x600")
tk.config(bg='white')

seat_buttons = []
selected = []
excluded = set()
candidate_buttons = []

# 자리 선택 후 스왑
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

# 제외 버튼 토글
def toggle_exclude(n, btn):
    if n in excluded:
        excluded.remove(n)
        btn.config(bg='SystemButtonFace')
    else:
        excluded.add(n)
        btn.config(bg='red')

# 후보 번호 버튼 생성
def generate_candidate_buttons():
    global excluded, candidate_buttons
    for widget in frame.winfo_children():
        widget.destroy()
    excluded = set()
    candidate_buttons = []

    try:
        nums = int(entry1.get())
    except ValueError:
        return

    rows = (nums + 9) // 10
    for i in range(nums):
        n = i + 1
        btn = Button(frame, text=str(n), width=5, height=2, font=('Arial', 12),
                     command=lambda n=n, b=None: None)  # 미리 생성 방지용
        btn.config(command=lambda n=n, b=btn: toggle_exclude(n, b))
        btn.grid(row=i // 10, column=i % 10, padx=3, pady=3)
        candidate_buttons.append(btn)

# 좌석 배치 생성
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

# 입력 UI
label1 = Label(tk, text='학생 수', bg='white', fg='black', font=('Arial', 14))
label1.grid(row=0, column=0, padx=10, pady=10)
entry1 = Entry(tk, width=20, font=('Arial', 14))
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = Label(tk, text='열 수', bg='white', fg='black', font=('Arial', 14))
label2.grid(row=1, column=0, padx=10, pady=10)
entry2 = Entry(tk, width=20, font=('Arial', 14))
entry2.grid(row=1, column=1, padx=10, pady=10)

label3 = Label(tk, text='제외할 번호 (쉼표로 구분)', bg='white', fg='black', font=('Arial', 14))
label3.grid(row=2, column=0, padx=10, pady=10)
entry3 = Entry(tk, width=20, font=('Arial', 14))
entry3.grid(row=2, column=1, padx=10, pady=10)

btn1 = Button(tk, text='자리 배치', command=generate_seats, font=('Arial', 12))
btn1.grid(row=2, column=2, padx=10, pady=10)

btn2 = Button(tk, text='자리 생성', command=generate_seats, font=('Arial', 12))
btn2.grid(row=1, column=2, padx=10, pady=10)

frame = Frame(tk, bg='white')
frame.grid(row=4, column=0, columnspan=2)

tk.mainloop()
