import json
import csv

def read_file(file_name: str) -> str:
    with open(file_name, 'r') as file:
        contents = file.read()

        return contents

def read_each_file_line(file_name: str) -> str:
    with open(file_name, 'r') as file:
        for line in file:
            print(line.strip())  

def read_parsed_each_file_line(file_name: str) -> list:
    with open(file_name, 'r') as file:
        contents = file.readlines()

    parsed_data = []

    for line in contents:
        fields = line.strip().split(',')
        parsed_data.append(fields)

    return parsed_data

def read_json_file(file_name: str):
    with open(file_name, 'r') as file:
        parsed_data = json.load(file)

        return parsed_data
    
def read_csv_file(file_name: str) -> list:
    parsed_data = []

    with open(file_name, 'r', newline = '') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            parsed_data.append(row)

    return parsed_data

def read_text_file_stream(file_name: str) -> list:
    parsed_file = []

    with open(file_name, 'r') as file:
        for line in file:
            parsed_file.append(line.strip())

    return parsed_file

def append_to_file(file_name: str, data) -> None:
    with open(file_name, 'a') as file:
        file.write(data)