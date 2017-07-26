"""数字比较。"""
if __name__=="__main__":
    mark = 1
    while mark:
        try:
            number1 = int(input("Please input first digit"))
            number2 = int(input("Second one"))
            mark = 0
        except:
            print("worry input")
    if number1>number2:
        print ("first(%d)is bigger then second(%d)"%(number1,number2))
    if number1<number2:
        print("first(%d)is smaller then second(%d)"%(number1,number2))
    if number1==number2:
        print ("they are equal")


