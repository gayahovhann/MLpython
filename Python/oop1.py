class Animals: 
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def aboutanimal(self):
        print("I am animal, my weight is{} kg, my height is {} cm".format(self.weight, self.height))


class Graund(Animals):
    def __init__(self, height, weight, velocity_on_ground):
        super().__init__(height, weight)
        self.velocity_on_ground = velocity_on_ground

    def aboutground(self):
        print("I am animal, my weight and height are {} kg and {} cm, my velocity on graound is {}".format(self.weight, self.height, self.velocity_on_ground))


class Water(Animals):
    def __init__(self, height, weight, velocity_in_water):
        super().__init__(height, weight)
        self.velocity_in_water = velocity_in_water

    def aboutwater(self):
        print("I am animal, my weight and height are {} kg and {} cm, my velocity in water is {}".format(self.weight, self.height, self.velocity_in_water))


class Air(Animals):
    def __init__(self, height, weight, velocity_in_air):
        super().__init__(height, weight)
        self.velocity_in_air = velocity_in_air

    def aboutair(self):
        print("My name is animal, my weight and height are {} kg and {} cm, my velocity in air is {}".format(self.weight, self.height, self.velocity_in_air))


general_animal = Animals(25, 65)
general_animal.aboutanimal()
#....