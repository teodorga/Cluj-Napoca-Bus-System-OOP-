from domain.autobuz import Bus
from domain.trip import Trip

from logic.validators import Validate
from repository.repositoryG import RepositoryGeneric

from logic.serviceBus import ServiceBus
from logic.serviceTrip import ServiceTrip


def test_Service():
    busRepo = RepositoryGeneric("TEST BUS")
    tripRepo = RepositoryGeneric("TEST TRIP")

    busRepo.clear()
    tripRepo.clear()

    busService = ServiceBus(busRepo, tripRepo)
    tripService = ServiceTrip(busRepo, tripRepo)

    bus = Bus(1, "24B")
    busService.add(bus.getID(), bus.getLine())
    for el in busService.getAll():
        assert el.getID() == 1
        assert el.getLine() == '24B'

    trip = Trip(1, "24B", 3, 5)
    tripService.add(trip.getID(), trip.getLine(), trip.getCard(), trip.getTimestamp())
    for el in tripService.getAll():
        assert el.getID() == 1
        assert el.getLine() == "24B"
        assert el.getCard() == 3
        assert el.getTimestamp() == 5


test_Service()


