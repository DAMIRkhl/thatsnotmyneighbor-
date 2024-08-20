import arcade


class Humans(arcade.Sprite):
    def __init__(self, human, appearance, ID, phone_number, apartment_number, floor, job, name,picture ="Charecters/download__1_-removebg-preview.png", scale=0.5):
        super().__init__(filename=human, scale=scale)
        self.appearance = appearance
        self.human = human
        self.ID = ID
        self.phone_number = phone_number
        self.apartment_number = apartment_number
        self.floor = floor
        self.job = job
        self.name = name
        self.picture = arcade.load_texture(picture)

        # self.say_something = arcade.load_sound('')
    def say_hi(self, phrase):
        pass

    def say_hfjkdhdjkfhfdjskfh(self):
        pass

    def update(self):
        # print(f'всем ку, я - {self.name}, change_x: {self.change_x}')
        self.center_x += self.change_x
        # print(self.center_x, self.change_x, 'Center_x & change_x')

    def move (self):
        self.change_x = 1

    def stop_mid (self):
        self.change_x = 0
