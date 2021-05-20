#function 函式/功能

#fuction是用來{收納}程式碼
#他是個功能

def wash(dry):
    print("加水")
    print("加洗衣精")
    print("旋轉")
    if dry:
        print("烘衣")

wash(False)


def p(x=0,y=3):
    print(x+y)

p(y=100)

def average(numbers):
    return sum(numbers) / len(numbers)

print(average([1,2,3,4,5]))
print(average([23,244,54]))