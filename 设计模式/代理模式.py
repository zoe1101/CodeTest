class Actor(object):
    def __init__(self):
        self.isBusy=False
    def occupied(self):
        self.isBusy=True
        print(type(self).__name__,'正在忙着拍电影')
    def available(self):
        self.isBusy=False
        print(type(self).__name__,'电影已经拍完了，已经闲了')
    def getStatus(self):
        return self.isBusy


class Agent(object):
    def __init__(self):
        self.principal=None
    def work(self):
        self.actor=Actor()
        if self.actor.getStatus():
            self.actor.occupied()
        else:
            self.actor.available()

if __name__ == '__main__':
    r=Agent()
    r.work()
    r.actor.isBusy=True
    r.work()