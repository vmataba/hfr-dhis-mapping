import csv
import json
from org_unit import OrgUnit
from config import Configuration
from csv_reader import CsvReader


class OrgUnitGroup (OrgUnit):

    'Has logic for formation of Organisation Unit Groups'

    def __init__(self,code,name,orgUnits = None):
        self.code = code
        self.name = name
        self.shortName = name

        org_units = []
        with open(CsvReader.config['csv_file'],'r') as csvFile:
            file_reader = csv.reader(csvFile)
            for row in file_reader:
                if self.name in row:
                    org_units.append({'code': row[CsvReader.get_key_code('code')]})
        self.organisationUnits = org_units

    config = Configuration.config

    @classmethod
    def get_org_groups_keys(self):
        keys = {}
        with open(CsvReader.config['csv_file'],'r') as csvFile:
            file_reader = csv.reader(csvFile)
            count  = 0
            for key in file_reader.next():
                if key in CsvReader.config['org_groups']:
                    keys.update({count:CsvReader.config['org_groups']})
                count += 1
        return keys


    def set_org_units(self):
        org_units = []
        with open(CsvReader.config['csv_file'],'r') as csvFile:
            file_reader = csv.reader(csvFile)
            for row in file_reader:
                if self.name in row:
                    org_units.append({'code','xxxx'})
        self.organisationUnits = org_units
    

    @classmethod
    def get_org_groups(self):
        with open(CsvReader.config['csv_file'], 'r') as csvFile:
            data = []
            data_vol = []
            file_reader = csv.reader(csvFile)
            file_reader.next()
            code_key = CsvReader.get_key_code('code')
            #name_key = CsvReader.get_key_code('name')
            identifier_key = CsvReader.get_key_code(Configuration.config['org_groups'].itervalues().next())
            for row in file_reader:
                    if row[identifier_key] not in data:
                        data.append(row[identifier_key])

                        orgGroup = OrgUnitGroup(row[code_key],row[identifier_key])
                    
                        data_vol.append(orgGroup.__dict__)
                                           
        return json.dumps(data_vol)
              


    