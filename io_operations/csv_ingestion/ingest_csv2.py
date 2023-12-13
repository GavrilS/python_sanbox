import pandas

# TEST_FILE = 'sample.csv'
TEST_FILE = 'io_operations/csv_ingestion/sample.csv'

def main():
    df = pandas.read_csv(TEST_FILE)
    print('df: ', df)


if __name__=='__main__':
    main()
