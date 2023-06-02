# life cycle of butterfly
class Egg:
    def first(self):
        print("I am the Egg")
class Caterpillar(Egg):
    def second(self):
        print("I am the Caterpillar")
class Pupa(Caterpillar):
    def third(self):
        print("I am the Pupa")
class Butterfly(Pupa):
    def fourth(self):
        print("I am the Butterfly")
        print("WoW! I am flying")
# main function
print("Life cycle of Butterfly-->")
butterfly=Butterfly()
# print("First stage-->{Egg}, Second stage-->{Caterpillar}, Third stage-->{Pupa}, Fourth stage-->{Butterfly}")
butterfly.first()
butterfly.second()
butterfly.third()
butterfly.fourth()
    