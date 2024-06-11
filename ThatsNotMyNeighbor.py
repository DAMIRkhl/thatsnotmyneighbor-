
from constant import *
import arcade


class FirstGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.BG = arcade.load_texture("Damir (2).png")
    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2 , SCREEN_WIDTH, SCREEN_HEIGHT, self.BG)
    def update(self, delta_time: float):
        pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        pass

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        pass

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        pass


window = FirstGame(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
