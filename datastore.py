import random
import sqlite3

class Datastore():
    """
    A class that represents the database of the hangman game
    """

    def __init__(self):
        """
        Connects to the database
        """
        db_file = "hangman_datastore.db"
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

        
    def __del__(self):
        """
        Close the datastore connection
        """
        self.connection.close()


    def get_word(self) -> str:
        """
        returns a random word of 3 or more characters
        """
        
        # get word list
        self.cursor.execute(
            """
            SELECT word
            FROM words
            """
        )

        #get results
        results = self.cursor.fetchall()

        while True:
            word = random.choice(results)[0]
            if len(word) > 3:
                return word