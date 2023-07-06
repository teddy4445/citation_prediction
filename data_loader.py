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
DATA_FOLDER_NAME = "data"
RESULTS_FOLDER_NAME = "results"

RESULTS_FOLDER = os.path.join(os.path.dirname(__file__), RESULTS_FOLDER_NAME)
PROCESSED_DATA_PATH = os.path.join(os.path.dirname(__file__), RESULTS_FOLDER_NAME, "processed_data_per.csv")


class DataLoader:
    """
    A class to load the data and process it into an all-numerical data using cross data
    """

    def __init__(self):
        pass

    @staticmethod
    def run(data_path: str) -> pd.DataFrame:

        for file_path in glob(os.path.join(data_path, "*.json")):
            # load file
            # with open(file_path, "r") as json_data_file:
            #     author_json = json.load(json_data_file)
            json_file = open(file_path,'r')
            json_lines = json_file.readlines()
            full_data = []
            c = 0
            for json_line in json_lines[:5]:
            # will be all jsons not only one
                c += 1
                author_json = json.loads(json_line)
                papers = []
                authors = {}
                # process the needed data on the author level for later
                authors[author_json["name"]] = Author.load_from_json(json_data=author_json)
                # process the basic data of the papers and the author
                papers.extend([Paper.load_from_json(json_data=paper_item) for paper_item in author_json["articles"]])

                # start run on the data and cross it to generate samples to analyze
                samples = []
                authors[author_json["name"]].__dict__['articles'] = []
                journals_data = {}
                for paper in papers:

                    try:
                        j_answer = journals_data[paper.title_name][paper.publish_year]
                    except:
                        j_answer = JournalDataFatchScopus.run(journal_name=paper.title_name,
                                                              lookup_year=paper.publish_year)

                        try:
                           journals_data[paper.title_name][paper.publish_year] = j_answer
                        except:
                            journals_data[paper.title_name] = {}
                            journals_data[paper.title_name][paper.publish_year] = j_answer

                    paper.update_journal_data(journal_citations=j_answer["citations"],
                                              journal_q_index=j_answer["q_index"],
                                              journal_impact_factor=j_answer["impact_factor"])

                    single_sample = Sample.create(paper=paper, authors=[authors[author_json["name"]]]).__dict__
                    authors[author_json["name"]].__dict__['articles'].append({'publish_year': single_sample['publish_year'],'q_at_year':single_sample['journal_q_index'],'cited_by': single_sample['cited_by']})

                full_data.append(authors[author_json["name"]].__dict__)
                # samples.append(Sample.create(paper=paper,
                #                              authors=[authors[author_name] for author_name in paper.co_authors if author_name in [*authors]]))
            # convert the data into pd.DataFrame with meaningful column names
            #columns = [*vars(samples[0])] if len(samples) > 0 else []
                columns = [*full_data[0]] if len(full_data) > 0 else []

                samples = pd.DataFrame(full_data, columns=columns)
                samples.to_csv(PROCESSED_DATA_PATH,
                           index=False)
                print(c)
        columns = [*full_data[0]] if len(full_data) > 0 else []

        samples = pd.DataFrame(full_data, columns=columns)
        return samples  # TODO: fix here

