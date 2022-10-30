# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS
    songplays (
        songplay_id SERIAL PRIMARY KEY, 
        start_time VARCHAR, 
        user_id INTEGER, 
        level VARCHAR, 
        song_id VARCHAR, 
        artist_id VARCHAR, 
        session_id , 
        location TEXT, 
        user_agent TEXT);
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS
    users (user_id SERIAL PRIMARY KEY, first_name VARCHAR, last_name VARCHAR, gender VARCHAR, level VARCHAR);
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS
    songs (song_id VARCHAR PRIMARY KEY, title VARCHAR, artist_id VARCHAR, year INTEGER, duration FLOAT8);
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS
    artists (artist_id VARCHAR PRIMARY KEY, name VARCHAR, location VARCHAR, latitude FLOAT8, longitude FLOAT8);
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS
    time (start_time VARCHAR, hour INTEGER, day INTEGER, week INTEGER, month, year, weekday);
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]