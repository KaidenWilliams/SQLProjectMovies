# main, where eveything is executed

import os
import sqlite3
from sqlite3 import Error
from openai import OpenAI
import build


# TODO
# 1. Create Connection
# 2. Create Tables: Keys, columns, data, other stuff
# 3. Take user input
# 4. Make ChatGPT respond to that, find answer in table





# 1. Establish table Connection def

def create_connection(file_path):
    conn = sqlite3.connect(file_path)
    return conn



# Function to create tables
def create_tables(conn):

    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Genres (
            GenreID INTEGER PRIMARY KEY AUTOINCREMENT,
            GenreName VARCHAR(255) NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Directors (
            DirectorID INTEGER PRIMARY KEY AUTOINCREMENT,
            FirstName VARCHAR(255),
            LastName VARCHAR(255),
            Biography TEXT
        )
        """)
 
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Movies (
            MovieID INTEGER PRIMARY KEY AUTOINCREMENT,
            Title VARCHAR(255) NOT NULL,
            ReleaseDate DATE,
            GenreID INT,
            DirectorID INT,
            Description TEXT,
            Runtime INT,
            Rating DECIMAL(3, 1),
            FOREIGN KEY (GenreID) REFERENCES Genres(GenreID),
            FOREIGN KEY (DirectorID) REFERENCES Directors(DirectorID)
        )
        """)
 
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Actors (
            ActorID INTEGER PRIMARY KEY AUTOINCREMENT,
            FirstName VARCHAR(255),
            LastName VARCHAR(255),
            Biography TEXT
        )
        """)
 
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS MovieActors (
            MovieID INT,
            ActorID INT,
            Role VARCHAR(255),
            PRIMARY KEY (MovieID, ActorID),
            FOREIGN KEY (MovieID) REFERENCES Movies(MovieID),
            FOREIGN KEY (ActorID) REFERENCES Actors(ActorID)
        )
        """)
 
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Reviews (
            ReviewID INTEGER PRIMARY KEY AUTOINCREMENT,
            MovieID INT,
            ReviewText TEXT,
            Rating DECIMAL(3, 1),
            ReviewDate DATE,
            FOREIGN KEY (MovieID) REFERENCES Movies(MovieID)
        )
        """)
 
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            UserID INTEGER PRIMARY KEY AUTOINCREMENT,
            UserName VARCHAR(255) UNIQUE NOT NULL,
            Email VARCHAR(255) UNIQUE NOT NULL,
            Password VARCHAR(255) NOT NULL
        )
        """)
 
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS UserReviews (
            ReviewID INT,
            UserID INT,
            PRIMARY KEY (ReviewID, UserID),
            FOREIGN KEY (ReviewID) REFERENCES Reviews(ReviewID),
            FOREIGN KEY (UserID) REFERENCES Users(UserID)
        )
        """)
 
        print("Tables created successfully")
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

        print("Data inserted into Genres table successfully")

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

        print("Data inserted into Directors table successfully")

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

        print("Data inserted into Actors table successfully")

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

        print("Data inserted into Movies table successfully")

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

        print("Data inserted into MovieActors table successfully")

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

        print("Data inserted into Reviews table successfully")

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

        print("Data inserted into Users table successfully")

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

        print("Data inserted into UserReviews table successfully")

    except Error as e:

        print(f"The error '{e}' occurred")




questions = [
    "What are the FirstNames of the people in the Directors table",  
    "What user wrote the most unfavorable review?",
]

def make_chat():
    open_AI_key = os.environ.get('openai')
    openai_client = OpenAI(api_key= "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")
    return openai_client



def call_chat(question, client):

    output = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f'''This is what the database looks like: {build.get_database_schema}. 
                                                    The data in the table is {build.get_insert_statements}].
                                                    The question is as follows: {question}
                                                    First, generate an sql query to answer these questions. Run the SQL query, and save the results. Translate the results into easily readible english and tell them to us here'''}]
    )

    return output.choices[0].message.content




questions = [
    "What are the FirstNames of the people in the Directors table",  
    "What user wrote the most unfavorable review?",
]

# 1. Establish Connection Implemented
# 2. Make Tables
# 3. Insert Info into tables


def main():
    os.makedirs("our_db", exist_ok=True)
    db_path = os.path.join("our_db", "OURsqlite.db")
    conn = create_connection(db_path)
    # create_tables(conn)
    # insert_all(conn)
    client = make_chat()
    answer = call_chat(questions[1], client)
    print(answer)




if __name__ == "__main__":
    main()

#     parser = argparse.ArgumentParser()
#     parser.add_argument("--query", type=str, default="natural language query")
#     args = parser.parse_args()

#     main()
#     main(conn, question=args.query)