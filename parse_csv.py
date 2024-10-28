import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',')  # delimiter is the field seperator

        header = next(csv_reader)  # This code skips to the next line of the csv file and stores the header

        for line in csv_reader:
            csv_writer.writerow(line)  # writes the lines from the original file to the new file
