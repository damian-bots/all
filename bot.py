from pymongo import MongoClient

# MongoDB connection URI
MONGO_URI = "mongodb+srv://fidixi3663:w7rvlxmDd5lsX9ix@cluster0.0k1an50.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Get all database names except system databases
databases = [db for db in client.list_database_names() if db not in ["admin", "config", "local"]]

for db_name in databases:
    db = client[db_name]
    collections = db.list_collection_names()
    
    for collection in collections:
        db[collection].drop()  # Delete all collections
        print(f"Dropped collection: {collection} from database: {db_name}")

    print(f"All collections dropped from database: {db_name}")

print("All user databases and collections have been deleted.")

# Close the connection
client.close()
