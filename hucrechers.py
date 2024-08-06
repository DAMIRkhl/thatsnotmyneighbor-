import arcade


class Humans(arcade.Sprite):
    def __init__(self, human, appearance, ID, phone_number, apartment_number, floor, job, name,picture ="Charecters/image.jpg", scale=0.5):
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

