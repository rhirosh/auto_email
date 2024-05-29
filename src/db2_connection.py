from dotenv import load_dotenv

load_dotenv()
import os

os.add_dll_directory(os.getenv("PATH_IBM_DB2"))
import ibm_db


def fetch_data_from_db2(query):
    database = os.getenv("DB2_DATABASE")
    hostname = os.getenv("DB2_HOSTNAME")
    port = os.getenv("DB2_PORT")
    protocol = os.getenv("DB2_PROTOCOL")
    username = os.getenv("DB2_UID")
    password = os.getenv("DB2_PASSWORD")
    schema = os.getenv("DB2_SCHEMA")

    connection_string = "DATABASE=" + database + ";HOSTNAME=" + hostname + ";PORT=" + port + ";PROTOCOL=" + protocol + ";UID=" + username + ";PWD=" + password + ";"+ "CURRENTSCHEMA="+ schema + ";"

    conn = ibm_db.connect(connection_string, "", "")
    stmt = ibm_db.exec_immediate(conn, query)
    result = []
    row = ibm_db.fetch_assoc(stmt)
    while row:
        result.append(row)
        row = ibm_db.fetch_assoc(stmt)
    ibm_db.close(conn)
    return result
