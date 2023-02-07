class Robot:
    def __init__ (self, n, c, w):
        self.name = n
        self.color = c 
        self.weight = w

    def introduce_self(self):
        print("my name is " + self.name)
    
r1 = Robot("Tom", "red", 30)
r2 = Robot ("Jerry", "blue", 40)

class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False

p1 = Person("Alice", "angry", False)
 #person is new object with args
p2 = Person("Becy", "talkative", True)
# p1 own r1
p1.robot_own = r2
p2.robot_own =r1

r2.introduce_self()