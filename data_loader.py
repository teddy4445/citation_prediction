# library imports
import os
import json
import pandas as pd
from glob import glob
import sys
sys.setrecursionlimit(1500)
import clarivate.wos_journals.client
from clarivate.wos_journals.client.api import journals_api
from clarivate.wos_journals.client.model.journal_list import JournalList

# project imports
from consts import *
from nlp_model import NLPmodel
from models.paper import Paper
from models.author import Author
from models.sample import Sample
from journal_data_fatch import JournalDataFatch


class DataLoader:
    """
    A class to load the data and process it into an all-numerical data using cross data
    """

    def __init__(self):
        pass

    @staticmethod
    def run(data_path: str) -> pd.DataFrame:
        papers = []
        authors = {}
        for file_path in glob(os.path.join(data_path, "*.json")):
            # load file
            with open(file_path, "r") as json_data_file:
                author_json = json.load(json_data_file)
            # process the needed data on the author level for later
            authors[author_json["name"]] = Author.load_from_json(json_data=author_json)
            # process the basic data of the papers and the author
            papers.extend([Paper.load_from_json(json_data=paper_item) for paper_item in author_json["articles"]])

        # start run on the data and cross it to generate samples to analyze
        samples = []
        journals_data = {}  # name is the key, the journal_h_index, journal_q_index, and journal_impact_factor are the values
        nlp_model = NLPmodel()
        for paper in papers:
            # use models to process the paper data to something we can use
            # TODO: for the specific paper, update it using the next method
            paper.update_journal_data(journal_h_index=0,
                                      journal_q_index=0,
                                      journal_impact_factor=0)
            # TODO: Teddy - I start an option for the NLP model in the below class
            paper.use_nlp_model(nlp_model=nlp_model)

            # TODO: gather data from the web to get the data about journals - try https://github.com/clarivate/wosjournals-python-client
            # TODO: once you learn the data about a journal, save it for later so you do not need to query it twice but just ref to it and use it again
            JournalDataFatch.run(journal_name=paper.journal_name,
                                 lookup_year=paper.publish_year)

            samples.append(Sample.create(paper=paper,
                                         authors=[authors[author_name] for author_name in paper.co_authors]))
        # convert the data into pd.DataFrame with meaningful column names
        return samples  # TODO: fix here
