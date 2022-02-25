import csv
import logging
import os.path

def removNestings(l, output):
    """ This method will help to remove the nesting of lists"""
    if bool(l) :
        for i in l:
            if type(i) == list:
                removNestings(i, output)
            else:
                output.append(i)
        return output
    else:
        logging.error("List is empty")
        raise Exception("The list is empty")


def removesemicolon(l, output):
    """ THis method will process the data convert it from the string format to int format """
    if bool(l):
        for i in l:
            if ',' in i:
                s1 = ''
                s1 = s1.join(i.split(',')[1:])
                output.append(int(s1))
            else:
                output.append(int(i))
        return output
    else:
        logging.error("List is empty")
        raise Exception("The list is empty")

def process_data_to_properformat(filename) :
    """ This method will read the file and convert the data into a list of dictionaries"""
    try :
        logging.info("process_data_to_properformat method started")
        if os.path.exists(filename) :
            lst_dict = []
            with open(filename, 'r') as f:
                print("Reaching Here")
                reader = csv.reader(f, delimiter='\n')
                heading = next(reader)
                head = []
                for i in heading:
                    head.append(i.split(';'))
                head = removNestings(head, [])
                row_data = []
                for data in reader:
                    lst = lambda x: (i.split(';') for i in x)
                    x = lst(data)
                    x = removNestings(x, [])
                    x = removesemicolon(x, [])
                    row_data.append(x)
                row_lst = []
                for row in row_data:
                    dic = {}
                    for (key, value) in zip(head, row):
                        dic[key] = value
                    lst_dict.append(dic)
                f.close()
            return lst_dict
        else :
            logging.error("File not found in the directory")
            raise FileNotFoundError("File not found in the directory")
    except IOError :
        logging.error("File related error occured")
        raise IOError("Not able to open the File and the error is IOError")
    except Exception as e :
        raise Exception("Exception occured due to this ")