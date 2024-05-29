# src/execution.py
from src.db2_connection import fetch_data_from_db2
from src.csv_writer import csv_writer
from src.email_sender import send_email
from query_db2 import get_query_db2
import os
from datetime import date, timedelta
from dotenv import load_dotenv

load_dotenv()


def execution():

    start_date = str(date.today() - timedelta(days=2))
    end_date = str(date.today())
    query_string = get_query_db2(start_date, end_date)
    data = fetch_data_from_db2(query_string)
    csv_filename = "Control_Desk_" + start_date + "_até_" + end_date + ".csv"

    csv_path = csv_writer(data, csv_filename)

    send_email(
        subject=csv_filename,
        email_to=[os.getenv('EMAIL_TO'),os.getenv('EMAIL_TO_2')],
        email_from=os.getenv('EMAIL_FROM'),
        csv_path=csv_path,
        filename=csv_filename,
        #cc_emails=[],
        body="Este é um email automático, contendo a consulta do Control Desk da data " + start_date + " até "+ end_date+ ".\nAgendado para ser executado segunda-feira as 9 horas da manhã"
    )
