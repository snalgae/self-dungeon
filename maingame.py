"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"

class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Call draw() on all your sprite lists below
    def grid_draw(self, x, y, sqwidth, sqheight, versquares, horsquares, rgbcolor, linesize=1):
        arcade.start_render()
        for i in range(versquares):
            for j in range(horsquares):
                print(x+(sqwidth*j), y+(sqheight*i))
                arcade.draw_rectangle_filled(x+(sqwidth*j), y+(sqheight*i), sqwidth-linesize, sqwidth-linesize, rgbcolor)
        arcade.finish_render()


    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        self.grid_draw(5,5,10,10,10,10,(10,10,10))



def main():
    """ Main function """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()