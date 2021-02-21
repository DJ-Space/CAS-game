"""
Platformer Game
"""
import arcade
import random

# Constants
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 975
SCREEN_TITLE = "CAS-Game"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable = True)
        
        bgcolor = [arcade.csscolor.DARK_OLIVE_GREEN, arcade.csscolor.SLATE_GRAY, arcade.csscolor.ROYAL_BLUE]
        windowcolor = random.choice(bgcolor)
        arcade.set_background_color(windowcolor)
        
    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        pass

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()
        # Code to draw the screen goes here


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
