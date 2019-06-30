from position import Position
from macgyver import MacGyver
class Labyrinth:
    """This class define the labyrinth model"""

    def __init__(self):
        """ This method is the constructor of the class Labyrinth"""
        self.streets = []
        self.walls = []
        self.width = None
        self.heigth = None
        self.departure = None
        self.arrival = None
        self.macgyver = None
        self.position = None


    def load_labyrinth_from_file(self, file_name):
        """-This method allows to:
           -Read labyrinth file
           -Determine labyrinth height and width
           -Determine walls and streets in the labyrinth"""

        with open("labyrinth.txt", "r") as my_file:
            my_labyrinth = my_file.readlines()

            #Determination of the street and wall of the labyrinth
            for i, ligne in enumerate(my_labyrinth):
                for j, caracter in enumerate(ligne.strip()):
                    if caracter == '.':
                        self.streets.append(Position(i,j))
                    elif caracter == '#':
                        self.walls.append(Position(i,j))
                    elif caracter == 'D':
                        self.departure = Position(i,j)
                    elif caracter == 'A':
                        self.arrival = Position(i,j) 
                          
            # Determination of the heigh and width of the labyrinth
                self.heigth = len(my_labyrinth)
                self.width = len(my_labyrinth[0].strip())

              
    def is_streets(self, position):
        """This methode return true if the position is a street"""
        if position in self.streets:
            return True
        return False

    def is_walls(self, position):
        """This method return true if the position is a wall"""
        if position in self.walls:
            return True
        return False


  
    def display(self):
        """This method display the labyrinth"""
        labyrinth = ""
        for i in range(self.heigth):
            for j in range(self.width):
                if Position(i, j) == self.macgyver.position:
                    labyrinth +="M" 
                elif Position(i, j) in self.streets:
                    labyrinth += "."
                elif Position(i, j) in self.walls:
                    labyrinth +="#"

                elif Position(i, j) == self.arrival:
                    labyrinth += "A"
                elif Position(i, j) == self.departure:
                    labyrinth += "D"
            labyrinth += "\n"

        return labyrinth
    
        

   
def main():
    labyrinth = Labyrinth()
    labyrinth.load_labyrinth_from_file("labyrinth.txt")
    macgyver = MacGyver(labyrinth)
    macgyver.move("go_right")
    macgyver.move("go_right")
    macgyver.move("go_down")
    macgyver.move("go_down")
    print(labyrinth.display())


if __name__=="__main__":
    main()





 



