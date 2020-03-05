from domain.autobuz import Bus
from domain.trip import Trip

from repository.repositoryG import RepositoryGeneric

import pickle


def test_repository():
    repoGeneric = RepositoryGeneric("TEST")

    newEntity = Bus(1, "24B")
    repoGeneric.addElement(newEntity)
    elements = repoGeneric.getStorage()
    assert len(elements) == 1

    repoGeneric.deleteElement(1)
    elements = repoGeneric.getStorage()
    assert len(elements) == 0

    with open("TEST", 'w') as file:
        file.close()

    repoGeneric = RepositoryGeneric("TEST")

    newEntity = Trip(1, "24B", 3, 4)
    repoGeneric.addElement(newEntity)
    elements = repoGeneric.getStorage()
    assert len(elements) == 1

    repoGeneric.deleteElement(1)
    elements = repoGeneric.getStorage()
    assert len(elements) == 0

    with open("TEST", 'w') as file:
        file.close()


test_repository()


