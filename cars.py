from turtle import Turtle
import random

COLOR_LIST = ["black", "gray", "green", "red", "blue", "orange", "purple", "yellow"]
Y_POS = [0, 20, 40, 80, 100, 120, 140, 160, 180,
            200, 220, 240, -20, -40, -80, -100,  -120, -140, 
            -160, -180, -200, -220, -240]
MOVE_DISTANCE = 5

class Cars(Turtle):

    def __init__(self):
        self.cars = []
          
    def create_car(self):
        random_chance = random.randint(1 , 6)
        if random_chance == 1:
            car = Turtle(shape="square")
            car.color(random.choice(COLOR_LIST))
            car.shapesize(1,2)
            car.penup()
            car.goto(x = 300, y = random.choice(Y_POS))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(MOVE_DISTANCE)

