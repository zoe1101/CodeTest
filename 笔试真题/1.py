import sys

if __name__ == "__main__":
    for num in sys.stdin:
        try:
            res=[0]*4
            for i in range(4):
                res[i]=(int(num[i])+5)%10
            for i in range(2):
                res[i],res[-i-1]=str(res[-i-1]),str(res[i])
            print(''.join(res))
        except:
            print('输入的非四位数字，请重新输入！')