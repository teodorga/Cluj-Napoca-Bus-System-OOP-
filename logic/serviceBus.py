from domain.autobuz import Bus
from repository.repositoryG import RepositoryGeneric
from logic.validators import Validate


class ServiceBus:
    def __init__(self, repoBus, repoTrip):
        self.__repoBus = repoBus
        self.__repoTrip = repoTrip

    def add(self, ID, line):
        """
        Read parameters, creates entity and add in storage
        """
        try:
            newEntity = Bus(ID, line)
            Validate.validateBus(newEntity)
            for element in self.__repoBus.getStorage():
                if element.getLine() == line:
                    raise ValueError("Line already exists!")
            self.__repoBus.addElement(newEntity)
        except ValueError as error:
            print(error)

    def delete(self):
        """
        Read ID and delete entity from storage
        """
        try:
            ID = int(input("ID: "))
            self.__repoBus.deleteElement(ID)
        except ValueError as error:
            print(error)

    def printStorage(self):
        """
        Print all the elements from storage list
        """
        for entity in self.__repoBus.getStorage():
            print(entity)

    def getAll(self):
        """
        Return storage
        :return: storage of elements
        """
        return list(self.__repoBus.getStorage())

    def sortBusesTrips(self):
        """
        Sort buses by the number of validations ( trips )
        :return: list of all validations ( trips ) by a specific bus line
        """
        elements = []
        counter = 0

        for line in self.__repoBus.getStorage():
            for trip in self.__repoTrip.getStorage():
                if trip.getLine() == line.getLine():
                    counter = counter + 1
            element = [line, counter]
            elements.append(element)
            counter = 0

        elements = sorted(elements, key=lambda element: element[1], reverse=True)

        return elements

