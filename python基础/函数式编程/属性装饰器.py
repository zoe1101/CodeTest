'''
请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
'''


class Screen(object) :
    @property
    def width(self) :
        return self._width

    @width.setter
    def width(self,valuer) :
        if not isinstance(valuer,int):
            raise ValueError('score must be an integer')
        if valuer < 0 :
            raise ValueError('score must over zero')
        self._width=valuer

    @property
    def height(self) :
        return self._height

    @height.setter
    def height(self,number) :
        if not isinstance(number,int) :
            raise ValueError('score must be an integer')
        if number < 0 :
            raise ValueError('score must be an zero')
        self._height = number

    @property
    def resolution(self):
        return self._width * self._height

if __name__ == '__main__':
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('测试通过!')
    else:
        print('测试失败!')
