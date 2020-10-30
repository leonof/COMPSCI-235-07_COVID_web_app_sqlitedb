import abc
from typing import List
from datetime import date

from covid.movie.model import *


repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):
    def getAllMovie(self):
        pass







