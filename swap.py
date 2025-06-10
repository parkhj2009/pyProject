# 교실 자리 뽑기 프로그램
import random
import time

print("\n교실 자리 뽑기 프로그램\n" + "="*20)
while True:
    line = input("교실 세로 줄 수를 입력하세요 (4 또는 5): ")
    if line in ("4", "5"):
        line = int(line)
        break
    print("올바르지 않습니다. 다시 입력하세요.\n")
while True:
    number = input("학급 전체 인원을 입력하세요 (최대 50명): ")
    if number.isdigit() and 1 <= int(number) <= 50:
        number = int(number)
        break
    print("올바르지 않습니다. 다시 입력하세요.\n")
while True:
    confirm = input(f"{number}명, {line}줄로 시작할까요? (Y/N): ").lower()
    if confirm == "y":
        print("\n============ 교탁 ============\n")
        seats = list(range(1, number + 1))
        random.shuffle(seats)
        for i, seat in enumerate(seats, 1):
            print(f"{seat:<4}", end=" ")
            if i % line == 0:
                time.sleep(1)
                print()
        print("\n")
    elif confirm == "n":
        print("프로그램을 종료합니다.")
        break
    else:
        print("Y 또는 N으로 입력해주세요.")
        continue
    again = input("다시 뽑을까요? (Y/N): ").lower()
    if again != "y":
        print("프로그램을 종료합니다.")
        break