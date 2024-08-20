import time

from constant import *
import arcade

from floors import Floor1, Floor2, Floor3
from hucrechers import Humans
from ponchocopay import OpenDoorsButtons


class FirstGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, fullscreen=True)

        # textures
        self.BG = arcade.load_texture("Office.png")
        self.officeBg = arcade.load_texture("Office_Background.webp")
        self.neighborsinfo = arcade.load_texture("FO-removebg-preview.png")
        self.darkness = arcade.load_texture("A_black_image.jpg")

        # sprite lists
        self.humans = arcade.SpriteList()

        # sprites
        self.openclose = OpenDoorsButtons()
        self.floor1 = Floor1()
        self.floor2 = Floor2()
        self.floor3 = Floor3()

        # states and etc
        self.folder_floor1 = False
        self.folder_floor2 = False
        self.folder_floor3 = False
        self.current_flat = 1
        self.opencloseF = False

        self.offset_x = 0
        self.offset_y = 0
        self.max_offset_x = 300
        self.max_offset_y = 200

        # sounds
        hurt_sound = arcade.load_sound("bg_sounds.wav")
        arcade.play_sound(hurt_sound)

        self.create_people()

    def create_people(self):
        self.aristacratic = Humans(
            human="Charecters/Aristacratic.webp",
            appearance=["Big nose", "Prominent mustache", "Uses a monocle", "Wears a hat", "Round face"],
            ID=749468,
            phone_number=7777,
            apartment_number=4,
            floor=3,
            job="aristacratism",
            name="Aristacratic",
            picture='Charecters/download__5_-removebg-preview.png',
        )
        self.fisryk = Humans(
            human="Charecters/image_2024-07-16_23-11-54.png",
            appearance=["Red plaid button-up jacket",
                        "White t-shirt with a blue peace sign",
                        "Red and pink headband", "Long grey hair",
                        "Scraggly beard", "Round nose",
                        "Eyes are two different sizes"],
            ID=123678,
            phone_number=5938,
            apartment_number=1,
            floor=1,
            job="pe teacher",
            name="Fisryk",
            picture='buttons2.png'
        )

        self.joe_biden = Humans(
            human="Charecters/Francis_Mosses.webp",
            appearance=["Long nose", "Thin chin", "Tired eyes", "Short hair", "Wears a hat"],
            ID=656754,
            phone_number=5836,
            apartment_number=3,
            floor=3,
            job="milkman",
            name="Franis Mosses",
            picture='Charecters/image-removebg-preview.png'
        )

        self.Afton = Humans(
            human="Charecters/Dr._W._Afton.webp",
            appearance=["Robust eyebrows", "Wears glasses", "Short hair",
                        "Round nose", "Square head"],
            ID=856745,
            phone_number=9675,
            apartment_number=2,
            floor=1,
            job="sret",
            name="Dr.W.Afton",
            picture='Charecters/download-removebg-preview (1).png'
        )

        self.bob = Humans(
            human="Charecters/Angus_Ciprianni.webp",
            appearance=["Long neck", "Wears a hat", "Has a moustache", "Small eyes"],
            ID=756954,
            phone_number=6946,
            apartment_number=4,
            floor=2,
            job="Ofice job",
            name="Bob",
            picture='Charecters/download__2_-removebg-preview.png'
        )

        self.Nacha = Humans(
            human="Charecters/Nacha_Mikaelys.webp",
            appearance=["Right eye blue", "Left eye green", "Curly hair", "She has freckles", "Round face",
                        "Blue shirt & White collar", "Small eyes", "Hair bun", "Blue hairtie"],
            ID=789653,
            phone_number=1346,
            apartment_number="2",
            floor=2,
            job="Chef",
            name="Nacha Mikaelys",
            picture='Charecters/download__1_-removebg-preview.png'
        )

        self.Yog = Humans(
            human="Charecters/Yog_Sothoth.webp",
            appearance=["Long nose", "Nose Ring", "Shaded Eyes", "Short Hair", "Has Fangs"],
            ID=689547,
            phone_number=1346,
            apartment_number="3",
            floor=2,
            job="Vampirism",
            name="Yog Sothoth",
            picture='Charecters/Yog_Sothoth.webp'
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
            picture='Charecters/download-removebg-preview (2).png'
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
            name="Anastacha Mikaelys",
            picture='Charecters/download__4_-removebg-preview.png'
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
            name="Robertsky Peachman",
            picture='Charecters/download-removebg-preview (4).png'
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
            name="Izaack Gauss",
            picture='Charecters/download__1_-removebg-preview (2).png'
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

        self.humans[0].center_x = 0
        self.humans[0].center_y = self.height // 2


    def draw_info_neighbor(self, person: Humans, distance_text: int, font_size: int):
        """Рисует инфу о соседях в папках с этажами"""

        arcade.draw_text(person.phone_number, 825, 590, font_size=30, color=arcade.color.BLACK)
        arcade.draw_text(person.ID, 700, 470, font_size=30, color=arcade.color.BLACK)

        for i in range(len(person.appearance)):
            arcade.draw_text(person.appearance[i], 350, 135 + distance_text * i, font_size=font_size, color=arcade.color.BLACK)
        arcade.draw_texture_rectangle(280, 320, person.picture.width * 2.5, person.picture.height * 2.5, person.picture)

    def on_draw(self):
        self.clear()

        arcade.draw_texture_rectangle(self.width / 2 + self.offset_x,
                                      self.height / 2 + self.offset_y,
                                      self.width + 600, self.height + 400, self.officeBg)

        self.humans.draw()

        arcade.draw_texture_rectangle(self.width / 2 + self.offset_x,
                                      self.height / 2 + self.offset_y,
                                      self.width + 600, self.height + 400, self.BG)
        self.openclose.draw()
        self.floor1.draw()
        self.floor2.draw()
        self.floor3.draw()

        # ---------------------------------------- этажи ---------------------------------------- #

        # -------- первый этаж -------- #
        if self.folder_floor1 :
            arcade.draw_texture_rectangle(self.width / 2, self.height / 2,
                                          self.width, self.height, self.darkness, alpha=65)
            arcade.draw_texture_rectangle(self.width / 2, self.height / 2,
                                          self.width - 100, self.height - 150, self.neighborsinfo)

            if self.current_flat == 1:
                self.draw_info_neighbor(self.fisryk, 25, 17)
            elif self.current_flat == 2:
                self.draw_info_neighbor(self.Afton, 30, 20)
            elif self.current_flat == 3:
                self.draw_info_neighbor(self.Izaack, 30, 20)
            elif self.current_flat == 4:
                self.draw_info_neighbor(self.Peache, 25, 20)

        # -------- второй этаж -------- #
        elif self.folder_floor2:
            arcade.draw_texture_rectangle(self.width / 2, self.height / 2,
                                          self.width, self.height, self.darkness, alpha=65)
            arcade.draw_texture_rectangle(self.width / 2, self.height / 2,
                                          self.width - 100, self.height - 150, self.neighborsinfo)

            if self.current_flat == 1:
                self.draw_info_neighbor(self.Gloria, 25, 20)
            elif self.current_flat == 2:
                self.draw_info_neighbor(self.Nacha, 22, 16)
            elif self.current_flat == 3:
                self.draw_info_neighbor(self.Yog, 25, 20)
            elif self.current_flat == 4:
                self.draw_info_neighbor(self.bob, 25, 20)

        # -------- третий этаж -------- #
        elif self.folder_floor3:
            arcade.draw_texture_rectangle(self.width / 2, self.height / 2,
                                          self.width, self.height, self.darkness, alpha=65)
            arcade.draw_texture_rectangle(self.width / 2, self.height / 2,
                                          self.width - 100, self.height - 150, self.neighborsinfo)

            if self.current_flat == 1:
                self.draw_info_neighbor(self.Anastacha, 25, 20)
            elif self.current_flat == 2:
                pass    # ПУСТАЯ ХАТА, НЕ ЗАНИМАТЬ!!!
            elif self.current_flat == 3:
                self.draw_info_neighbor(self.joe_biden, 25, 20)
            elif self.current_flat == 4:
                self.draw_info_neighbor(self.aristacratic, 25, 20)

    def update(self, delta_time: float):
        # обновление координат для разных спрайтов
        self.openclose.center_x = self.width / 0.90 + self.offset_x
        self.openclose.center_y = self.height / 30 + self.offset_y
        self.floor1.center_x = self.width / 0.957 + self.offset_x
        self.floor1.center_y = self.height / 1.05 + self.offset_y
        self.floor2.center_x = self.width / 0.957 + self.offset_x
        self.floor2.center_y = self.height / 1.5 + self.offset_y
        self.floor3.center_x = self.width / 0.957 + self.offset_x
        self.floor3.center_y = self.height / 2.6 + self.offset_y
        # self.aristacratic.center_x = self.width / 30 + self.offset_x
        # self.aristacratic.center_y = self.height / 2 + self.offset_y
        # self.fisryk.center_x = self.width / 30 + self.offset_x
        # self.fisryk.center_y = self.height / 2 + self.offset_y
        # self.joe_biden.center_x = self.width / 30 + self.offset_x
        # self.joe_biden.center_y = self.height / 2 + self.offset_y
        # self.Afton.center_x = self.width / 30 + self.offset_x
        # self.Afton.center_y = self.height / 2 + self.offset_y
        # self.bob.center_x = self.width / 30 + self.offset_x
        # self.bob.center_y = self.height / 2 + self.offset_y
        # self.Nacha.center_x = self.width / 30 + self.offset_x
        # self.Nacha.center_y = self.height / 2 + self.offset_y
        # self.Yog.center_x = self.width / 30 + self.offset_x
        # self.Yog.center_y = self.height / 2 + self.offset_y
        # self.Gloria.center_x = self.width / 30 + self.offset_x
        # self.Gloria.center_y = self.height / 2 + self.offset_y
        # self.Anastacha.center_x = self.width / 30 + self.offset_x
        # self.Anastacha.center_y = self.height / 2 + self.offset_y
        # self.Peache.center_x = self.width / 30 + self.offset_x
        # self.Peache.center_y = self.height / 2 + self.offset_y
        # self.Izaack.center_x = self.width / 30 + self.offset_x
        # self.Izaack.center_y = self.height / 2 + self.offset_y

        # self.humans[0].update()
        # self.humans[0].move_to_center()
        # self.humans[0].center_y = self.height // 2 + self.offset_y
        # self.humans[0].center_x = self.humans[0].center_x + self.offset_x
        # print(self.humans[0].center_x)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.close()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print(x, y)
        print(all([self.folder_floor1, self.folder_floor2, self.folder_floor3]))

        if (self.floor1.left <= x <= self.floor1.right and self.floor1.bottom <= y <= self.floor1.top and
                not any([self.folder_floor1,self.folder_floor2,self.folder_floor3])):
            self.folder_floor1 = True
        if (self.floor2.left <= x <= self.floor2.right and self.floor2.bottom <= y <= self.floor2.top and
                not any([self.folder_floor1,self.folder_floor2,self.folder_floor3])):
            self.folder_floor2 = True
        if (self.floor3.left <= x <= self.floor3.right and self.floor3.bottom <= y <= self.floor3.top and
                not any([self.folder_floor1,self.folder_floor2,self.folder_floor3])):
            self.folder_floor3 = True

        if self.folder_floor1 or self.folder_floor2 or self.folder_floor3:  # нажатие на крестик в этажах
            if 515 <= x <= 557 and 761 <= y <= 803:
                self.folder_floor1 = False
                self.folder_floor2 = False
                self.folder_floor3 = False

            # если открыт этаж, то выбираем конкретную квартиру
            if 344 <= x <= 603 and 638 <= y <= 705:
                self.current_flat = 1
            elif 607 <= x <= 860 and 641 <= y <= 705:
                self.current_flat = 2
            elif 861 <= x <= 1115 and 641 <= y <= 705:
                self.current_flat = 3
            elif 1116 <= x <= 1367 and 641 <= y <= 705:
                self.current_flat = 4

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
# ---------------------------------------------------- #
"""


"""
