# library imports
import dataclasses
from dataclasses import dataclass

# project imports
from consts import ERROR_VAL
from models.model import Model


@dataclass(init=False)
class Author(Model):
    """
    A data class to holder all we need for an author
    """
    # core data
    name: str
    h_index: str
    citations: list
    i10_index: str
    papers_count: int

    @staticmethod
    def load_from_json(json_data: dict):
        answer = Author()
        # enter the core data
        answer.name = json_data["name"]
        answer.papers_count = len(json_data["articles"])
        answer.citations = int(json_data["cited_by"]["citations_all"])
        answer.h_index = int(json_data["cited_by"]["h_index_all"])
        answer.i10_index = int(json_data["cited_by"]["i10_index_all"])
        return answer
