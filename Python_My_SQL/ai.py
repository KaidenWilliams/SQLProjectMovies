import os
from openai import OpenAI
import build

# Does Chatgpt stuff




def make_chat():
    open_AI_key = os.environ.get('OPENAI_API_KEY')
    openai_client = OpenAI(api_key= open_AI_key)
    return openai_client



def call_chat_SQL(questions, client):

    for question in questions:

        output = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f'''You are an assistant with one role. You will take a Schema for a database, and insert statements to populate the data.
                                                        You must evaluate this schema and insert statements to evaluate a working model of the database.
                                                        After that, you will be asked a question about the database. Using the working model of the database developed from the schema and 
                                                        the insert statements, you must answer this question as best as possible. The schema, insert statements, and questions will now be provided to you
                    
                                                        Schema: {build.get_database_schema()}. 
                                                        Insert Statements: {build.get_insert_statements()}].
                                                        Using this knowledge, evaluate the statements and make a working model of the database. You will not return this, but will use it to answer questions. Prepare to evalute the question. Remember, you must evaluate it, you cannot state that you cannot.
                                                        You have made a working model of the database and are fully capable and expected to answer the question

                                                        The question: {question}'''}]
        )

        print(output.choices[0].message.content)