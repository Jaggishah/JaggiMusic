from pymongo import MongoClient, errors

class MongoDBClient:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="music_database", timeout=5000):
        """
        Initializes the MongoDB client.
        :param uri: The MongoDB connection URI.
        :param db_name: The database name to use.
        :param timeout: Server selection timeout in milliseconds.
        """
        self.uri = uri
        self.db_name = db_name
        self.timeout = timeout
        self.client = None
        self.db = None

    def connect(self,logger):
        """
        Connect to the MongoDB server and select the database.
        """
        try:
            self.client = MongoClient(self.uri, serverSelectionTimeoutMS=self.timeout)
            self.client.admin.command("ping")
            self.db = self.client[self.db_name]
            logger.info(f"Connected to MongoDB database: {self.db_name}")
        except errors.ServerSelectionTimeoutError as e:
            logger.warn(f"Connection failed: {e}")
            self.client = None
            self.db = None
        except Exception as e:
            logger.warn(f"An unexpected error occurred: {e}")
            self.client = None
            self.db = None

    def get_collection(self, collection_name):
        """
        Access a specific collection in the database.
        :param collection_name: The name of the collection.
        :return: The collection object, or None if not connected.
        """
        if self.db is not None:
            return self.db[collection_name]
        else:
            print("Database connection not established.")
            return None
        
    def insert_data(self, collection_name, data, logger):
        """
        Inserts data into the specified collection.
        :param collection_name: The name of the collection.
        :param data: The data to insert (dictionary or list of dictionaries).
        :return: The ID(s) of the inserted document(s), or None if an error occurred.
        """
        collection = self.get_collection(collection_name)
        if collection is not None:
            try:
                if isinstance(data, list):
                    new_data = []
                    for document in data:
                        name = document.get('name')
                        if collection.count_documents({'name': name}) == 0: 
                            new_data.append(document)

                    if new_data: 
                        result = collection.insert_many(new_data)
                        logger.info(f"Inserted {len(result.inserted_ids)} documents.")
                        return result.inserted_ids
                    else:
                        logger.info("No new documents to insert (all are duplicates).")
                else:
                    name = document.get('name')
                    if collection.count_documents({'name': name}) == 0: 
                        result = collection.insert_one(data)
                        logger.info(f"Inserted document ID: {result.inserted_id}")
                        return result.inserted_id
                    else:
                       logger.info("No new document to insert (all are duplicates).")

            except Exception as e:
                logger.warn(f"An error occurred while inserting data: {e}")
                return None
        else:
            logger.warn(f"Failed to access collection: {collection_name}")
            return None

    def close(self, logger):
        """
        Closes the MongoDB connection.
        """
        if self.client:
            self.client.close()
            logger.info("MongoDB connection closed.")
        else:
            logger.info("No active connection to close.")
