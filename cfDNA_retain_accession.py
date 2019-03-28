#!/usr/bin/env python3

# Get the fluid-x tube ID from Accession number

"""
INSTRUCTIONS:
# save this script to your desktop
# connect to scratch
# terminal:

source ~/miniconda3/bin/activate py3    # start virtual env
username=lspurka    # set variable to your username (NO SPACES!)
python ~/Desktop/cfDNA_retain_accesion.py -u $username  # run script
python /Users/lspurka/Documents/Code/cfDNA_retain_request/cfDNA_retain_accesion.py -u $username
"""

# We need:
# Batch ID
# Sample well position
# Fluid-X plate ID
# Fluid-X tube ID
# from accession number as shown in the attached file.


import pandas as pd
import argparse
import os
import sys
from datetime import datetime

def get_cfDNA_retain_info(username):

    csv = f"/Users/{username}/Desktop/cfDNA_retain_request_input.csv"

    if not os.path.isfile(csv):
        sys.exit(f"\nERROR:\n{csv} does not exist!\n")

    parsed_wb_data_dir = "/Volumes/scratch/01 - DATA/Parsed-WB-Data"
    if not os.path.isdir(parsed_wb_data_dir):
        sys.exit("\nERROR:\nConnect to 'scratch' on smb://fserv.gha.local\n")

    agg_ex_df = pd.read_csv(f"{parsed_wb_data_dir}/Aggregated_EX.csv")

    df = pd.read_csv(csv)

    if "accession_number" not in df.columns:
        sys.exit(f"\nERROR:\ncolumn 'accession_number' missing in:\n{csv}\n"
                f"Update csv!\n")

    filtered_ex_df = agg_ex_df.loc[agg_ex_df.sample_name.isin\
            (df.accession_number)]\
            [["sample_name",
              "batch_id",
              "concs_ng/ul",
              "yields_ng",
              "Tube_Rack_ID",
              "Well_Name",
              "Tube_ID"]]

    suffix = str(datetime.now()).replace(" ", "_").replace(":", "-")\
            .split(".")[0]
    filtered_ex_df.to_csv(f"/Users/{username}/Desktop/"
            f"cfDNA_retain_request_output_{suffix}.csv", index=False)

    print(f"\nDONE! Find:\ncfDNA_retain_request_output_{suffix}.csv\non "
            f"Desktop\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', dest='username', type=str,
                        help='your username')
    args = parser.parse_args()

    get_cfDNA_retain_info(args.username)

