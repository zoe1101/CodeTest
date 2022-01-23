
class EventManager(object): #门面
    def __init__(self):
        print('Event Manager:: let me talk to the folks\n')

    def arrange(self):
        self.hotelier=Hotelier()
        self.hotelier.bookHotel()
        self.florist=Florist()
        self.florist.setFlowerRequirements()

        self.caterer=Caterer()
        self.caterer.setCuisine()

        self.musician=Musician()
        self.musician.setMusicType()



class Hotelier(object):
    def __init__(self):
        print('为婚礼安排酒店？ --')
    def __isAvailable(self):
        print('事件当天是否有空闲的酒店？')
    def bookHotel(self):
        if self.__isAvailable():
            print('预定成功')


class Florist(object):
    def __init__(self):
        print('为事件进行花卉装饰？--')
    def setFlowerRequirements(self):
        print('玫瑰、百合将用作花卉装饰')


class Caterer(object):
    def __init__(self):
        print('为事件安排宴席？ --')
    def setCuisine(self):
        print('准备的是中餐')


class Musician(object):
    def __init__(self):
        print('播放婚礼音乐')
    def setMusicType(self):
        print('播放爵士乐')


class You(object):
    def __init__(self):
        print('准备婚礼')
    def askEventManager(self):
        print('联系婚礼准备管理人')
        em=EventManager()
        em.arrange()
    def __del__(self):
        print('婚礼筹办完毕')

if __name__ == '__main__':
    you=You()
    you.askEventManager()