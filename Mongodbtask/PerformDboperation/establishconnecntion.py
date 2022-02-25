import logging
import pymongo
#import dnspython
def create_connection() :
    try :
        client = pymongo.MongoClient(
            "mongodb+srv://sameep:mongodb@cluster0.k4ufu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
            tls=True,
            tlsAllowInvalidCertificates=True)
        return client
    except Exception as e :
        logging.error("Exception occured during the database connection")

def create_database_and_collection(client) :
    try :
        db = client["Ineuron"]
        colection = db["carbon_nanotubes"]
        return colection
    except Exception as e :
        logging.error("Exception occured during the database creation")

def insert_alldata(client, lst_of_data) :
    try :
        client.insert_many(lst_of_data)
    except Exception as e :
        logging.error("Exception occured during the insertion operation")
        raise Exception("Exception occured during the insertion operation")

def update_data(client) :
    try :
        client.update_many({'Chiral indice m' : 1},{"$set":{'Chiral indice m' : 100}})
    except Exception as e :
        logging.error("Exception occured during the updation operation")
        raise Exception("Exception occured during the updation operation")

def delete_data(client) :
    try :
        client.delete_many({'Chiral indice m' : {"$gte" : 100}})
    except Exception as e :
        logging.error("Exception occured during the deletion operation")
        raise Exception("Exception occured during the deletion operation")

def filter_specific_data(client) :
    try :
        result = client.find({'Initial atomic coordinate w': 111865})
        for i in result:
            logging.info(i)
    except Exception as e :
        logging.error("Exception occured during the filter operation")
        raise Exception("Exception occured during the filter operation")

def find_data(client) :
    try :
        for i in client.find().limit(2):
            logging.info(i)
    except Exception as e :
        logging.error("Exception occured during the find operation")
        raise Exception("Exception occured during the find operation")