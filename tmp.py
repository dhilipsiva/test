class Room(object):

    def __init__(self, l, b):
        self.l = l
        self.b = b

    def show(self):
        print "Area of room: %d" % (self.l * self.b, )


class BedRoom(Room):

    def __init__(self, l, b, color):
        super(BedRoom, self).__init__(l, b)
        self.color = color

    def show(self):
        super(BedRoom, self).show()
        print "And it is %s color" % self.color

room = BedRoom(4, 5, 'yellow')
room.show()
