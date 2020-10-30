from datetime import date

from covid.movie.model import *

import pytest


@pytest.fixture()
def movie():
    return Movie(
        'Year 1983',2019
    )


def test_movie_construction(movie):
    assert movie.title == 'Year 1983'
    assert movie.year == 2019
    