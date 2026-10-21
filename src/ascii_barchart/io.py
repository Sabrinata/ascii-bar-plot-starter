import csv

def load_rows(csv_path):

    csv_list = []
    with open(csv_path, mode="r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        next(reader)
        
        for row in reader:
            row_tuple = tuple(row)
            csv_list.append(row_tuple)

    return csv_list

