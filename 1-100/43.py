"""python作用域使用方法"""

class Num:
    nNum=1
    def inc(self):
        self.nNum+=1
        print('nNum = %d'%self.nNum)
if __name__ == '__main__':
    nNum = 2
    inst =Num()
    for i in range(3):
        nNum+=2
        print ('The Num = %d'%nNum)
        inst.inc()


