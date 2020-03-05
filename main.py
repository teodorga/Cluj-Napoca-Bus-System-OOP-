from repository.repositoryG import RepositoryGeneric

from logic.serviceBus import ServiceBus
from logic.serviceTrip import ServiceTrip

from tests.domainTests import *
from tests.repoTests import *
from tests.serviceTests import *

from UI.userInterface import UI

repoBus = RepositoryGeneric("BUS")
repoTrip = RepositoryGeneric("TRIP")

serviceBus = ServiceBus(repoBus, repoTrip)
serviceTrip = ServiceTrip(repoBus, repoTrip)

ui = UI(serviceBus, serviceTrip)
ui.mainConsole()
