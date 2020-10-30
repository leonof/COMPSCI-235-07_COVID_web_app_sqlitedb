import pytest

import datetime

from sqlalchemy.exc import IntegrityError

from covid.movie.model import *

import time
now=time.time()
article_date = datetime.fromtimestamp(now)

def insert_movie(empty_session, values=None):
    rank = "1001"
    title = "test_title"
    genre = 'test_genre'
    description = 'test_description'
    director = 'test_director'
    actors = 'test_actors'
    year = '2020'
    runtime = '60'
    rating = '9'
    votes = '10'
    revenue = '12'
    metascore = '1'


    if values is not None:
        rank = values[0]
        title = values[1]
        description = values[2]
        director    =values[3]
        actors      =values[4]
        year        =values[5]
        runtime     =values[6]
        rating      =values[7]
        votes       =values[8]
        revenue     =values[9]
        metascore   =values[10]
            

    empty_session.execute('INSERT INTO movies (rank,title,genre,description,director,actors,year,runtime,rating,votes,revenue,metascore) VALUES (:rank,:title,:genre,:description,:director,:actors,:year,:runtime,:rating,:votes,:revenue,:metascore)',
                          {'rank':rank,'title':title,'genre':genre,'description':description,'director':director,'actors':actors,'year':year,'runtime':runtime,'rating':rating,'votes':votes,'revenue':revenue,'metascore':metascore})
    row = empty_session.execute('SELECT id from movies where rank = :rank',
                                {'rank': rank}).fetchone()
    return row[0]



def test_loading_of_movie(empty_session):
    movie = empty_session.query(Movie)

    assert len(movie) > 0

