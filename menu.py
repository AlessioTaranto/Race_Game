import pyglet

# TODO: create a debug menu

class menu:
    def __init__(self):
        # Load background
        background_image = pyglet.image.load("C:/Users/aless/Documents/Python/2D_games/Race_car2D/Images/menu_background.png")
        self.background_sprite = pyglet.sprite.Sprite(background_image, x=0, y=0)

        # Setup texts
        self.info_score = pyglet.text.Label("Score: " + str(0),
                                            font_name='Arial',
                                            font_size=14,
                                            x=10, y=30)
        self.info_velocity = pyglet.text.Label("Velocity: " + str(0),
                                               font_name='Arial',
                                               font_size=14,
                                               x=10, y=10)

    # Draw menu
    def draw(self):
        self.background_sprite.draw()
        self.info_score.draw()
        self.info_velocity.draw()

    # Menu Update
    def update(self, velocity, score):
        self.info_velocity.text = ("Velocity: " + str(int(velocity)))
        self.info_score.text = ("Score: " + str(int(score)))
