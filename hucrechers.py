import arcade


class Humans(arcade.Sprite):
    def __init__(self, appearance, ID, phone_number, apartment_number, floor, job, name):
        super().__init__(filename=appearance, scale=2)
        self.appearance = appearance
        self.ID = ID
        self.phone_number = phone_number
        self.apartment_number = apartment_number
        self.floor = floor
        self.job = job
        self.name = name
