# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = groupresponse_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, List

from pets.common.jsonparser import from_int, from_str


@dataclass
class GroupResponse:
    id: int
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'GroupResponse':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        return GroupResponse(id, name)

    def to_dict(self) -> dict:
        result: dict = {"id": from_int(self.id), "name": from_str(self.name)}
        return result


def groupresponse_from_dict(s: Any) -> List[GroupResponse]:
    return from_list(GroupResponse.from_dict, s)


def groupresponse_to_dict(x: List[GroupResponse]) -> Any:
    return from_list(lambda x: to_class(GroupResponse, x), x)
