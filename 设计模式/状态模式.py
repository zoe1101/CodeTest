from abc import ABCMeta,abstractmethod
class State(metaclass=ABCMeta):
    @abstractmethod
    def doThis(self):
        pass

class StartState(State):
    def doThis(self):
        print('打开电视')

class StopState(State):
    def doThis(self):
        print('关闭电视')

class TVContext(State):
    def __init__(self):
        self.state=None

    def getState(self):
        return self.state

    def setState(self,state):
        self.state=state

    def doThis(self):
        self.state.doThis()

if __name__ == '__main__':
    context=TVContext()
    context.getState()

    start=StartState()
    stop=StopState()

    context.setState(stop)
    context.doThis()

    context.setState(start)
    context.doThis()