from constant import *
import arcade

from floors import Floor1, Floor2, Floor3
from hucrechers import Humans
from ponchocopay import OpenDoorsButtons


class FirstGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, fullscreen=True)
        self.BG = arcade.load_texture("Office.png")
        self.officeBg = arcade.load_texture("Office_Background.webp")
        self.neighborsinfo = arcade.load_texture("pixelcut-export-removebg-preview.png")
        self.darkness = arcade.load_texture("A_black_image.jpg")
        hurt_sound = arcade.load_sound("bg_sounds.wav")
        arcade.play_sound(hurt_sound)
        self.offset_x = 0
        self.offset_y = 0
        self.max_offset_x = 300
        self.max_offset_y = 200
        self.opencloseF = False

        self.aristacratic = Humans("Charecters/Aristacratic.webp",
                                   ["Big nose", "Prominent mustache","Uses a monocle", "Wears a hat", "Round face"],
                                   749468,
                                   7777,
                                   4,
                                   3,
                                   "aristacratism",
                                   "Aristacratic")
        self.fisryk = Humans("Charecters/image_2024-07-16_23-11-54.png",
                             ["Red plaid button-up jacket", "White t-shirt with a blue peace sign",
                              "Red and pink headband", "Long grey hair","Scraggly beard", "Round nose",
                              "Eyes are two different sizes"],
                             123678,
                             5938,
                             1,
                             1, "pe_teacher",
                             "Fisryk")
        self.joe_biden = Humans("Charecters/Francis_Mosses.webp",
                                ["Long nose", "Thin chin", "Tired eyes","Short hair", "Wears a hat"],
                                656754,
                                5836,
                                3,
                                3,
                                "seamen",
                                "Joe Biden")
        self.the_fnaf_creator = Humans("Charecters/Dr._W._Afton.webp",
                                       ["Robust eyebrows", "Wears glasses", "Short hair",
                                        "Round nose", "Square head"],
                                       856745,
                                       9675,
                                       2,
                                       1,
                                       "sret",
                                       "Dr. W. Afton")
        self.bob = Humans("Charecters/Angus_Ciprianni.webp",
                          ["Long neck", "Wears a hat", "Has a moustache","Small eyes"],
                          756954,
                          6946,
                          4,
                          2,
                          "Ofice job",
                          "Bob")
        self.Nacha = Humans(
            human="Charecters/Nacha_Mikaelys.webp",
            appearance=["Right eye blue", "Left eye green", "Curly hair", "She has freckles", "Round face",
                        "Blue shirt & White collar", "Small eyes", "Hair bun", "Blue hairtie"],
            ID=789653,
            phone_number=1346,
            apartment_number="2",
            floor=2,
            job="Chef",
            name="Nacha Mikaelys"
        )
        self.Yog = Humans(
            human="Charecters/Yog_Sothoth.webp",
            appearance=["Long nose", "Nose Ring", "Shaded Eyes", "Short Hair", "Has Fangs"],
            ID=689547,
            phone_number=1346,
            apartment_number="3",
            floor=2,
            job="Vampirism",
            name="Yog Sothoth"
        )
        self.Gloria = Humans(
            human="Charecters/Gloria_Schmicht.webp",
            appearance=["Round face", "Mole on right cheek", "Short hair", "Round nose"],
            ID=698522,
            phone_number="5123",
            apartment_number="1",
            floor="2",
            job="Banker",
            name="Gloria Schmicht",
        )
        self.Anastacha = Humans(
            human="Charecters/Anastacha_Mikaelys.webp",
            appearance=[
                "Tired eyes", "Two ponytails", "Small nose", "Round face",
                "Brown hair", "Blue hair ties", "White shirt with a blue collar", "Purple backpack"
            ],
            ID=132698,
            phone_number=1346,
            apartment_number="2",
            floor=3,
            job="Student",
            name="Anastacha_Mikaelys"
        )

        self.Peache = Humans(
            human="Charecters/Robertsky_Peachman.webp",
            appearance=[
                "Long neck", "Without eyebrows", "Big nose", "Has a goatee",
                "Orange curly hair", "Small eyes", "Yellow shirt", "Blue ascot"
            ],
            ID=114652,
            phone_number=2668,
            apartment_number="4",
            floor=1,
            job="Shoemaker",
            name="RobertskyPeachman",
        )
        self.Izaack = Humans(
            human="Charecters/Izaack_Gauss.webp",
            appearance=[
                "Big eyebrows", "Big smile", "Prominent chin", "Big nose",
                "Blue eyes", "Dark gray trench coat", "White shirt", "Dull blue necktie"
            ],
            ID=456985,
            phone_number=7332,
            apartment_number="3",
            floor=1,
            job="Reporter",
            name="Izaack Gauss"
                )
        self.humans.append(self.fisryk)
        self.humans.append(self.aristacratic)
        self.humans.append(self.joe_biden)
        self.humans.append(self.Afton)
        self.humans.append(self.bob)
        self.humans.append(self.Nacha)
        self.humans.append(self.Yog)
        self.humans.append(self.Gloria)
        self.humans.append(self.Anastacha)
        self.humans.append(self.Peache)
        self.humans.append(self.Izaack)

        self.humans[0].center_x = self.width // 2 - 50
        self.humans[0].center_y = self.height // 2
        # self.aristacratic.center_y = self.height // 2
        # self.aristacratic.center_x = self.width // 2

        self.openclose = OpenDoorsButtons()
        self.floor1 = Floor1()
        self.floor2 = Floor2()
        self.floor3 = Floor3()

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(self.width / 2 + self.offset_x,
                                      self.height / 2 + self.offset_y,
                                      self.width + 600, self.height + 400, self.officeBg)

        arcade.draw_texture_rectangle(self.width / 2 + self.offset_x,
                                      self.height / 2 + self.offset_y,
                                      self.width + 600, self.height + 400, self.BG)
        self.humans.draw()
        self.openclose.draw()
        self.floor1.draw()
        self.floor2.draw()
        self.floor3.draw()

        if self.opencloseF == True:
            arcade.draw_texture_rectangle(self.width / 2, self.height / 2,
                                          self.width, self.height, self.darkness, alpha=65)
            arcade.draw_texture_rectangle(self.width / 2, self.height / 2,
                                          self.width - 100, self.height - 150, self.neighborsinfo)
            arcade.draw_text(self.fisryk.phone_number,825,590,font_size=30,color=arcade.color.BLACK)

    def update(self, delta_time: float):
        self.openclose.center_x = self.width / 0.90 + self.offset_x
        self.openclose.center_y = self.height / 30 + self.offset_y
        self.floor1.center_x = self.width / 0.957 + self.offset_x
        self.floor1.center_y = self.height / 1.05 + self.offset_y
        self.floor2.center_x = self.width / 0.957 + self.offset_x
        self.floor2.center_y = self.height / 1.5 + self.offset_y
        self.floor3.center_x = self.width / 0.957 + self.offset_x
        self.floor3.center_y = self.height / 2.6 + self.offset_y
        self.aristacratic.center_x = self.width / 30 + self.offset_x
        self.aristacratic.center_y = self.height / 2 + self.offset_y
        self.fisryk.center_x = self.width / 30 + self.offset_x
        self.fisryk.center_y = self.height / 2 + self.offset_y
        self.joe_biden.center_x = self.width / 30 + self.offset_x
        self.joe_biden.center_y = self.height / 2 + self.offset_y
        self.Afton.center_x = self.width / 30 + self.offset_x
        self.Afton.center_y = self.height / 2 + self.offset_y
        self.bob.center_x = self.width / 30 + self.offset_x
        self.bob.center_y = self.height / 2 + self.offset_y
        self.Nacha.center_x = self.width / 30 + self.offset_x
        self.Nacha.center_y = self.height / 2 + self.offset_y
        self.Yog.center_x = self.width / 30 + self.offset_x
        self.Yog.center_y = self.height / 2 + self.offset_y
        self.Gloria.center_x = self.width / 30 + self.offset_x
        self.Gloria.center_y = self.height / 2 + self.offset_y
        self.Anastacha.center_x = self.width / 30 + self.offset_x
        self.Anastacha.center_y = self.height / 2 + self.offset_y
        self.Peache.center_x = self.width / 30 + self.offset_x
        self.Peache.center_y = self.height / 2 + self.offset_y
        self.Izaack.center_x = self.width / 30 + self.offset_x
        self.Izaack.center_y = self.height / 2 + self.offset_y

        self.humans[0].update()
        self.humans[0].move()
        print(self.humans[0].center_x)

        # if time.time() - self.timer > 2:
        #     self.close()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.close()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.floor1.left <= x <= self.floor1.right and self.floor1.bottom <= y <= self.floor1.top:
            self.opencloseF = True
        if self.opencloseF:
            if 515 <= x <= 557 and 761 <= y <= 803:
                self.opencloseF = False

        if self.floor2.left <= x <= self.floor2.right and self.floor2.bottom <= y <= self.floor2.top:
            self.opencloseF = True

        if self.floor3.left <= x <= self.floor3.right and self.floor3.bottom <= y <= self.floor3.top:
            self.opencloseF = True

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.offset_x -= dx
        self.offset_y -= dy

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

# чё пацаны аниме??😎 17.06.2024
