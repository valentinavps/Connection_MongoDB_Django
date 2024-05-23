from pymongo import MongoClient
def get_db_handle(db_name="Time", host="mongodb://localhost", port=27017): #, username, password):

    client = MongoClient(host=host,
                      port=int(port)
                      #username=username,
                      #password=password
                     )
    db_handle = client[db_name]
    return db_handle #, client