# The start of a packet is indicated by a sequence of four characters
# that are all different.
# mjqjpqmgbljsphdztnvjfqwrcgsmlb

def find_marker(data):

    data_buffer = list(data)

    packet = Packet()

    while not packet.markerFound():
        packet.add(data_buffer.pop(0))

    return packet.markerPosition


class Packet:
    def __init__(self, data=""):
        self.buffer = list(data)
        self.markerPosition = 0

    def add(self, d):
        if self.isDuplicate(d):
            self.clearDuplicate(d)

        self.buffer.append(d)

        self.markerPosition += 1

    def isDuplicate(self, d):
        return self.buffer.count(d) > 0

    def clearDuplicate(self, d):
        while len(self.buffer) > 0 :
            b = self.buffer.pop(0)

            if b == d:
                return

    def needsMoreData(self):
        return len(self.buffer) < 14

    def markerFound(self):

        if self.needsMoreData():
            return False

        for b in self.buffer:
            if self.buffer.count(b) > 1:
                return False

        return True
