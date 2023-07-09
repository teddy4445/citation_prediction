# library imports
import dataclasses
from dataclasses import dataclass

# project imports
from consts import ERROR_VAL
from models.model import Model
from nlp_model import NLPmodel


@dataclass(init=False)
class Paper(Model):
    """
    A data class to holder all we need for a paper
    """
    # core data
    title_name: str
    co_authors: list
    journal_name: str
    publish_year: int
    citations_per_year: list  # this is the "y" column
    cited_by: str
    # processed data
    title_encoded: list
    abstract_encoded: list
    co_authors_count: int
    journal_h_index: int
    publish_type: str
    journal_q_index: int
    journal_impact_factor: int

    def use_nlp_model(self,
                      nlp_model: NLPmodel):
        self.title_encoded = nlp_model.run(text=self.title)
        self.abstract_encoded = nlp_model.run(text=self.abstract)

    def update_journal_data(self,
                            journal_q_index: int,
                            journal_impact_factor: int,
                            journal_citations: int):
        self.journal_q_index = journal_q_index
        self.journal_impact_factor = journal_impact_factor
        self.journal_citations = journal_citations

    @staticmethod
    def load_from_json(json_data: dict):
        answer = Paper()
        # enter the core data
        answer.title_name = json_data["name"]
        #answer.co_authors = json_data["co_authors"].split(",") if "," in json_data["co_authors"] else json_data["co_authors"]
        answer.journal_name = json_data["publication_name"]
        answer.publish_year = json_data["publish_year"]
        #answer.citations_per_year = json_data["citations_per_year"]  # TODO: make sure with Alexi this is the name she uses
        #answer.publish_type = json_data['publication_type']
        # init empty the process data
        answer.cited_by = json_data['cited_by']
        answer.title_encoded = None
        answer.abstract_encoded = None
        #answer.co_authors_count = len(answer.co_authors)
        answer.journal_q_index = ERROR_VAL
        answer.journal_citations = ERROR_VAL
        answer.journal_impact_factor = ERROR_VAL
        return answer
