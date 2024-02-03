import sqlite3
from sqlite3 import Error


# Creates Tables
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
 
    except Error as e:
        print(f"The error '{e}' occurred")
 