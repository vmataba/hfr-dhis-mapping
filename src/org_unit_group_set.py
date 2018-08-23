from org_unit import OrgUnit
from org_unit_group import OrgUnitGroup
from config import Configuration
from csv_reader import CsvReader
import csv
import json

class OrgUnitGroupSet:
    
    'Has logic for formation of Organisation Unit Group Sets'

    def __init__(self,code,name,organisationUnitGroups = None):
        self.code = code
        self.name = name

        with open(Configuration.config['csv_file'],'r') as csvFile:

            data = []
            data_vol = []
            file_reader = csv.reader(csvFile)
            file_reader.next()
            code_key = CsvReader.get_key_code('code')
            #name_key = CsvReader.get_key_code('name')
            group_identifier_key = CsvReader.get_key_code(Configuration.config['org_groups'].itervalues().next())
            group_set_identifier_key = CsvReader.get_key_code(Configuration.config['org_group_sets'].itervalues().next())
            for row in file_reader:
                if row[group_identifier_key] not in data:
                    if row[group_set_identifier_key] not in data:
                        data.append(row[group_identifier_key])

                        data_vol.append({'code':row[code_key]})

        self.organisationUnitGroups = data_vol


    config = Configuration.config
           
    @classmethod
    def get_org_group_set_keys(self):
        keys = {}
        with open(CsvReader.config['csv_file'],'r') as csvFile:
            file_reader = csv.reader(csvFile)
            count  = 0
            for key in file_reader.next():
                if key in CsvReader.config['org_group_sets']:
                    keys.update({count:CsvReader.config['org_group_sets']})
                count += 1
        return keys

    @classmethod
    def get_org_unit_groups(self,key,group_set_name):
        with open(OrgUnitGroupSet.config['csv_file']) as csvFile:
            file_reader = csv.reader(csvFile)
            file_reader.next()
            #keys = CsvReader.read_csv_data()
            org_unit_groups = []
            for row in file_reader:
                if group_set_name in row:
                    org_unit_groups.append({key: 'XXXXX'})
                    
        return org_unit_groups

    @classmethod
    def get_org_group_sets(self):
        with open(CsvReader.config['csv_file'], 'r') as csvFile:
            data = []
            data_vol = []
            file_reader = csv.reader(csvFile)
            file_reader.next()
            code_key = CsvReader.get_key_code('code')
            #name_key = CsvReader.get_key_code('name')
            identifier_key = CsvReader.get_key_code(Configuration.config['org_group_sets'].itervalues().next())
            for row in file_reader:
                    if row[identifier_key] not in data:
                        data.append(row[identifier_key])

                        orgGroupSet = OrgUnitGroupSet(row[code_key],row[identifier_key])
                    
                        data_vol.append(orgGroupSet.__dict__)
                                           
        return json.dumps(data_vol)




    