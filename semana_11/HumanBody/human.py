from torso import Torso
from head import Head
from arm import Arm
from hand import Hand
from leg import Leg
from feet import Feet

class Human:
    def __init__(self):
        
        self.head = Head()
        self.right_hand = Hand()
        self.left_hand = Hand()
        self.right_arm = Arm(self.right_hand)
        self.left_arm = Arm(self.left_hand)

        self.right_feet = Feet()
        self.left_feet = Feet()
        self.right_leg = Leg(self.right_feet)
        self.left_leg = Leg(self.left_feet)

        self.torso = Torso(
            self.head,
            self.right_arm,
            self.left_arm,
            self.right_leg,
            self.left_leg
        )


