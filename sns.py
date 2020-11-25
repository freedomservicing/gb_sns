# This is *very* rough rn
import mysql.connector as connector
from mysql.connector import errorcode
from firebase import firebase
import json


'''Return a json loaded with necessary FB and mysql credentials'''
def retrieve_config(credentials_file_path):

    with open(credentials_file_path) as f:
        config  = json.load(f)

    return config


'''Return a mysqlDB connection '''
def get_mysqlDB_connection(config):

    dbCon = None

    try:
        dbCon = connector.connect(
        user = config.get("mysqlUser"),
        password = config.get("mysqlPass"),
        host = config.get("mysqlUser"),
        database = config.get("mysqlUser"))
    except connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Wrong user or password!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Bad Database!")
        else:
            print(err)

    return dbCon


'''Return an FB connection using provided json config'''
def get_fb_connection(config_file):
    return firebase.FirebaseApplication(config_file.get("databaseURL"), None)


'''Establish the pipe between GB server and automatically forward to FB'''
def main():

    # Remove .TEMPLATE from crednetials.json.TEMPLATE and populate as necessary
    CREDENTIALS_FILE_PATH = "credentials.json"

    config = retrieve_config(CREDENTIALS_FILE_PATH)

    fb = get_fb_connection(config)
    db = get_mysqlDB_connection(config)

    print("\nTesting Firebase Connection: \n", fb.get("Machines", None), "\n")


if __name__ == "__main__":
    main()
