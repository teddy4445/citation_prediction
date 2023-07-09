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
    study_fields: str
    citations_all: str
    citations_since_2018: str
    h_index_all: str
    h_index_since_2018: str
    i10_index_all: str
    i10_index_since_2018: str
    articals: list

    @staticmethod
    def load_from_json(json_data: dict):
        answer = Author()
        # enter the core data
        answer.name = json_data["name"]
        # answer.study_fields = int(len(json_data['study_fields'].split(',')))
        # answer.citations_all = int(json_data["cited_by"]["citations_all"])
        # answer.citations_since_2018 = int(json_data['cited_by']['citations_since_2018'])
        # answer.h_index_all = int(json_data["cited_by"]["h_index_all"])
        # answer.h_index_since_2018 = int(json_data["cited_by"]["h_index_since_2018"])
        # answer.i10_index_all = int(json_data["cited_by"]["i10_index_all"])
        # answer.i10_index_since_2018 = int(json_data['cited_by']['i10_index_since_2018'])
        answer.citations_all = int(json_data["citations_all"])
        answer.citations_since_2018 = int(json_data['citations_since_2018'])
        answer.h_index_all = int(json_data["h_index_all"])
        answer.h_index_since_2018 = int(json_data["h_index_since_2018"])
        answer.i10_index_all = int(json_data["i10_index_all"])
        answer.i10_index_since_2018 = int(json_data['i10_index_since_2018'])
        answer.articles = []
        return answer
