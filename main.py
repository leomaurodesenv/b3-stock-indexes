'''Main'''
import os
import pandas as pd
from pandas.core.frame import DataFrame
from indexes import INDEXES

# settings
REMOVE_DUPLICATES = True
KEEP_COLUMNS = ['Code', 'Stock', 'Type', 'Theoretical Quantity']

def preprocess_file(folder, filename, destination):
    '''Fix the CSV file'''
    filepath = f'{folder}/{filename}'
    mockpath = f'{destination}/{filename}'
    with open(filepath, 'r') as file:
        lines = file.readlines()
        # remove first line
        lines = lines[1:]
        # remove two last lines
        lines = lines[:-2]
    # remove last comma
    lines = [line.rstrip(',\n') for line in lines]
    # remove unnecessary spaces
    lines = [' '.join(line.split()) for line in lines]
    # add breaklines
    lines = [line+'\n' for line in lines]

    # creating staging area
    if not os.path.exists(destination): os.makedirs(destination)
    with open(mockpath, 'w') as file:
        for line in lines: file.write(line)
    return mockpath


# create temporary folder
if not os.path.exists('source/mock'):
    os.makedirs('source/mock')


# empty DataFrame
df = DataFrame()

# run main
for name, folder, idict in INDEXES:
    print(f'{name} - folder: {folder}')
    # process indexes types
    for type_code, type_name in idict.items():
        source = f'source/{folder}'
        destination = f'source/mock/{folder}'
        filenames = [fname for fname in os.listdir(source) if fname.startswith(f"{type_code}")]
        print(type_code, filenames)
        # preprocess the b3 file
        filepath = preprocess_file(source, filenames[0], destination)
        # read the b3 file
        mdf = pd.read_csv(filepath, sep=',')
        mdf = mdf[KEEP_COLUMNS]
        mdf['Segment Area'] = name
        mdf['Segment Code'] = type_code
        mdf['Segment Name'] = type_name
        df = df.append(mdf).reset_index(drop=True)

# removing duplicates
print(f'\nNumber of stocks: {df.shape[0]}')
if REMOVE_DUPLICATES:
    df = df.drop_duplicates(subset=['Code', 'Stock'], keep='first')
    print(f'Number of stocks: {df.shape[0]}')
# saving the stock indexes
df.to_csv(f'output/stock-indexes.csv', sep=',', index=False)
