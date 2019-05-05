import os
import pyglet
from pyglet.window import key, FPSDisplay

from background import background
from barrier import barrier
from car import car
from menu import menu

# TODO: implement a better image finding system

class Game_Window(pyglet.window.Window):
    def __init__(self):
        super(Game_Window, self).__init__()

        # Window setup
        self.frame_rate = 1 / 60.0
        self.set_size(600, 1000)
        self.set_location(200, 50)
        self.set_caption('Race Game')
        self.fps_display = FPSDisplay(self)
        self.fps_display.label.x = 10
        self.fps_display.label.y = 980
        self.fps_display.label.font_size = 14

        # Dependecies setup
        self.background = background()
        self.menu = menu()
        self.race_car = car()
        self.barriers = []
        self.start_score = 600
        self.score = self.start_score

    def on_key_press(self, symbol, modifiers):
        if symbol is key.A:
            self.race_car.steering = -1
        elif symbol is key.D:
            self.race_car.steering = 1

    def on_key_release(self, symbol, modifiers):
        if symbol is key.A:
            self.race_car.steering = 0
        elif symbol is key.D:
            self.race_car.steering = 0

        # Restart key
        if symbol is key.R:
            self.restart()

    # Draw function
    def on_draw(self):
        self.clear()
        self.background.draw()
        self.race_car.draw()
        self.menu.draw()

        self.fps_display.draw()

        # Draw barriers
        for x in range(len(self.barriers)):
            self.barriers[x].draw()

    # Update function
    def update(self, dt):
        # Update Dependecies
        self.update_barriers()
        self.update_difficulty()
        self.background.flower_update(self.race_car.velocity)
        self.race_car.update(dt)
        self.menu.update(self.race_car.velocity, self.score)

        # Check collisions
        self.check_collision()

        # Update score
        if self.race_car.on_Track is False:
            self.score -= 0.1
        else:
            self.score += (self.race_car.velocity / 200)

    # Update barriers
    def update_barriers(self):
        # Check if there's not barrier and create the first one
        if len(self.barriers) is 0:
            self.barriers.append(barrier())

        # Update barriers position
        for x in range(len(self.barriers)):
            self.barriers[x].update(self.race_car.velocity)

        # Check if a barrier is out of the screen
        for x in range(len(self.barriers)):
            # Delete old one and create a new one
            if self.barriers[x].posy < 0:
                del self.barriers[x]
                self.barriers.append(barrier())

    # Restart function
    def restart(self):
        if self.score > self.start_score:
            print('Score: ' + str(int(self.score)))
        self.score = self.start_score
        self.race_car.velocity = 0
        self.race_car.posx = 350
        self.race_car.posy = 200

        # Delete all flowers
        for x in range(len(self.background.flowers)):
            self.background.reset_flowers()

        # Delete all barriers
        for x in range(len(self.barriers)):
            del self.barriers[x]

    # Check if a collision has happened and restart the game
    def check_collision(self):
        # Calculate the x,y of the car
        car_x = []
        for x in range(self.race_car.posx, self.race_car.posx + self.race_car.car_lenght):
            car_x.append(x)
        car_y = []
        for x in range(self.race_car.posy - 15, self.race_car.posy):
            car_y.append(x)

        # Calculate the x,y of the barrier
        barrier_x = []
        for b in range(len(self.barriers)):
            for x in range(self.barriers[b].posx, self.barriers[b].posx + 100):
                barrier_x.append(x)
        barrier_y = int(self.barriers[0].posy)

        # Check if the car collides with a barrier
        for b in range(len(self.barriers)):
            if barrier_y in car_y:  # 'y' axis
                for x in barrier_x:
                    if x in car_x:  # 'x' axis
                        if self.score is not 0:
                            self.restart()

    # Update the difficulty
    def update_difficulty(self):
        if 200 < self.score < 300:
            self.race_car.max_velocity = 50
        elif 300 < self.score < 400:
            self.race_car.max_velocity = 60
        elif 400 < self.score < 500:
            self.race_car.max_velocity = 70
        elif 600 < self.score < 700:
            self.race_car.max_velocity = 80


if __name__ == "__main__":
    window = Game_Window()
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()
