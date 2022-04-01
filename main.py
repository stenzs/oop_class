class Elevator:
    def __init__(self, starting_floor):
        self.make = "The elevator company"
        self.floor = starting_floor


elevator = Elevator(6)
print(elevator.make)
print(elevator.floor)


class Square:
    def __init__(self):
      self.__height = 2
      self.__width = 2
    def set_side(self, new_side):
      self.__height = new_side
      self.__width = new_side
    def get_height(self):
      return self.__height, self.__width
    def set_height(self, h):
      if h >= 0:
        self.__height = h
      else:
        raise Exception("value needs to be 0 or larger")

square = Square()
square.set_height(10)
print(square.get_height())
square.set_side(20)
print(square.get_height())
