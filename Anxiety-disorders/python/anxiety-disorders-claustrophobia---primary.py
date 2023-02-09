# caliber, 2021.

import sys, csv, re

codes = ["E202000","E202300","E202400","E202500","E202700","E202800","E202B00","E202C00","Eu40100","Eu40200","Eu40212","Eu40213","Eu40214","Eu40300","Eu40z11"];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('anxiety-disorders-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["anxiety-disorders-claustrophobia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in codes): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["anxiety-disorders-claustrophobia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["anxiety-disorders-claustrophobia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
