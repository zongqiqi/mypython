
### 列表推导
# list1=[i for i in range(10) if i%2==0]
# print(list1)

# seq=["one","two","three"]
# for i,element in enumerate(seq):
#     seq[i]="%d:%s"%(i,seq[i])
# print(seq)


### 迭代器
# i=iter("abc")
# print(i.__next__())

# def fibonacci():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# fib=fibonacci()
# print(fib.__next__())
# print(fib.__next__())
# print(fib.__next__())
# print(fib.__next__())
# print(fib.__next__())
# print(fib.__next__())
# list2=[fib.__next__() for i in range(10) ]
# print(list2)

def psychologist():
    print("Please tell your problems")
    while True:
        answer=(yield)
        if answer is not None:
            if answer.endwith('?'):
                print("Don't ask yourself")