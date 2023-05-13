from sqlalchemy import create_engine


def main():
    login = "root"
    password = "qwerty"
    host = "localhost"
    port = "3306"
    dbname = "company"

    engine = create_engine(f"mysql+pymysql://{login}:{password}@{host}:{port}/{dbname}")
    sql_statements = [
        """INSERT INTO archived_users (id, first_name, last_name, email)
	    (SELECT * FROM users);
	    """,
        "TRUNCATE company.users;"
    ]
    with engine.connect() as con:
        for sql in sql_statements:
            con.execute(sql)

if __name__ == "__main__":
    main()