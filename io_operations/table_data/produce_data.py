import openpyxl

PATH = '/tmp/data.xlsx'

def build_data(data=None):
    if not data:
        data = [
            ['country', 'capital', 'population'],
            ['Denmark', 'Copenhagen', '5,989,000'],
            ['United States', 'Washington, D.C.', '331,449,281'],
            ['Japan', 'Tokyo', '123,953,000'],
            ['Brazil', 'Brasília', '205,223,000'],
            ['Taiwan', 'Taipei', '23,356,000']
        ]

    return data


def create_file(data, path=PATH):
    # Create an excel workbook
    workbook = openpyxl.Workbook()
    # Select the default sheet (usually named 'Sheet')
    sheet = workbook.active
    # Add data to the sheet
    for row in data:
        sheet.append(row)
    
    # Save the workbook to a file
    workbook.save(path)

    print('File successfully saved!')


if __name__=='__main__':
    data = build_data()

    create_file(data)
