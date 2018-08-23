import csv
from config import Configuration


class CsvReader:
    'For Reading various CSV Data'

    config = Configuration.config

    @classmethod
    def read_csv_data(self,cols = 'columns'):
        with open(CsvReader.config['csv_file'], 'r') as csvFile:
            file_reader = csv.reader(csvFile)
            # Capturing set colums
            keys = file_reader.next()
            # Setting Key Values
            col_keys = {}
            index = 0
            for key in keys:
                if key in CsvReader.config[cols]:
                    col_keys.update({index: CsvReader.config[cols][key]})
                index += 1
        return col_keys

    @classmethod
    def get_org_group_keys(self):
        keys = {}
        with open(CsvReader.config['csv_file'], 'r') as csvFile:
            file_reader = csv.reader(csvFile)
            count = 0
            for key in file_reader.next():
                if key in CsvReader.config['org_groups']:
                    keys.update({count: CsvReader.config['org_groups'][key]})
                count += 1
        return keys
    
    @classmethod
    def get_key_code(self,key_name):
        keys = CsvReader.read_csv_data('cols')
        for key in keys:
            if key_name == keys[key]:
                result = key
                break
        return result