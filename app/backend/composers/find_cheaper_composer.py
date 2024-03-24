from ..infra.db.repositories.transport import TransportRepo
from ..data.use_cases.find_cheaper import FindCheaper
from ..presentation.controllers.find_cheaper_controller import FindCheaperController

#composer of the serach for the more confortable trip
def find_cheaper_composer():

    repository = TransportRepo()
    use_case = FindCheaper(repository)
    controller = FindCheaperController(use_case)

    return controller.handle
