# caliber, 2021.

import sys, csv, re

codes = ["225K.00","8G94.00","8HHp.00","9N54.00","E200200","E200400","E200500","E202900","E202A00","E202D00","E202E00","Eu41100","Eu41112","Eu41y11","Eu41z11"];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('anxiety-disorders-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["anxiety-disorders---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in codes): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["anxiety-disorders---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["anxiety-disorders---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
