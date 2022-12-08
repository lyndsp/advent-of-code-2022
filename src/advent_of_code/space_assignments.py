class Assignment:
    def __init__(self, definition):
        parts = definition.split("-")

        self.start = int(parts[0])
        self.end = int(parts[1])

    def contains(self, otherAssignment):
        return self.start <= otherAssignment.start and self.end >= otherAssignment.end

    def overlaps(self, otherAssignment):
        return self.startOverlaps(otherAssignment) or self.endOverlaps(otherAssignment)

    def startOverlaps(self, otherAssignment):
        return self.start == otherAssignment.start or \
            self.start > otherAssignment.start and self.start <= otherAssignment.end
            
    def endOverlaps(self, otherAssignment):
        return self.end == otherAssignment.end or \
            self.end < otherAssignment.end and self.end >= otherAssignment.start
            
    @classmethod
    def parsePair(cls, pairDefinition):
        definitions = pairDefinition.split(",")

        pair = list()

        pair.append(cls(str(definitions[0])))
        pair.append(cls(str(definitions[1])))

        return pair
        