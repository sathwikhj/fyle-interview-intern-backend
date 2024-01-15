from sqlalchemy import create_engine, MetaData

# Replace 'your_database_url' with the actual URL of your database
database_url = 'sqlite:///./store.sqlite3'

engine = create_engine(database_url)
metadata = MetaData(bind=engine)

# Reflect all the tables from the database
metadata.reflect()

# Print the table names
print("Tables in the database:")
for table_name in metadata.tables.keys():
    print(table_name)
