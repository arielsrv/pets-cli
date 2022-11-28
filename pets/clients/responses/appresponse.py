from dataclasses import dataclass
from typing import Any

from pets.common.jsonparser import from_int, from_str, to_class


@dataclass
class App:
    id: int
    url: str

    @staticmethod
    def from_dict(obj: Any) -> 'App':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        url = from_str(obj.get("url"))
        return App(id, url)

    def to_dict(self) -> dict:
        result: dict = {"id": from_int(self.id), "url": from_str(self.url)}
        return result


def app_from_dict(s: Any) -> App:
    return App.from_dict(s)


def app_to_dict(x: App) -> Any:
    return to_class(App, x)
