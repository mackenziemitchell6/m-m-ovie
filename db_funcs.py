import mysql.connector


def get_db_conn(config_params):
    """get_db_conn(config_params):
    Open a MySQL DB connection using
    config parameters
    Params:
        config module: config_params
    Returns:
        MySQL DB connection or None if exception
    """
    try:
        conn = mysql.connector.connect(
            host=config_params.host,
            user=config_params.user,
            passwd=config_params.password,
            database=config_params.db)

    except mysql.connector.Error as err:
        print('Connection error:  ', err.errno)
        return None

    return conn


def insert_movie_values(cursor, title_id, title, director, studio, meta_score,
                        budget, bo_gu, bo_ww, bo_ow):
    """
    insert_movie_values(movie_id, title, director, studio, meta_score, budget,
                        bo_gu, bo_ww, bo_ow, config_params):

    Insert values into movie table
    Params:
    Returns:
    """
    QUERY = """Insert into movies (title_id, title, director, studio,
                                        meta_score, budget, bo_gu,
                                        bo_ww, bo_ow)
                                        values (%s, %s, %s, %s, %s, %s,
                                                %s, %s, %s)"""

    values = (title_id, title, director, studio, meta_score,
              budget, bo_gu, bo_ww, bo_ow)

    cursor.execute(QUERY, values)


def insert_actor_values(cursor, actor_id, first_name, last_name, pop_rank,
                        social_rank, salary):
    """
    insert_actor_values(cursor, actor_id, first_name, last_name, pop_rank,
                        social_rank, salary):
    Insert values into the actor table
    Params:
    Returns:
    """
    QUERY = """insert into actors (actor_id, first_name, last_name, pop_rank,
                                   social_rank, salary)
                                   values (%s, %s, %s, %s, %s, %s)"""

    values = (actor_id, first_name, last_name, pop_rank,
              social_rank, salary)

    cursor.execute(QUERY, values)
