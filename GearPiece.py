#Python program used to Set the status and print individual Gear Pieces

class GearPiece:
    def __init__(self, name):
        """
        Constructor for GearPiece.

        Parameters:
        name (str): Name of the Gear Piece.
        """
        self.name = name
        self.status = False

    def __str__(self):
        return f"{self.name}"

    #Getters for GearPiece class
    def get_name(self):
        return self.name
    def get_status(self):
        return self.status

    #Setters for GearPiece class
    def set_name(self, name):
        self.name = name
    def set_status(self, status):
        self.status = status
