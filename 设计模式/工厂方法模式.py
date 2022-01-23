from abc import ABCMeta,abstractmethod

class Section(metaclass=ABCMeta): #抽象产品
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):#具体产品
    def describe(self):
        print('Personal Section')

class AlbumSection(Section): #具体产品
    def describe(self):
        print('Album Section')

class PatentSection(Section): #具体产品
    def describe(self):
        print('Patent Section')

class PublicationSection(Section): #具体产品
    def describe(self):
        print('Publication Section')

class Profile(metaclass=ABCMeta): #抽象工厂
    def __init__(self):
        self.sections=[]
        self.createProfile()
    @abstractmethod
    def createProfile(self):
        pass
    def getSections(self):
        return self.sections
    def addSctions(self,section):
        self.sections.append(section)

class linkedin(Profile): #具体工厂
    def createProfile(self):
        self.addSctions(PersonalSection())
        self.addSctions(PatentSection())
        self.addSctions(PublicationSection())

class facebook(Profile): #具体工厂
    def createProfile(self):
        self.addSctions(PersonalSection())
        self.addSctions(AlbumSection())

if __name__ == '__main__':
    profile_type=input('which profile you would like to create? [Linkedin or FaceBook]')
    profile=eval(profile_type.lower())()
    print('Creatinf profile..',type(profile).__name__)
    print('profile has sections：',profile.getSections())