class Family:
    def __init__(self,address) -> None:
        self.address=address
class School:
    def __init__(self,name,Class) -> None:
        self.name=name
        self.class_=Class
class Sports:
    def __init__(self,game) -> None:
        self.game=game

class Student(Family,School,Sports):
    def __init__(self, address,name,Class,game) -> None:
        School.__init__(self,name,Class)
        Family.__init__(self,address)
        Sports.__init__(self,game)
        