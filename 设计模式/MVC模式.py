class Model(object):
    services={'email':{'number':1000,'price':2},
              'ems':{'number':1000,'price':10},
              'voice':{'number':1000,'price':15}}

class View(object):
    def list_services(self,services):
        for scv in services:
            print(scv,' ')

    def list_pricing(self,services):
        for scv in services:
            print('For',Model.services[scv]['number'],
                  scv,'message you pay $',Model.services[scv]['price'])

class Controller(object):
    def __init__(self):
        self.model=Model()
        self.view=View()

    def get_services(self):
        services=self.model.services.keys()
        return self.view.list_services(services)
    def get_princing(self):
        services=self.model.services.keys()
        return self.view.list_pricing(services)

class Client(object):
    controller=Controller()
    print('Services provided')
    controller.get_services()
    print('Pricing for Services')
    controller.get_princing()
