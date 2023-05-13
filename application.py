from sqlalchemy import create_engine

def main():
    login = "root"
    password = "qwerty"
    host = "localhost"
    port = "3306"
    dbname = "company"

    engine = create_engine(f"mysql+pymysql://{login}:{password}@{host}:{port}/{dbname}")
    print(engine.table_names())
    sql = "SELECT * FROM company.archived_users;"

    with engine.connect() as connection:
        result = connection.execute(sql)
        for row in result:
            print(row)
if __name__ == "__main__":
    main()
