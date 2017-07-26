"""一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。"""

n = input("number \n")
for a in range(1,len(n)):
    if n[a-1]!=n[-a]:
        print('不是回文数')
        break
    if a+1 == len(n) and n[a-1] == n[-a]:
        print('回文数')


