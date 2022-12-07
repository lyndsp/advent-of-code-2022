class Assignment:
    def __init__(self, definition):
        parts = definition.split("-")

        self.start = int(parts[0])
        self.end = int(parts[1])

    @classmethod
    def parsePair(cls, pairDefinition):
        definitions = pairDefinition.split(",")

        pair = list()

        pair.append(cls(str(definitions[0])))
        pair.append(cls(str(definitions[1])))

        return pair
        