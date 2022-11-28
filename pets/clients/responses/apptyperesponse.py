# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = groupresponse_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, List

from pets.common.jsonparser import from_int, from_str, from_list, to_class


@dataclass
class AppTypeResponse:
    id: int
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'AppTypeResponse':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        return AppTypeResponse(id, name)

    def to_dict(self) -> dict:
        result: dict = {"id": from_int(self.id), "name": from_str(self.name)}
        return result


def apptyperesponse_from_dict(s: Any) -> List[AppTypeResponse]:
    return from_list(AppTypeResponse.from_dict, s)


def apptyperesponse_to_dict(x: List[AppTypeResponse]) -> Any:
    return from_list(lambda x: to_class(AppTypeResponse, x), x)
