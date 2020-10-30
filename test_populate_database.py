from sqlalchemy import select, inspect

from covid.adapters.orm import metadata

def test_database_populate_select_all_movies(database_engine):

    # Get table information
    inspector = inspect(database_engine)
    ranks = inspector.get_table_names()[0]

    with database_engine.connect() as connection:
        # query for records in table users
        select_statement = select([metadata.tables[ranks]])
        result = connection.execute(select_statement)

        assert len(result)>0
