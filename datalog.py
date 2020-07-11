from datetime  import datetime

class Datalog:
    def __init__(self):
        self.loglist = []

    def log(self, data):
        now = datetime.now() #現在の日時データ
        item = (now, data)
        self.loglist.append(item)
