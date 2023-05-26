# library imports
import sys

sys.setrecursionlimit(1500)
import clarivate.wos_journals.client
from clarivate.wos_journals.client.api import journals_api

# project imports
from journal_data_apis.journal_data_fatch import JournalDataFatch

class JournalDataFatchWOS(JournalDataFatch):
    """
    A class to get the needed data about a journal from its name
    Note, run 'pip install git+https://github.com/clarivate/wosjournals-python-client.git' to make this class work
    """

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
        # See configuration.py for a list of all supported configuration parameters.

        configuration = clarivate.wos_journals.client.Configuration()
        configuration.api_key['key'] = 'YOUR API KEY'  # TODO: we need to get an API

        # Enter a context with an instance of the API client
        with clarivate.wos_journals.client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = journals_api.JournalsApi(api_client)
            # example passing only required values which don't have defaults set
            try:
                # Get journal metrics for a year
                api_response = api_instance.journals_id_reports_year_year_get(journal_name,
                                                                              lookup_year)
                api_response_metrics = api_response["metrics"]
                return {"impact_factor": int(api_response_metrics["impact_metrics"]["jif"]),
                        "citations": int(api_response_metrics["impact_metrics"]["total_cites"]),
                        "q_index": round(float(api_response_metrics["source_metrics"]["jif_percentile"])*4)}  # TODO: we assume the value is between 0-1, if it is between 0-100, divide by zero before rounding
            except clarivate.wos_journals.client.ApiException as e:
                print("Exception when calling JournalsApi->journals_id_reports_year_year_get: {}\n".format(e))
