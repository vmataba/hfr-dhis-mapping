from config import Configuration
from org_unit import OrgUnit
from org_unit_group import OrgUnitGroup
from csv_reader import CsvReader
from org_unit_group_set import OrgUnitGroupSet
import csv
import json

class PayLoad:

    config = Configuration.config
    
    @classmethod
    def read_csv_data(self):
        
        with open(PayLoad.config['csv_file'], 'r') as csvFile:
            file_reader = csv.reader(csvFile)
            # Capturing set colums
            keys = file_reader.next()
            # Setting Key Values
            col_keys = {}
            index = 0
            for key in keys:
                if key in PayLoad.config['columns']:
                    col_keys.update({index: PayLoad.config['columns'][key]})
                index += 1
        return col_keys

    @classmethod
    def generate_payload(self):
        contents = '{' 
        contents += '"system":'
        contents += json.dumps(OrgUnit.config['system'])
        contents += ','
        contents += '"organisationUnits":'
        contents += OrgUnit.get_org_units()
        contents += ','
        contents += '"organisationUnitGroups":'
        contents += OrgUnitGroup.get_org_groups()
        contents += ','
        contents += '"organisationUnitGroupSets":'
        contents += OrgUnitGroupSet.get_org_group_sets()
        contents += '}'

        with open(Configuration.config['payload_file'],'w') as payLoad:
            payLoad.write(contents)

        #return contents

PayLoad.generate_payload()
#print OrgUnit.get_org_units()
#print CsvReader.get_org_group_keys()
#print CsvReader.get_org_group_keys()
#print CsvReader.read_org_group_data()
#print OrgUnitGroup.get_org_units('DSP')
#print 'Organisation Groups #: ',len(OrgUnitGroup.get_org_groups())
#print 'Orgnisation Units #: ', len(OrgUnit.get_org_units())
#print OrgUnitGroupSet.get_org_group_set_keys()
#print 'Group Sets Count: ',len(OrgUnitGroupSet.get_org_group_sets())


#print OrgUnitGroup.get_org_groups()
#print CsvReader.get_key_code(Configuration.config['org_groups'].itervalues().next())

#print Configuration.config['org_groups'].itervalues().next()