import sqlite3
from sqlite3 import Error

# Inserts data into tables
def insert_into_genres(conn):

    sql = """

    INSERT OR REPLACE INTO Genres (GenreName) VALUES

    ('Action'),

    ('Crime'),

    ('Drama');

    """

    try:

        cursor = conn.cursor()

        cursor.execute(sql)

        conn.commit()


    except Error as e:

        print(f"The error '{e}' occurred")
 
# Function to insert data into the Directors table

def insert_into_directors(conn):

    sql = """

    INSERT OR REPLACE INTO Directors (FirstName, LastName, Biography) VALUES

    ('Christopher', 'Nolan', 'Christopher Nolan is a British-American film director, producer, and screenwriter.'),

    ('Quentin', 'Tarantino', 'Quentin Tarantino is an American film director, producer, and screenwriter.'),

    ('Robert', 'Zemeckis', 'Robert Zemeckis is an American film director, producer, and screenwriter.');

    """

    try:

        cursor = conn.cursor()

        cursor.execute(sql)

        conn.commit()


    except Error as e:

        print(f"The error '{e}' occurred")
 
# Function to insert data into the Actors table

def insert_into_actors(conn):

    sql = """

    INSERT OR REPLACE INTO Actors (FirstName, LastName, Biography) VALUES

    ('Christian', 'Bale', 'Christian Bale is an English actor known for his versatility and intense method acting.'),

    ('John', 'Travolta', 'John Travolta is an American actor, singer, and dancer known for his roles in iconic films like "Saturday Night Fever" and "Grease".'),

    ('Tom', 'Hanks', 'Tom Hanks is an American actor and filmmaker known for his roles in films like "Forrest Gump", "Cast Away", and "Saving Private Ryan".'),

    ('Uma', 'Thurman', 'Uma Thurman is an American actress and model known for her collaborations with director Quentin Tarantino.');

    """

    try:

        cursor = conn.cursor()

        cursor.execute(sql)

        conn.commit()

    except Error as e:

        print(f"The error '{e}' occurred")
 
# Function to insert data into the Movies table

def insert_into_movies(conn):

    sql = """

    INSERT OR REPLACE INTO Movies (Title, ReleaseDate, GenreID, DirectorID, Description, Runtime, Rating) VALUES

    ('The Dark Knight', '2008-07-18', 1, 1, 'Action-packed superhero film directed by Christopher Nolan', 152, 9.0),

    ('Pulp Fiction', '1994-10-14', 2, 2, 'Cult classic crime film directed by Quentin Tarantino', 154, 8.9),

    ('Forrest Gump', '1994-07-06', 3, 3, 'Heartwarming drama directed by Robert Zemeckis', 142, 8.8);

    """

    try:

        cursor = conn.cursor()

        cursor.execute(sql)

        conn.commit()


    except Error as e:

        print(f"The error '{e}' occurred")
 
# Function to insert data into the MovieActors table

def insert_into_movie_actors(conn):

    sql = """

    INSERT OR REPLACE INTO MovieActors (MovieID, ActorID, Role) VALUES

    (1, 1, 'Bruce Wayne / Batman'),

    (1, 4, 'Harvey Dent / Two-Face'),

    (2, 2, 'Vincent Vega'),

    (2, 1, 'Jules Winnfield'),

    (3, 3, 'Forrest Gump'),

    (3, 4, 'Jenny Curran');

    """

    try:

        cursor = conn.cursor()

        cursor.execute(sql)

        conn.commit()


    except Error as e:

        print(f"The error '{e}' occurred")



def insert_into_reviews(conn):

    sql = """

    INSERT OR REPLACE INTO Reviews (MovieID, ReviewText, Rating, ReviewDate) VALUES

    (1, 'A gripping and dark portrayal of Batman.', 8.5, '2023-01-15'),

    (2, 'A masterpiece in storytelling and filmmaking.', 9.0, '2023-01-20'),

    (3, 'An emotionally moving and unforgettable film.', 8.8, '2023-01-25');

    """

    try:

        cursor = conn.cursor()

        cursor.execute(sql)

        conn.commit()


    except Error as e:

        print(f"The error '{e}' occurred")
 
# Function to insert data into the Users table

def insert_into_users(conn):

    sql = """

    INSERT OR REPLACE INTO Users (UserName, Email, Password) VALUES

    ('user1', 'user1@example.com', 'password1'),

    ('user2', 'user2@example.com', 'password2'),

    ('user3', 'user3@example.com', 'password3');

    """

    try:

        cursor = conn.cursor()

        cursor.execute(sql)

        conn.commit()


    except Error as e:

        print(f"The error '{e}' occurred")
 
# Function to insert data into the UserReviews table

def insert_into_user_reviews(conn):

    sql = """

    INSERT OR REPLACE INTO UserReviews (ReviewID, UserID) VALUES

    (1, 1),

    (2, 2),

    (3, 3),

    (1, 2),

    (2, 3),

    (3, 1);

    """

    try:

        cursor = conn.cursor()

        cursor.execute(sql)

        conn.commit()

       

    except Error as e:

        print(f"The error '{e}' occurred")


def insert_all(conn):

    insert_into_genres(conn)
    insert_into_directors(conn)
    insert_into_movies(conn)
    insert_into_actors(conn)
    insert_into_movie_actors(conn)
    insert_into_reviews(conn)
    insert_into_users(conn)
    insert_into_user_reviews(conn)