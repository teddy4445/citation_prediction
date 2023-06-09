# library imports
import json
import pandas as pd
from glob import glob

# project imports
from consts import *
from nlp_model import NLPmodel
from models.paper import Paper
from models.author import Author
from models.sample import Sample
from journal_data_apis.journal_data_fatch_scopus import JournalDataFatchScopus


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
            # with open(file_path, "r") as json_data_file:
            #     author_json = json.load(json_data_file)
            json_file = open(file_path,'r')
            json_lines = json_file.readlines()
            # will be all jsons not only one
            author_json = json.loads(json_lines[0])
            # process the needed data on the author level for later
            authors[author_json["name"]] = Author.load_from_json(json_data=author_json)
            # process the basic data of the papers and the author
            papers.extend([Paper.load_from_json(json_data=paper_item) for paper_item in author_json["articles"]])

        # start run on the data and cross it to generate samples to analyze
        samples = []
        journals_data = {}
        for paper in papers:

            try:
                j_answer = journals_data[paper.journal_name][paper.publish_year]
            except:
                if paper.publish_type != 'Journal':
                    continue
                j_answer = JournalDataFatchScopus.run(journal_name=paper.journal_name,
                                                      lookup_year=paper.publish_year)
                try:
                   journals_data[paper.journal_name][paper.publish_year] = j_answer
                except:
                    journals_data[paper.journal_name] = {}
                    journals_data[paper.journal_name][paper.publish_year] = j_answer

            paper.update_journal_data(journal_citations=j_answer["citations"],
                                      journal_q_index=j_answer["q_index"],
                                      journal_impact_factor=j_answer["impact_factor"])

            samples.append(Sample.create(paper=paper,
                                         authors=[authors[author_name] for author_name in paper.co_authors]))
        # convert the data into pd.DataFrame with meaningful column names
        return samples  # TODO: fix here

