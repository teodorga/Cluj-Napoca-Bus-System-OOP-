from domain.entity import Entity


class Bus(Entity):
    def __init__(self, ID, line):
        super().__init__(ID)
        self.__line = line

    def __str__(self):
        return '- {} | Line: {}'.format(self.getID(),
                                        self.__line)

    def getLine(self):
        return self.__line
