from tkinter import *
import random as r

def get():
    nums = entry1.get()
    rows = entry2.get()
    ext = entry3.get()
    print(nums)
    print(rows)
    chose(nums, rows)

def chose(nums, rows,ext):
    nums = int(nums)
    rows = int(rows)
    ext = ext.split(',')
    l = [i for i in range(1,nums+1)]
    seats=[[] for _ in range(rows)]
    r.shuffle(l)
    print(l)
    for i in range(rows):
        for j in range(nums // rows):
            seats[i].append(l.pop())
    print(seats)        


tk = Tk() 
tk.title("교실 자리 뽑기 프로그램")
tk.geometry("600x400")  # 창 크기 설정
tk.resizable(True, True)
tk.config(padx=10, pady=10, bg='white')

# 학생 수 라벨 (Entry 왼쪽, row=0, column=0)
label1 = Label(tk, text='학생 수', bg='white', fg='black', font=('Arial', 14))
label1.grid(row=0, column=0, padx=10, pady=10)


# Entry (row=0, column=1)
entry1 = Entry(tk, width=30, bg='white', fg='black', font=('Arial', 14))
entry1.grid(row=0, column=1, padx=10, pady=10)


label2 = Label(tk, text='열 수', bg='white', fg='black', font=('Arial', 14))
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = Entry(tk, width=30, bg='white', fg='black', font=('Arial', 14))
entry2.grid(row=1, column=1, padx=10, pady=10)

label3 = Label(tk, text='제외할 번호(쉼표로 구분)', bg='white', fg='black', font=('Arial', 14))
label3.grid(row=1, column=0, padx=10, pady=10)

entry3 = Entry(tk, width=30, bg='white', fg='black', font=('Arial', 14))
entry3.grid(row=1, column=1, padx=10, pady=10)

btn = Button(tk, text='확정', command=get)
btn.grid(row=0, column=2, padx=10, pady=10)



tk.mainloop()
