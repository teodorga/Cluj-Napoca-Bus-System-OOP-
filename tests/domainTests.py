from domain.autobuz import Bus
from domain.trip import Trip


def test_Bus():
    entity = Bus(1, "24B")
    assert entity.getID() == 1
    assert entity.getLine() == "24B"


def test_Trip():
    entity = Trip(1, "24B", 3, 45)
    assert entity.getID() == 1
    assert entity.getLine() == "24B"
    assert entity.getCard() == 3
    assert entity.getTimestamp() == 45


test_Bus()
test_Trip()
