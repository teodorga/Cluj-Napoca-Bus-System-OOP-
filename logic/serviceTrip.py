from domain.trip import Trip
from logic.validators import Validate

import time


class ServiceTrip:
    def __init__(self, repoBus, repoTrip):
        self.__repoBus = repoBus
        self.__repoTrip = repoTrip

    def add(self, ID, line, card, seconds):
        """
        Read parameters, creates entity and add in storage
        """
        try:
            exists = False

            for element in self.__repoBus.getStorage():
                if element.getLine() == line:
                    newEntity = Trip(ID, line, card, seconds)
                    Validate.validateTrip(newEntity)
                    self.__repoTrip.addElement(newEntity)
                    exists = True
            if exists is False:
                print("Line doesn't exists!")
        except ValueError as error:
            print(error)

    def delete(self):
        """
        Read ID and delete entity from storage
        """
        try:
            ID = int(input("ID: "))
            self.__repoTrip.deleteElement(ID)
        except ValueError as error:
            print(error)

    def printStorage(self):
        """
        Print all the elements from storage list
        """
        for entity in self.__repoTrip.getStorage():
            print(entity)

    def getAll(self):
        """
        Return storage
        :return: storage of elements
        """
        return list(self.__repoTrip.getStorage())

    def linesValidations(self, line):
        """
        Creates a list with all line validations
        :param line: string, Line to be checked
        :return: list of lines
        """
        elements = []

        for trip in self.__repoTrip.getStorage():
            if trip.getLine() == line:
                elements.append(trip)

        return elements

    def taxedCard(self):
        """
        Sort the groups of timestamps and lines and calculate if a line is taxed or not
        :return: final list with all details
        """
        cards = []
        trips = []

        cardTaxed = []
        finalList = []

        exists = False

        for trip in self.__repoTrip.getStorage():
            for element in cards:
                if element == trip.getCard():
                    exists = True
            if exists is False:
                cards.append(trip.getCard())
            exists = False

        for card in cards:
            for trip in self.__repoTrip.getStorage():
                if trip.getCard() == card:
                    trips.append(trip)

            trips = sorted(trips, key=lambda trip: trip.getTimestamp())

            timeCounter = 0
            for trip in trips:
                if timeCounter == 0:
                    timeCounter = timeCounter + trip.getTimestamp()
                    string = "{}* ({})".format(trip.getLine(), trip.getTimestamp())
                    cardTaxed.append(string)
                else:
                    timeCounter = timeCounter + trip.getTimestamp()
                    if timeCounter > 3600:
                        string = "{}* ({})".format(trip.getLine(), trip.getTimestamp())
                    else:
                        string = "{} ({})".format(trip.getLine(), trip.getTimestamp())
                    cardTaxed.append(string)

            finalElement = [card, cardTaxed]
            finalList.append(finalElement)

            cardTaxed = []
            trips = []

        return finalList

