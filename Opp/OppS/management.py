class Company:
    def __init__(self,name,address) -> None:
        self.name=name
        self.bus=[]
        self.routes=[]
        self.drivers=[]
        self.counter=[]
        self.supervisor=[]

class Driver:
    def __init__(self,name,license,age) -> None:
        self.name=name
        self.license=license
        self.age=age