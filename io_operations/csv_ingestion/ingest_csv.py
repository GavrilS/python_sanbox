import csv


# TEST_FILE = 'sample.csv'
TEST_FILE = 'io_operations/csv_ingestion/sample.csv'


def read_csv():
    with open(TEST_FILE) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {" : ".join(row)}')
            else:
                print(f'{row[0]} : {row[1]} : {row[2]} : {row[3]}')
            
            line_count += 1
        
        print(f'Number of processed lines: {line_count}')


def reading_csv_dict():
    with open(TEST_FILE, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {" : ".join(row)}')
            else:
                print(f'{row["type"]} : {row["group"]} : {row["category"]} : {row["code"]}')
            
            line_count += 1

        print(f'Number of processed lines: {line_count}')


if __name__=='__main__':
    read_csv()
    # reading_csv_dict()
