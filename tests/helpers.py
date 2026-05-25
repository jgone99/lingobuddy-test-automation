from psycopg2.extensions import cursor as _cursor

def get_translation(db: _cursor, word: str):
    db.execute("SELECT spanish FROM word_pairs WHERE english = %s", (word,))
    return str(db.fetchone()[0])