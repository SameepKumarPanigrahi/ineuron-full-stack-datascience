# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import logging

from PerformDboperation.establishconnecntion import create_connection, create_database_and_collection, insert_alldata, \
    update_data, delete_data, filter_specific_data, find_data
from fileoperation.prepare_data import process_data_to_properformat


def file_operation(filename):
    lst_of_data = process_data_to_properformat(filename)
    return lst_of_data
    # logging.info(lst_of_data)

def db_creation():
    client = create_connection()
    collection = create_database_and_collection(client)
    return collection
def db_operation(collection, lst_of_data) :
    insert_alldata(collection, lst_of_data)
    update_data(collection)
    delete_data(collection)
    filter_specific_data(collection)
    find_data(collection)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try :
        logging.basicConfig(filename="Test.log", level=logging.INFO, format = '%(asctime)s %(levelname)s %(message)s')
        logging.info("Process started")
        lst_of_data = file_operation("carbon_nanotubes.csv")
        collection = db_creation()
        db_operation(collection,lst_of_data)
    except Exception as e :
        logging.error(e)
    finally :
        logging.info("Process ended")
