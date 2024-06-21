
from constant import *
import arcade


class FirstGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height,fullscreen=True)
        self.BG = arcade.load_texture("Damir (2).png")
        self.officeBg = arcade.load_texture("Office_Background.webp")
        hurt_sound = arcade.load_sound("a6f6-a2d8-4389-a606-173ef0cd7ef2.wav")
        arcade.play_sound(hurt_sound)
        self.offset_x = 0
        self.offset_y = 0
        self.max_offset_x = 300
        self.max_offset_y = 200

        self.some_sprite = arcade.Sprite('buttons2.png', 2)
        self.some_sprite.center_x = self.width / 2
        self.some_sprite.center_y = self.height / 2

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(self.width / 2 + self.offset_x,
                                      self.height / 2 + self.offset_y,
                                      self.width + 600, self.height + 400, self.officeBg)
        arcade.draw_texture_rectangle(self.width / 2 + self.offset_x,
                                      self.height / 2 + self.offset_y,
                                      self.width + 600, self.height + 400, self.BG)

        # self.some_sprite.draw()

    def update(self, delta_time: float):
        pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        pass

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.offset_x -= dx
        self.offset_y -= dy
        print(dx,dy)

        if self.offset_x > self.max_offset_x:
            self.offset_x = self.max_offset_x
        elif self.offset_x < -self.max_offset_x:
            self.offset_x = -self.max_offset_x

        if self.offset_y > self.max_offset_y:
            self.offset_y = self.max_offset_y
        elif self.offset_y < -self.max_offset_y:
            self.offset_y = -self.max_offset_y


    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        pass




window = FirstGame(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
