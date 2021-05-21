data = []
count = 0
sum = 0
with open ("reviews.txt" , "r" , encoding="utf-8" ) as f:
    for line in f:
        
        data.append(line)

    for number in data:
        sum+=len(number)
    print("每筆留言平均數為",sum/len(data))
        
    print("總共有",len(data),"筆資料")

print(data[0])

#文字記數

wc = {} # word_count
for d in data :
    words = d.split()
    
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1   #新增新的key進wc字典

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])
    
    
print(len(wc))
print(wc["Allen"])

while True :
    word = input("請問你想查什麼字: ")
    if word == "q":
        print("感謝使用")
        break
    if word in wc:
        print(word , "出現過的次數為" , wc[word])
    else:
        print("沒有出現過喔")
new=[]
for d in data:
    if len(d) < 100:
        new.append(d)
print("留言長度小於100一共有",len(new),"筆")
print(new[10])

good=[]
for d in data:
    if "good" in d:
        good.append(d)
print("有包含good的留言一共有",len(good),"筆")

#快選法 
good = [d for d in data if "good" in d]
print("有包含good的留言一共有",len(good),"筆") 