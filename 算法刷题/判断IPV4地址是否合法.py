# 正则表达式实现
import re


def func1(s):
    pattern=re.compile('^([1-9]\d?|1\d{2}|2[0-4]\d|25[0-5])(\.[1-9]?\d|\.1\d{2}|\.2[0-4]\d|\.25[0-5]){3}$')
    return True if pattern.match(s) else False

def func2(s):
    addr=s.split('.')
    if len(addr)!=4:
        return False
    for i in range(4):
        try:
            addr[i]=int(addr[i])
            if i==0 and addr[i]==0:
                return False
            if addr[i]>255:
                return False
        except:
            print('ipv4字符串中包含非数字字符')
            return False
        return True


def func2(s):
    import IPy  #IPy库是一个处理IP比较强大的第三方库。涉及到计算大量的IP地址，包括网段、网络掩码、广播地址、子网数、IP类型等
    try:
        IPy.IP(s)
        return True
    except:
        return False
if __name__ == '__main__':
    s='1.11.12.222'
    print(func1(s))
    print(func2(s))