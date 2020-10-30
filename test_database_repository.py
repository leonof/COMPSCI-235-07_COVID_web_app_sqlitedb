from datetime import date, datetime

import pytest

from covid.adapters.database_repository import SqlAlchemyRepository
from covid.movie.model import *
from covid.adapters.repository import RepositoryException

def test_repository_can_get_all_movie(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    movies = repo.getAllMovie()

    assert len(movies)==1000



