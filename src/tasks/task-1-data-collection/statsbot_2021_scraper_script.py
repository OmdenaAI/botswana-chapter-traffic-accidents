# We are going to use the tabula library

import tabula
from tabula.io import read_pdf
from tabulate import tabulate
import json
import pandas as pd
import os

#url = "https://www.statsbots.org.bw/sites/default/files/publications/Transport%20%26%20Infrastructure%20Statistics%20Report%202021.pdf"

# We are going to extract from the above pdf

# Read pdf into list of DataFrame
pdf = tabula.io.read_pdf("C://Users//Administrator//Documents//Transport_Infrastructure_Statistics_Report_2021.pdf", pages='all')

# save them in a folder
folder_name = "tables"
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)
# iterate over extracted tables and export as csv individually
for i, table in enumerate(pdf, start=1):
    table.to_excel(os.path.join(folder_name, f"table_{i}.xlsx"), index=False)

# Convert the output to one csv
# We will use the glob library to get all the files in the folder
import glob
# Set the path
path = r'C://Users//Administrator//Botswana-chapter-traffic-accidents//tables'

# Use glob to match the pattern ‘csv’
# and save the list of file names in the ‘all_filenames’ variable.
all_filenames = [i for i in glob.glob(path + "/*.xlsx")]
# Loop over the list of file names
# and read them into pandas
li = []
for filename in all_filenames:
    df = pd.read_excel(filename, index_col=None, header=0)
    li.append(df)

# Concatenate all data into one DataFrame
frame = pd.concat(li, axis=0, ignore_index=True)
# Save the DataFrame to csv
frame.to_csv('C://Users//Administrator//Documents//tables//combined_csv.csv', index=False, encoding='utf-8-sig')