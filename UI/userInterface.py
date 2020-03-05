class UI:
    def __init__(self, serviceBus, serviceTrip):
        self.__serviceBus = serviceBus
        self.__serviceTrip = serviceTrip

    @staticmethod
    def __mainMenu():
        print("\n")
        print("1. Buses")
        print("2. Validations")
        print("\033[32m-----------\033[0m")
        print("3. Print validations for a line")
        print("4. Sort buses by number of validations")
        print("5. Paid trips for every card ID ( if bus line has '*' -> is a paid trip). "
              "A paid trip is when 2 trips are made if 60 minutes did not passed")


    @staticmethod
    def __BusMenu():
        print("\n")
        print("\033[32mBuses\033[0m")
        print("1. Add")
        print("2. Show")
        print("\033[31m3. Back\033[0m")

    @staticmethod
    def __TripMenu():
        print("\n")
        print("\033[32mValidations\033[0m")
        print("1. Add")
        print("2. Show")
        print("\033[31m3. Back\033[0m")

    def mainConsole(self):
        try:
            while True:
                self.__mainMenu()
                command = int(input("Command: "))
                if command == 1:
                    self.__BusConsole()
                if command == 2:
                    self.__TripConsole()
                if command == 3:
                    line = input("Line to check: ")
                    self.functionality3(line)
                if command == 4:
                    self.functionality4()
                if command == 5:
                    self.functionality5()
        except ValueError:
            print("Wrong command!")
            self.mainConsole()

    def __BusConsole(self):
        try:
            while True:
                self.__BusMenu()
                command = int(input("Command: "))
                if command == 1:
                    try:
                        ID = int(input("ID: "))
                        line = input("Line: ")

                        self.__serviceBus.add(ID, line)
                    except ValueError:
                        print("Reading ERROR!")
                if command == 2:
                    self.__serviceBus.printStorage()
                if command == 3:
                    self.mainConsole()

        except ValueError:
            print("Wrong command!")
            self.__BusConsole()

    def __TripConsole(self):
        try:
            while True:
                self.__TripMenu()
                command = int(input("Command: "))
                if command == 1:
                    try:
                        ID = int(input("ID: "))
                        line = input("Line: ")
                        card = int(input("Card: "))
                        seconds = int(input("Seconds: "))

                        self.__serviceTrip.add(ID, line, card, seconds)
                    except ValueError:
                        print("Reading ERROR")
                if command == 2:
                    self.__serviceTrip.printStorage()
                if command == 3:
                    self.mainConsole()
        except ValueError:
            print("Wrong command!")
            self.__TripConsole()

    def functionality3(self, line):
        """
        Recieve the result and prints using some design
        :return:
        """
        elements = self.__serviceTrip.linesValidations(line)
        for element in elements:
            print(element)

    def functionality4(self):
        """
        Recieve the result and prints using some design
        :return:
        """
        elements = self.__serviceBus.sortBusesTrips()
        for element in elements:
            print(element[0], "TRIPS:", element[1])

    def functionality5(self):
        """
        Recieve the result and prints using some design
        :return:
        """
        elements = self.__serviceTrip.taxedCard()
        for element in elements:
            print(str(element[0])+':', end=' ')
            for el in element[1]:
                print(el, end=', ')
            print('\n')

