class Configuration:

    config = {
        # Csv File Path
        'csv_file': '../tz_facility_registry.csv',
        # JSON File name
        'payload_file': '../payload.json',
        # System Details
        'system': {
            # System id
            'id': '9ae8d969-2597-41b5-a82d-ca819ff25fd0',
            # Rev
            'rev': '76df3be',
            # Version
            'version': '2.27'
        },
        # Specify columns from CSV as keys and their corresponding payload names as values
        'columns': {
            #'resmap-id': 'id',
            'Fac_IDNumber': 'code',
            'name': 'shortName',
            'Comm_FacName': 'name',
            # 'Fac_Type' : 'Fac-Type',
            # 'Fac_Type-1':'Fac-TYpe-Detailed',
            # 'Fac_Type-2':'Fac-Type-Detailed-Further',
            # 'Ownership':'Ownership',
            # 'Ownership-1': 'Ownership-Detailed',
            # 'Ownership-2' : 'Ownership-Detailed-Further',
            # 'Ownership-3' : 'Ownership-Detailed-Further-More',
            # 'OwnershipDetail':'Ownership-Detail'
        },
        #Columns to be used for retreving CSV Indexes
        'cols':{
            'resmap-id': 'id',
            'Fac_IDNumber': 'code',
            'name': 'name',
            'Fac_Type' : 'type',
            'Fac_Type-1':'facility-type-1',
            'Fac_Type-2':'Fac-Type-Detailed-Further',
            'Ownership':'Ownership',
            'Ownership-1': 'ownership-1',
            'Ownership-2' : 'Ownership-Detailed-Further',
            'Ownership-3' : 'Ownership-Detailed-Further-More',
            'OwnershipDetail':'Ownership-Detail'
        },
        #Column that has Organisation group formation Createria
        'org_groups': {
           'Fac_Type-1':'facility-type-1'
        },
        #Column that has Organisation Group Set formation creteria
        'org_group_sets': {
            'Ownership-1': 'ownership-1',
        }
    }