class Car :

    def __init__(self, color = "white"):
        self.color = color
        self.milege = 0

    def drive(self, km):
        self.milege += km
        msg = f"{km}kmドライブしました。総距離は{self.milege}kmです。"
        print(msg)
