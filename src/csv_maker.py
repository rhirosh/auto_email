from io import StringIO
import csv


def csv_maker(data):
    if data:
        csv_buffer = StringIO()
        csv_writer = csv.DictWriter(csv_buffer, fieldnames=data[0].keys(), delimiter=';')
        csv_writer.writeheader()
        csv_writer.writerows(data)
        csv_buffer.seek(0)
        return csv_buffer
