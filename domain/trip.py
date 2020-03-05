from domain.entity import Entity


class Trip(Entity):
    def __init__(self, ID, line, card, timestamp):
        super().__init__(ID)
        self.__line = line
        self.__card = card
        self.__timestamp = timestamp

    def __str__(self):
        return '- {} | Line: {}, Card: {}, Timestamp: {}'.format(self.getID(),
                                                                 self.__line,
                                                                 self.__card,
                                                                 self.__timestamp)

    def getLine(self):
        return self.__line

    def getCard(self):
        return self.__card

    def getTimestamp(self):
        return self.__timestamp
