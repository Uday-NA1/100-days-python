import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

over = False

while not over:
    time.sleep(0.1)
    screen.update()
    
    # Create and move cars
    car_manager.create_car()
    car_manager.move()

    # Detect car collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            over = True
            score.game_over()

    # Detect player cross
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score.point()

screen.exitonclick()