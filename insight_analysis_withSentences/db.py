import psycopg2


def get_db_connection():

    conn = psycopg2.connect(
        database="dna_practice", user='postgres', password='123', host='127.0.0.1', port='54320'
    )
    return conn


def create_attrition_table():
    conn = get_db_connection()
    schema = """
        CREATE TABLE IF NOT EXISTS attrition_insights (
            id SERIAL PRIMARY KEY,
            track TEXT,
            value TEXT
        );
    """
    with conn.cursor() as cur:
        cur.execute(schema)
        conn.commit()
    print("created")


def add_attrition_dictionary_to_table(data):
    conn = get_db_connection()
    with conn.cursor() as cur:
        for key, value in data.items():
            cur.execute("INSERT INTO attrition_insights (track, value) VALUES (%s, %s)", (key, value))
        conn.commit()
    print("added")


def get_attrition_insight():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'SELECT track, value FROM attrition_insights')
    response = cur.fetchall()
    cur.close()
    conn.close()
    return response
