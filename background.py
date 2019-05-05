import pyglet
import random

# TODO: make the background scrolling


class background:
    def __init__(self):
        # Load image
        image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Race_car2D/Images/background.png")

        # Create 2 (y = 500) sprites to fill the y = 1000 screen
        self.background_sprite1 = pyglet.sprite.Sprite(image, x=0, y=0)
        self.background_sprite2 = pyglet.sprite.Sprite(image, x=0, y=500)

        # Flowers setup
        self.flowers = []

    def draw(self):
        self.background_sprite1.draw()
        self.background_sprite2.draw()

        for x in range(len(self.flowers)):
            self.flowers[x].draw()

    def update(self):
        pass

    def flower_update(self, velocity):
        # Generate flowers
        if len(self.flowers) < 60:
            self.flowers.append(generate_flower())

        # Update the flower position in relation to the velocity
        for x in range(len(self.flowers)):
            self.flowers[x].y -= velocity / 8

        # Check if the flower is out of the screen
        for x in range(len(self.flowers)):
            if self.flowers[x].y < 0:
                del self.flowers[x]
                self.flowers.append(generate_flower())

    # Make all flowers move to the start position
    def reset_flowers(self):
        for x in range(len(self.flowers)):
            self.flowers[x].y = random.randint(1010, 2000)


# Generate a flower in a random x and y
def generate_flower():
    image = random_color()
    flower = pyglet.sprite.Sprite(image, x=random.randint(20, 580), y=random.randint(1010, 2000))
    while True:
        flower.x = random.randint(20, 580)
        flower.y = random.randint(1010, 2000)
        if flower.x < 120:
            break
        elif flower.x > 480:
            break
    return flower


# Choose a random color(0 = red, 1 = yellow, 2 = blue)
def random_color():
    color = random.randint(0, 2)

    # Load image
    if color is 0:
        image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Race_car2D/Images/flower_red.png")
    elif color is 1:
        image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Race_car2D/Images/flower_blue.png")
    elif color is 2:
        image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Race_car2D/Images/flower_yellow.png")

    return image
