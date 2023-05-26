# library imports
import math
from pyscopus import Scopus

# project imports
from journal_data_apis.journal_data_fatch import JournalDataFatch


class JournalDataFatchScopus(JournalDataFatch):
    """
    A class to get the needed data about a journal from its name, using the scopus API
    """

    KEY = "e849bb8cd07641cc6b57b599bcc64595"

    def __init__(self):
        JournalDataFatch.__init__(self)

    @staticmethod
    def run(journal_name: str,
            lookup_year: int) -> dict:
        """
        A single function for this class
        :param journal_name: the name of the journal we wish to query
        :param lookup_year: the year we wish to get the data for
        :return: a dict with the h-index, impact factor, and journal_q_index of the journal in the wanted year
        """
        scopus = Scopus(JournalDataFatchScopus.KEY)
        meta_df, citescore_df, sj_rank_df = scopus.search_serial(journal_name)
        percentile = int(sj_rank_df[sj_rank_df["year"] == str(lookup_year)]["percentile"])
        filtered_year = citescore_df[citescore_df["year"] == str(lookup_year)]
        # an edge case for the last journal in the ranking
        if percentile == 0:
            percentile = 1
        return {"impact_factor": int(list(filtered_year["citeScore"])[0]),
                "citations": int(list(filtered_year["citationCount"])[0]),
                "q_index": 5 - math.ceil(percentile/25)}

