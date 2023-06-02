# creational pattern
# structural pattern
# behavioral pattern

# singleton ->one single instance
# if you want a new instance of a class, you can create it

class SingleTon:
    _instance = None
    def __init__(self):
        if SingleTon._instance != None:
            raise Exception("This class is a singleton!")
        else:
            SingleTon._instance = self
    @staticmethod
    def get_instance():
        if SingleTon._instance == None:
            SingleTon()
        return SingleTon._instance
    
s1 = SingleTon.get_instance()
s2 = SingleTon.get_instance()
print(s1)
print(s2)