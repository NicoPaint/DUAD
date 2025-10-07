class Head:
    def __init__(self):
        pass

class Torso:
    def __init__(self):
        pass

class Hand:
    def __init__(self):
        pass

class Feet:
    def __init__(self):
        pass

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Leg:
    def __init__(self, feet):
        self.feet = feet

class Human:
    def __init__(self, head, torso, left_arm, right_arm, left_leg, right_leg):
        self.head = head
        self.torso = torso
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg

my_head = Head()
my_torso = Torso()
my_left_hand = Hand()
my_right_hand = Hand()
my_left_arm = Arm(my_left_hand)
my_right_arm = Arm(my_right_hand)
my_left_foot = Feet()
my_right_foot = Feet()
my_left_leg = Leg(my_left_foot)
my_right_leg = Leg(my_right_foot)

me = Human(my_head, my_torso, my_left_arm, my_right_arm, my_left_leg, my_right_leg)