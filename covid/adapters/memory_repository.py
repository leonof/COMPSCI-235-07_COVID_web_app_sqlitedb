import csv
import os
from datetime import date, datetime
from typing import List

from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash

from covid.adapters.repository import AbstractRepository, RepositoryException
from covid.movie.model import *

class MemoryRepository(AbstractRepository):
    # Articles ordered by date, not id. id is assumed unique.

    def __init__(self):
        self._articles = list()
        self._articles_index = dict()
        self._tags = list()
        self._users = list()
        self._comments = list()

    


def read_csv_file(filename: str):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row


def load_articles_and_tags(data_path: str, repo: MemoryRepository):
    tags = dict()

    for data_row in read_csv_file(os.path.join(data_path, 'Data1000Movies.csv')):
        movie = Movie(
            name=data_row[1],year = data_row[6]

        )

        # Add the Article to the repository.
        repo.add_movie(movie)





def populate(data_path: str, repo: MemoryRepository):
    # Load articles and tags into the repository.
    load_articles_and_tags(data_path, repo)

    # Load users into the repository.
    users = load_users(data_path, repo)

    # Load comments into the repository.
    load_comments(data_path, repo, users)
