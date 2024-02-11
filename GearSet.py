#Python program used to Set the status and print compleate gear sets
from GearPiece import  GearPiece
#Gear slot constants
HEAD = 0
BODY = 1
HANDS = 2
LEGS = 3
FEET = 4
class GearSet:
    def __init__(self, head, body, hands, legs, feet):
        """
        Constructor for GearSet.

        Parameters:
        head (GearPiece): GearPiece object for head slot.
        body (GearPiece): GearPiece object for body slot.
        hands (GearPiece): GearPiece object for hands slot.
        legs (GearPiece): GearPiece object for legs slot.
        feet (GearPiece): GearPiece object for feet slot.
        """
        self.head = head
        self.body = body
        self.hands = hands
        self.legs = legs
        self.feet = feet

    def __str__(self):
        return (f"Head: {self.head} {self.head.status}\n"
                f"Body: {self.body} {self.body.status}\n"
                f"Hands: {self.hands} {self.hands.status}\n"
                f"Legs: {self.legs} {self.legs.status}\n"
                f"Feet: {self.feet} {self.feet.status}\n")

    #Getters for GearSet class
    def get_head(self):
        return self.head
    def get_body(self):
        return self.body
    def get_hands(self):
        return self.hands
    def get_legs(self):
        return self.legs
    def get_feet(self):
        return self.feet

    #Setters for GearSet class
    def set_head(self, head):
         self.head = head
    def set_body(self, body):
         self.body = body
    def set_hands(self, hands):
         self.hands = hands
    def set_legs(self, legs):
         self.legs =legs
    def set_feet(self, feet):
         self.feet = feet

    def update_GearSet_status(self, headStatus, bodyStatus, handsStatus, legsStatus, feetStatus):
        self.head.set_status(headStatus)
        self.body.set_status(bodyStatus)
        self.hands.set_status(handsStatus)
        self.legs.set_status(legsStatus)
        self.feet.set_status(feetStatus)

def populate_gearset(gearList):
    """
    Creates Gearset from a list of gear piece names.

    Parameters:
    gearList: The list of gear piece names.

    Returns:
    GearSet: GearSet object that contains 5/5 gear pieces
    """
    headPiece = GearPiece(gearList[HEAD])
    bodyPiece = GearPiece(gearList[BODY])
    handsPiece = GearPiece(gearList[HANDS])
    legsPiece = GearPiece(gearList[LEGS])
    feetPiece = GearPiece(gearList[FEET])
    gearSet = GearSet(headPiece, bodyPiece, handsPiece, legsPiece, feetPiece)
    return gearSet