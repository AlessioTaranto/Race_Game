import pyglet
import random

class car:
    def __init__(self):
        self.velocity = 0
        self.max_velocity = 40
        self.turnspeed = 5
        self.posx = 350
        self.posy = 200
        self.car_lenght = 16

        self.on_Track = True

        # Controls (-1 = min, 0 = idle ,1 = max)
        self.steering = 0

        # Load car image
        car_image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Race_car2D/Images/car.png")
        self.car_sprite = pyglet.sprite.Sprite(car_image, x = self.posx, y = self.posy)
 
        # Load dirt gif image
        dirt_left = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Race_car2D/Images/dirt_left.png")
        self.dirt_left_sprite = pyglet.sprite.Sprite(dirt_left, x = -10, y = -10)

        dirt_right = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Race_car2D/Images/dirt_right.png")
        self.dirt_right_sprite = pyglet.sprite.Sprite(dirt_right, x = -10, y = -10)

        dirt = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Race_car2D/Images/dirt.png")
        self.dirt_sprite = pyglet.sprite.Sprite(dirt, x = -10, y = -10)

    def draw(self):
        # Draw
        self.car_sprite.draw()

        # Draw dirt
        tire = self.tire_off()
        if tire is 0:
            self.dirt_sprite.set_position(self.posx, self.posy - 25)
            self.dirt_sprite.draw()
        elif tire is -1:
            self.dirt_left_sprite.set_position(self.posx, self.posy - 25)
            self.dirt_left_sprite.draw()
        elif tire is 1:
            self.dirt_right_sprite.set_position(self.posx, self.posy - 25)
            self.dirt_right_sprite.draw()

    def update(self, dt):
        self.update_velocity()
        # Check if the car is on the screen and make sure the car remain on the screen
        if self.posx  < 0:
            self.posx = 1
        if self.posx  > (600 - 25):
            self.posx = 600 - 26

        # Check steering
        if self.steering is -1:
            self.posx -= self.turnspeed
        elif self.steering is 1:
            self.posx += self.turnspeed
        else:
            self.posy = self.posy
        
        # Update position
        self.car_sprite.set_position(self.posx, self.posy)

    # Check which tire is off the track
    # Return (0 = both tires, -1 = left tire, 1 = right tire)
    def tire_off(self):
        self.on_Track = True

        # Left tire
        if self.posx < 150:
            self.on_Track = False
            if self.posx < (150 - self.car_lenght):
                return 0
            else:
                return -1
        
        # Right tire
        elif self.posx > 450 - self.car_lenght:
            self.on_Track = False
            if self.posx > 450:
                return 0
            else:
                return 1

    # Update the car velocity
    # TODO: finish to implent a better velocity menagment
    # TODO: fix glittering when off track
    def update_velocity(self):
        # If the car is on the dirt it goes slower
        if self.on_Track is False:
            if self.velocity > 20:
                self.velocity -= 0.5

        # Accelerate or decellerate
        if self.velocity < self.max_velocity:
            if self.velocity < 40:
                self.velocity += 0.2
            else:
                self.velocity += 0.1
        elif self.velocity > self.max_velocity + 1:
            self.velocity -= 0.4
