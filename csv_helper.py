'''
Utility file to process large CSV files
and quickly retrieve some metrics
'''
import csv

delimiter = '|'
file1 = ""
file2 = ""

'''
Return the headers + indexes and line count
of a file
'''
def process_header(file, delimiter):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        line_count = 0
        print("""HEADER:""")
        for row in csv_reader:
            if line_count == 0:
                [print(f"[ {x}, {i} ]") for (x,i) in enumerate(row)]
                line_count += 1
            else:
                line_count += 1

        print(f'[{file}]Line count: {line_count}')


'''
Return the # of unique keys in a file for a key_index
'''
def unique_keys(file, delimiter, key_index):
    keys_set = set()
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        for row in csv_reader:
            if row[5] not in keys_set:
                keys_set.add(row[key_index])
    
    print(f"[{file}] unique keys:", len(keys_set))

process_header(file1, delimiter)
process_header(file2, delimiter)
unique_keys(file1, delimiter, 5)
unique_keys(file2, delimiter, 5)
