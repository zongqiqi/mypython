"""练习函数调用"""

def hello():
    print('Hello World')

def many():
    for a in range(3):
        hello()
many()


