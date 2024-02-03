# Will load the cursors, other stuff



def get_database_schema():
    schema = """
    -- Genres table
    CREATE TABLE IF NOT EXISTS Genres (
        GenreID INTEGER PRIMARY KEY AUTOINCREMENT,
        GenreName VARCHAR(255) NOT NULL
    );

    -- Directors table
    CREATE TABLE IF NOT EXISTS Directors (
        DirectorID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName VARCHAR(255),
        LastName VARCHAR(255),
        Biography TEXT
    );

    -- Movies table
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
    );

    -- Actors table
    CREATE TABLE IF NOT EXISTS Actors (
        ActorID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName VARCHAR(255),
        LastName VARCHAR(255),
        Biography TEXT
    );

    -- MovieActors table
    CREATE TABLE IF NOT EXISTS MovieActors (
        MovieID INT,
        ActorID INT,
        Role VARCHAR(255),
        PRIMARY KEY (MovieID, ActorID),
        FOREIGN KEY (MovieID) REFERENCES Movies(MovieID),
        FOREIGN KEY (ActorID) REFERENCES Actors(ActorID)
    );

    -- Reviews table
    CREATE TABLE IF NOT EXISTS Reviews (
        ReviewID INTEGER PRIMARY KEY AUTOINCREMENT,
        MovieID INT,
        ReviewText TEXT,
        Rating DECIMAL(3, 1),
        ReviewDate DATE,
        FOREIGN KEY (MovieID) REFERENCES Movies(MovieID)
    );

    -- Users table
    CREATE TABLE IF NOT EXISTS Users (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserName VARCHAR(255) UNIQUE NOT NULL,
        Email VARCHAR(255) UNIQUE NOT NULL,
        Password VARCHAR(255) NOT NULL
    );

    -- UserReviews table
    CREATE TABLE IF NOT EXISTS UserReviews (
        ReviewID INT,
        UserID INT,
        PRIMARY KEY (ReviewID, UserID),
        FOREIGN KEY (ReviewID) REFERENCES Reviews(ReviewID),
        FOREIGN KEY (UserID) REFERENCES Users(UserID)
    );
    """
    return schema






def get_insert_statements():
    statements = """
    -- Insert statements for Genres table
    INSERT OR REPLACE INTO Genres (GenreName) VALUES
    ('Action'),
    ('Crime'),
    ('Drama');

    -- Insert statements for Directors table
    INSERT OR REPLACE INTO Directors (FirstName, LastName, Biography) VALUES
    ('Christopher', 'Nolan', 'Christopher Nolan is a British-American film director, producer, and screenwriter.'),
    ('Quentin', 'Tarantino', 'Quentin Tarantino is an American film director, producer, and screenwriter.'),
    ('Robert', 'Zemeckis', 'Robert Zemeckis is an American film director, producer, and screenwriter.');

    -- Insert statements for Actors table
    INSERT OR REPLACE INTO Actors (FirstName, LastName, Biography) VALUES
    ('Christian', 'Bale', 'Christian Bale is an English actor known for his versatility and intense method acting.'),
    ('John', 'Travolta', 'John Travolta is an American actor, singer, and dancer known for his roles in iconic films like "Saturday Night Fever" and "Grease".'),
    ('Tom', 'Hanks', 'Tom Hanks is an American actor and filmmaker known for his roles in films like "Forrest Gump", "Cast Away", and "Saving Private Ryan".'),
    ('Uma', 'Thurman', 'Uma Thurman is an American actress and model known for her collaborations with director Quentin Tarantino.');

    -- Insert statements for Movies table
    INSERT OR REPLACE INTO Movies (Title, ReleaseDate, GenreID, DirectorID, Description, Runtime, Rating) VALUES
    ('The Dark Knight', '2008-07-18', 1, 1, 'Action-packed superhero film directed by Christopher Nolan', 152, 9.0),
    ('Pulp Fiction', '1994-10-14', 2, 2, 'Cult classic crime film directed by Quentin Tarantino', 154, 8.9),
    ('Forrest Gump', '1994-07-06', 3, 3, 'Heartwarming drama directed by Robert Zemeckis', 142, 8.8);

    -- Insert statements for MovieActors table
    INSERT OR REPLACE INTO MovieActors (MovieID, ActorID, Role) VALUES
    (1, 1, 'Bruce Wayne / Batman'),
    (1, 4, 'Harvey Dent / Two-Face'),
    (2, 2, 'Vincent Vega'),
    (2, 1, 'Jules Winnfield'),
    (3, 3, 'Forrest Gump'),
    (3, 4, 'Jenny Curran');

    -- Insert statements for Reviews table
    INSERT OR REPLACE INTO Reviews (MovieID, ReviewText, Rating, ReviewDate) VALUES
    (1, 'A gripping and dark portrayal of Batman.', 8.5, '2023-01-15'),
    (2, 'A masterpiece in storytelling and filmmaking.', 9.0, '2023-01-20'),
    (3, 'An emotionally moving and unforgettable film.', 8.8, '2023-01-25');

    -- Insert statements for Users table
    INSERT OR REPLACE INTO Users (UserName, Email, Password) VALUES
    ('user1', 'user1@example.com', 'password1'),
    ('user2', 'user2@example.com', 'password2'),
    ('user3', 'user3@example.com', 'password3');

    -- Insert statements for UserReviews table
    INSERT OR REPLACE INTO UserReviews (ReviewID, UserID) VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (1, 2),
    (2, 3),
    (3, 1);
    """
    return statements