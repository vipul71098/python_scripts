
def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://127.0.0.1:27017"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    client.testdb.command(
        'dropUser', 'newTestUser',
    )

    return

# This is added so that many files can reuse the function get_database()
if _name_ == "__main__":

    # Get the database
    dbname = get_database()