import random
import pyglet


class barrier:
    def __init__(self):
        self.lenght = 100
        self.posx = random.randint(150, 450 - 100)
        self.posy = 1100

        # Choose the color and create the sprite
        image = random_color()
        self.barrier = pyglet.sprite.Sprite(image, x=self.posx, y=self.posy)

    # Update function
    def update(self, velocity):
        # Calculate new position and set it
        self.posy -= (velocity / 4)
        self.barrier.set_position(self.posx, self.posy)

    # Draw function
    def draw(self):
        self.barrier.draw()


# Choose a random color(0 = red, 1 = yellow, 2 = blue)
def random_color():
    color = random.randint(0, 2)

    # Load image
    if color is 0:
        image = pyglet.image.load("C:/Users/aless/Documents/Pyton/2D_games/Race_car/resources/barrier_red.png")
    elif color is 1:
        image = pyglet.image.load("C:/Users/aless/Documents/Pyton/2D_games/Race_car/resources/barrier_yellow.png")
    elif color is 2:
        image = pyglet.image.load("C:/Users/aless/Documents/Pyton/2D_games/Race_car/resources/barrier_blue.png")

    return image

