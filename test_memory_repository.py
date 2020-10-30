from datetime import date, datetime
from typing import List

import pytest

from covid.domain.model import User, Article, Tag, Comment, make_comment
from covid.adapters.repository import RepositoryException


def test_repository_can_get_all_movie(in_memory_repo):

    movies = in_memory_repo.getAllMovie()

    assert len(movies)==1000