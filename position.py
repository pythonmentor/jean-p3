class Position:
    """This class define the different position of Macgyver"""
    def __init__(self, x, y):
        self._x = x
        self._y = y

   
    def _get_up(self):
        """This method define the up direction"""
        return Position(self._x-1, self._y)

    def _get_down(self):
        """This method define the down direction"""
        return Position(self._x+1, self._y)

    def _get_left(self):
        """This method define the left direction"""
        return Position(self._x, self._y-1)

    def _get_right(self):
        """This method define the right direction"""
        return Position(self._x, self._y+1)

    def __repr__(self):
        return str((self._x, self._y))



