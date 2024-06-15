import turtle
import time
WIDTH, HEIGHT = 500, 500

#initializes a graphical user interface with turtle racers
def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number turtle you want to race (2 -10): ")
        if racers.isdigit() :
            racers = int(racers)
        else:
            print("Input is not Numeric... Try Again!")
            continue #takes the execution back to the starting of while loop
        
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number is not in range between 2 and 10. Try Again!")


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

racers = get_number_of_racers()
init_turtle()

racer = turtle.Turtle()
racer.forward(100)
time.sleep(5)