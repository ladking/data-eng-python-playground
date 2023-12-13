import psycopg2

def ConnectPostgres(db_params):
    params_key = ["host", 'port','user', 'password', 'database']
    for keys in db_params:
        params_key.remove(keys)
    if len(params_key) > 0:
        for x in params_key:
            print(x + " is required")
        raise ValueError("Missing Connection parameters")

    try:
        conn = psycopg2.connect(**db_params)
    except psycopg2.Error as err:
        print(f"Error: {err}")

    cursor = conn.cursor()
    conn.autocommit = True
    print(f"Connected to Database sucessfully")
    return cursor

