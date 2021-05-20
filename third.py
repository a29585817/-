import random
start=input("請決定隨機數字範圍開始值:")
end=input("請決定隨機數字範圍結束值:")
start=int(start)
end=int(end)
r = random.randint(start,end)
count=0


while True:
    count += 1
    answer = input("請猜數字:")
    answer = int(answer)
    if answer == r:
        print("恭喜尼答對了")
        break
    elif answer>r:
        print("在猜小一點")
    elif answer<r:
        print("在猜大一點")
    print("這是你猜的第" , count , "次")