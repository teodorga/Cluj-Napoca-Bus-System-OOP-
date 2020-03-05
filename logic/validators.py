class Validate:

    @staticmethod
    def validateBus(entity):
        if not isinstance(entity.getID(), int):
            raise ValueError("Wrong ID!")
        if len(entity.getLine()) == 0:
            raise ValueError("Name lenght 0!")

    @staticmethod
    def validateTrip(entity):
        if not isinstance(entity.getID(), int):
            raise ValueError("Wrong ID!")
        if entity.getCard() < 0:
            raise ValueError("Card number negative!")
        if entity.getTimestamp() < 0:
            raise ValueError("Seconds number negative!")