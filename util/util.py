import csv


def maze_csv_to_matrix(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        return [[int(num) for num in row] for row in reader]
