from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, DateTime,
    ForeignKey
)
from sqlalchemy.orm import mapper, relationship

from covid.movie import model

metadata = MetaData()

movie = Table(
    'movies', metadata,
    Column('rank', Integer, primary_key=True, autoincrement=True),
    Column('title', String(1024), nullable=False),
    Column('genre', String(1024), nullable=False),
    Column('description', String(1024), nullable=False),
    Column('director', String(1024), nullable=False),
    Column('actors', String(1024), nullable=False),
    Column('year', String(8), nullable=False),
    Column('runtime', String(1024), nullable=False),
    Column('rating', String(8), nullable=False),
    Column('votes', String(16), nullable=False),
    Column('revenue', String(32), nullable=False),
    Column('metascore', String(16), nullable=False),
)



def map_model_to_tables():
    mapper(model.Movie, movie, properties={
        '__rank': movie.c.rank,
        '__title': movie.c.title,
        #'__genre': movie.c.genres,
        '__description': movie.c.description,
        '__director': movie.c.director,
        #'__actors': movie.c.actors,
        '__year': movie.c.year,
        '__runtime': movie.c.runtime,
        '__rating': movie.c.rating,
        '__votes': movie.c.votes,
        '__revenue': movie.c.revenue,
        '__metascore': movie.c.metascore,
    })
