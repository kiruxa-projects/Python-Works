class SomeClass:

    def __init__(self):
        self.state = "A"

    def add(self):
        if (self.state == "A"):
            self.state = "E"
            return 1
        elif (self.state == "C"):
            self.state = "D"
            return 3
        elif (self.state == "D"):
            self.state = "A"
            return 5
        elif (self.state == "E"):
            self.state = "A"
            return 8
        else:
            raise KeyError(self.state)

    def crawl(self):
        if (self.state == "A"):
            self.state = "B"
            return 0
        elif (self.state == "B"):
            self.state = "C"
            return 2
        elif (self.state == "D"):
            self.state = "E"
            return 4
        elif (self.state == "E"):
            self.state = "F"
            return 6
        else:
            raise KeyError(self.state)

    def bend(self):
        if (self.state == "E"):
            self.state = "C"
            return 7
        else:
            raise KeyError(self.state)


def main():
    return SomeClass()
