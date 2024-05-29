import os
import csv

def csv_writer(data, csv_filename):
    if data:

        output_directory = "data/output"
        output_path = os.path.join(os.getcwd(), output_directory)
        os.makedirs(output_path, exist_ok=True)
        csv_filepath = os.path.join(output_path, csv_filename)

        headers = data[0].keys()
        with open(csv_filepath, 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter=';')
            writer.writeheader()
            writer.writerows(data)
    return csv_filepath