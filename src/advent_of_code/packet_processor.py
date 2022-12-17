# The start of a packet is indicated by a sequence of four characters that are all different.

# mjqjpqmgbljsphdztnvjfqwrcgsmlb

def findMarker(data):

    dataBuffer = list(data)

    packet = Packet()

    while not packet.markerFound():
        packet.add(dataBuffer.pop())

    return packet.markerPosition

class Packet:
    def __init__(self, data=""):
        self.buffer = list(data)
        self.markerPosition = 1

    def add(self, d):
        if self.isDuplicate(d):
            self.clearDuplicate(d)

        self.buffer.append(d)

        self.markerPosition += 1

    def isDuplicate(self, d):
        return self.buffer.count(d) > 0

    def clearDuplicate(self, d):
        while len(self.buffer) > 0 :
            b = self.buffer.pop()

            if b == d:
                return

    def needsMoreData(self):
        return len(self.buffer) < 4

    def markerFound(self):

        if self.needsMoreData():
            return False

        for b in self.buffer:
            if self.buffer.count(b) > 1:
                return False
        
        return True