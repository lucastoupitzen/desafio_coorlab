from ..interfaces.controller_interface import ControllerInterface
from ...domain.use_cases.find_confort import FindConfortInterface
from ..http_types.http_request import HttpRequest
from ..http_types.http_response import HttpResponse

class FindConfortController(ControllerInterface):

    def __init__(self, use_case: FindConfortInterface) -> None:

        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        
        city : str = http_request.query_params["city"]

        response = self.__use_case.find_confort(city=city)

        if response:
            return HttpResponse (
                    status_code= 200,
                    body= {
                        "data": response
                    }
                )
        
        return HttpResponse (
	            status_code= 400,
	            body= {
	                "data": "City Not Found"
	            }
	        )
    