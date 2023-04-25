# library imports
import dataclasses
from dataclasses import dataclass


@dataclass(init=False)
class Model:
    """
    An abstract class that all data model classes implements to make sure we can make recursive actions
    """

    @staticmethod
    def load_from_json(json_data: dict):
        answer = Model()
        return answer

    def __str__(self):
        """
        Returns a string containing only the non-default field values
        """
        s = ", ".join(
            f"{field.name}={getattr(self, field.name)!r}"
            for field in dataclasses.fields(self)
        )
        return f"{type(self).__name__}({s})"

    def __repr__(self):
        return self.__str__()