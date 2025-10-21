# #1
# class person:
#     def __init__(self,ism,yosh):
#         self.ism = ism
#         self.yosh = yosh
#     def greet(self):
#         return f"Salom {self.ism},yoshingiz {self.yosh}"
# isim=input("Ismingizni kiriting: ")
# me=person(isim)
# print(me.greet())
# #2
# class person:
#     ism="Muhammad ali"
#     def __init__(self,ism="Muhammad ali"):
#         self.ism = ism
#     def personn(self):
#         return f"Salom {self.ism}"
# me=person()
# print(me.personn())
# #3
# class student:
#     def __init__(self, ism):
#         self.ism = ism
#     def hello(self,name="Foydalanuvchi"):
#         return f"Salom {name}"
# me = student("Muhammad ali")
# print(me.hello())
# #4
# class metob:
#     def __init__(self,eskibaho):
#         self.baho = eskibaho
#     def metod(self,yangibaho):
#         self.baho = yangibaho
#         print(f"{self.baho} qo`yildi!")
# math =metob(3)
# print(f"Eski baho: {math.baho}")
# math.metod(5)
# # 5.Bir nechta obyekt yaratib, ularning metodlarini chaqirish.
# class Car:
#     def __init__(self, model):
#         self.model = model
#     def start(self):
#         print(f"{self.model} ishga tushdi!")
# car1 = Car("Cobalt")
# car2 = Car("Malibu")
# car1.start()
# car2.start()