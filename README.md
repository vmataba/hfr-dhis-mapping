# HFR - DHIS DATA MAPPING PROGRAM
1 --> Under src/config.py you will have to specify various settings for the program to work
  --> Settings like, csv file (as data source), path to which payload (.json) file will be output
  --> Which columns from csv will be considered and their reanming standards in a payload file
  --> What csv column determines Organisation Unit Groups/Sets separation
2 --> Run src/gen_payload.py to generate payload file (This will later be imported to DHIS2),when
  --> importing set code as Identifier
