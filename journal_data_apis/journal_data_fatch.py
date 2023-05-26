# library imports

class JournalDataFatch:
    """
    A class to get the needed data about a journal from its name - abstract
    """

    def __init__(self):
        pass

    @staticmethod
    def run(journal_name: str,
            lookup_year: int) -> dict:
        """
        A single function for this class
        :param journal_name: the name of the journal we wish to query
        :param lookup_year: the year we wish to get the data for
        :return: a dict with the h-index, impact factor, and journal_q_index of the journal in the wanted year
        """
        return {"impact_factor": None,
                "citations": None,
                "q_index": None}
