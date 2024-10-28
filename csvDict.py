# this code uses the DictReader and DictWriter methods
import csv


with open('MOCK_DATA.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('NEW_DATA.csv', 'w', newline='') as new_file:
        # field = ['order_id',
        #         'first_name',
        #         'last_name', 'email',
        #         'Shipping Address',
        #         'Shipping Country',
        #         'Shipping Time',
        #         'item',
        #         'Colour',
        #         'size']

        field = csv_reader.fieldnames  # this function allows to store the fieldnames from the original file

        csv_writer = csv.DictWriter(new_file, fieldnames=field, delimiter='\t')  # delimiter is the field seperator

        csv_writer.writeheader()  # writes the fieldnames as the first line of the file

        for line in csv_reader:
            del line['Shipping Time']   # deletes the row 'email' from the line
            csv_writer.writerow(line)   # writes the lines from the original file to the new file
            print(line)
