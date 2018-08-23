from config import Configuration
from csv_reader import CsvReader
import json
import csv

class OrgUnit(object):

    'Has logic for formation of Organisation Unit'

    #Acquire configuration settings
    config = Configuration.config
    # Organization Units
    organization_units = []
 
    def __init__(self, attributes):
        for attribute in attributes:
            setattr(self, attribute, attributes[attribute])
    
    @classmethod
    def get_org_units(self):
            with open(OrgUnit.config['csv_file'], 'r') as csvFile:
                file_reader = csv.reader(csvFile)
                file_reader.next()

                data = CsvReader.read_csv_data()
            
                attributes = {}

                for row in file_reader:

                    for index in data:

                        attributes.update({data[index]: row[index]})

                    org_unit = OrgUnit(attributes)

                    OrgUnit.organization_units.append(org_unit.__dict__)

            contents = ''
            contents += '['
            count = 1
            for org_unit in OrgUnit.organization_units:
                if count < len(OrgUnit.organization_units):
                    contents += json.dumps(org_unit)+','
                else:
                    contents += json.dumps(org_unit)
                count += 1

            contents += ']'
            return contents
    
    #Returns Organisation Group Instance for a group
    @classmethod
    def get_org_unit_for_group(self,group_name):
        return group_name

