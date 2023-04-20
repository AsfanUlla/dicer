from piccolo.engine.postgres import PostgresEngine


DB = PostgresEngine(config={
    'host': 'localhost',
    'database': 'scrap_db',
    'user': 'postgres',
    'password': ''
})
