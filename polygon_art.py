import turtle
import random

class Polygon:
    def __init__(self,num_sides, size, orientation, location, color, border_size):
        self.__num_sides = num_sides
        self.__size = size
        self.__orientation = orientation
        self.__location = location
        self.__color = color
        self.__border_size = border_size
    
    def draw_polygon(self,i):
        turtle.penup()
        turtle.goto(self.__location[i][0], self.__location[i][1])
        turtle.setheading(self.__orientation[i])
        turtle.color(self.__color[i])
        turtle.pensize(self.__border_size[i])
        turtle.pendown()
        for _ in range(self.__num_sides):
            turtle.forward(self.__size[i])
            turtle.left(360/self.__num_sides)
        turtle.penup()
    
    def draw_multi_polygon(self,i,num_times):
        for _ in range(0,num_times):
            self.draw_polygon(i)
            reduction_ratio = 0.618
            turtle.penup()
            turtle.forward(self.__size[i]*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(self.__size[i]*(1-reduction_ratio)/2)
            turtle.right(90)
            self.__location[i][0] = turtle.pos()[0]
            self.__location[i][1] = turtle.pos()[1]
            self.__size[i] *= reduction_ratio
        

class gen_art:
    def __init__(self, num_art):
        self.__art_type = int(input("Which art do you want to generate? Enter a number between 1 to 8, inclusive:"))
        self.__num_art = num_art
        self.__num_sides = 0
        self.__size = []
        self.__orientation = []
        self.__location = []
        self.__color = []
        self.__border_size = []
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        for _ in range(self.__num_art):
            self.__size.append(random.randint(50, 150))
            self.__orientation.append(random.randint(0, 90))
            self.__location.append([random.randint(-300, 300), random.randint(-200, 200)])
            self.__color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            self.__border_size.append(random.randint(1, 10))
    
    def initiate(self):
        if self.__art_type == 1 or self.__art_type == 5:
            self.__num_sides = 3
        elif self.__art_type == 2 or self.__art_type == 6:
            self.__num_sides = 4
        elif self.__art_type == 3 or self.__art_type == 7:
            self.__num_sides = 5
        for i in range(self.__num_art):
            if self.__art_type == 4 or self.__art_type == 8:
                self.__num_sides = random.randint(3, 5)
            artwork = Polygon(self.__num_sides,self.__size,self.__orientation,self.__location,self.__color,self.__border_size)
            if self.__art_type <= 4:
                artwork.draw_polygon(i)
            elif self.__art_type > 4:
                artwork.draw_multi_polygon(i,3)
        turtle.done()


if __name__ == "__main__":
    my_art = gen_art(30)
    my_art.initiate()