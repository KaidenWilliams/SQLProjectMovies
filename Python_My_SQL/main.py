# main, where eveything is executed

import os
import sqlite3
from openai import OpenAI
import build
import create
import insert
import ai



def create_connection(file_path):
    conn = sqlite3.connect(file_path)
    return conn


questions = [
    "What are the FirstNames of the people in the Directors table",  
    "What user wrote the most unfavorable review?",
    "What Genres are in the table?",
    "What is the purpose of life",
    "What is the description of all the actors?",
    "What actors are in Movie_Actors"
]




def main():
    os.makedirs("our_db", exist_ok=True)
    db_path = os.path.join("our_db", "OURsqlite.db")
    conn = create_connection(db_path)
    create.create_tables(conn)
    insert.insert_all(conn)
    client = ai.make_chat()
    ai.call_chat_SQL(questions, client)



if __name__ == "__main__":
    main()