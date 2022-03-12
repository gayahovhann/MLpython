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
