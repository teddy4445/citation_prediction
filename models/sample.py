# library imports
import numpy as np
import dataclasses
from dataclasses import dataclass

# project imports
from consts import ERROR_VAL
from models.model import Model
from models.paper import Paper
from models.author import Author


@dataclass(init=False)
class Sample(Model):
    """
    A data class to holder all we need for a sample for the model
    """
    # core data
    title_encoded: list
    abstract_encoded: list
    co_authors_count: int
    co_authors_h_index_avg: float
    co_authors_citation_avg: float
    co_authors_i10_avg: float
    co_authors_h_index_max: int
    co_authors_citation_max: int
    co_authors_i10_max: int
    journal_q_index: int
    journal_citations: int
    journal_impact_factor: int
    publish_year: int
    citations_per_year: list  # this is the "y" column

    # processed data

    @staticmethod
    def create(paper: Paper,
               authors: list):
        answer = Sample()
        # enter the core data
        answer.title_encoded = paper.title_encoded
        answer.abstract_encoded = paper.abstract_encoded
        answer.co_authors_count = paper.co_authors_count
        answer.co_authors_citation_avg = np.mean([author.citations for author in authors])
        answer.co_authors_h_index_avg = np.mean([author.h_index for author in authors])
        answer.co_authors_i10_avg = np.mean([author.i10_index for author in authors])
        answer.co_authors_citation_max = np.max([author.citations for author in authors])
        answer.co_authors_h_index_max = np.max([author.h_index for author in authors])
        answer.co_authors_i10_max = np.max([author.i10_index for author in authors])
        answer.journal_q_index = paper.journal_q_index
        answer.journal_citations = paper.journal_citations
        answer.journal_impact_factor = paper.journal_impact_factor
        answer.citations_per_year = paper.citations_per_year
        return answer
