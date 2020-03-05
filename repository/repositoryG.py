from domain.autobuz import Bus
from domain.trip import Trip

import pickle


class RepositoryGeneric:
    def __init__(self, fileName):
        """
        Creates the repository for the specific category( by filename)
        :param fileName: str, name of file for storage
        """
        self.__file = fileName
        self.__storage = {}
        self.__loadFile()

    def __loadFile(self):
        """
        Reads file and saves data in storage
        """
        try:
            with open(self.__file, 'rb') as file:
                self.__storage = pickle.load(file)
        except EOFError:
            pass
        except FileNotFoundError:
            print('File error!')

    def __writeFile(self):
        """
        Writes in file the new data from storage
        """
        try:
            with open(self.__file, 'wb') as file:
                pickle.dump(self.__storage, file)
        except FileNotFoundError:
            print('File error!')

    def addElement(self, entity):
        """
        Adds a new element in storage and re write it
        :param entity: object, the entity to add in storage
        """
        ID = entity.getID()
        if ID in self.__storage:
            raise ValueError("ID already existent!")
        self.__storage[ID] = entity
        self.__writeFile()

    def deleteElement(self, ID):
        """
        Deletes an element from storage and re write it
        :param ID: int, ID of the element
        """
        if ID in self.__storage:
            del self.__storage[ID]
            self.__writeFile()

    def getStorage(self):
        """
        Gives the storage as a list for easy acces
        :return: list of elements from storage
        """
        return list(self.__storage.values())

    def clear(self):
        """
        Clears the file
        """
        self.__storage.clear()
        self.__writeFile()



