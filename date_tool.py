# For timestamps like "2021-06-25T15:18:54.050443+00:00"
# Anything like yyyy-mm-ddThh:mm:ss should work
# USAGE: "python3 date_tool.py infile.csv outfile.csv"

import csv
import sys
from datetime import datetime
from pathlib import Path

if not len(sys.argv) == 3:
    print("USAGE: python3 date_tool.py infile.csv outfile.csv")

path_csv_in = Path(sys.argv[1])
path_csv_out = Path(sys.argv[2])

validate1 = path_csv_in.is_file() and path_csv_in.suffix.lower() == '.csv'
validate2 = path_csv_out.is_file() == False

if not validate2:
    print("Output file already exists, aborting")
    exit(1)

if validate1 and validate2:
    with open(path_csv_in,'r',encoding='utf-8-sig') as csv_in:
        csv_reader = csv.DictReader(csv_in)
        with open(path_csv_out,'w') as csv_out:
            writer = csv.DictWriter(csv_out, fieldnames=csv_reader.fieldnames)
            writer.writeheader()
            for row in csv_reader:
                #parse the timestamp
                olddate, oldtime = row['Date'].split('T')
                oldtime = oldtime[:8]
                #translate it into the proper format
                new_ts = f"{datetime.strptime(olddate,'%Y-%m-%d').strftime('%m-%d-%Y')} {oldtime}"
                row['Date'] = new_ts
                writer.writerow(row)
else:
    print("Input file must be .csv")
