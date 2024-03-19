from ..infra.db.repositories.transport import TransportRepo
from ..data.use_cases.find_confort import FindConfort
from ..presentation.controllers.find_confort_controller import FindConfortController

def find_confort_composer():

    repository = TransportRepo()
    use_case = FindConfort(repository)
    controller = FindConfortController(use_case)

    return controller.handle
