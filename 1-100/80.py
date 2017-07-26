"""海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？"""

num=int(input('有几只猴子'))
def fn(n):
    if n == num:
        return (4*x)
    else:
        return(fn(n+1)*5/4+1)
x=1
while 1:
    count=0
    for i in range(1,num):
        if fn(i)%4==0:
            count=count+1
    if count==num-1:
        print("海滩上原来有%d个桃子"%int(fn(0)))
        break
    else:
        x=x+1


