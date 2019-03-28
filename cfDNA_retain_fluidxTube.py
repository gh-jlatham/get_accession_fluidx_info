#!/usr/bin/env python3

# Get the Accession number from fluid-x tube ID

"""
INSTRUCTIONS:
# save this script to your desktop
# connect to scratch
# terminal:

source ~/miniconda3/bin/activate py3    # start virtual env
username=lspurka    # set variable to your username (NO SPACES!)
python ~/Desktop/cfDNA_retain_fluidxTube.py -u $username  # run script
python /Users/lspurka/Documents/Code/cfDNA_retain_request/cfDNA_retain_fluidxTube.py -u $username
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

def get_fluidxTube_info(username):

    csv = f"/Users/{username}/Desktop/fluidx_tube_input.csv"

    if not os.path.isfile(csv):
        sys.exit(f"\nERROR:\n{csv} does not exist!\n")

    parsed_wb_data_dir = "/Volumes/scratch/01 - DATA/Parsed-WB-Data"
    if not os.path.isdir(parsed_wb_data_dir):
        sys.exit("\nERROR:\nConnect to 'scratch' on smb://fserv.gha.local\n")

    agg_ex_df = pd.read_csv(f"{parsed_wb_data_dir}/Aggregated_EX.csv")

    df = pd.read_csv(csv)

    if "Tube_ID" not in df.columns:
        sys.exit(f"\nERROR:\ncolumn 'Tube_ID' missing in:\n{csv}\n"
                f"Update csv!\n")

    filtered_ex_df = agg_ex_df.loc[agg_ex_df.Tube_ID.isin\
            (df.Tube_ID)]\
            [["sample_name",
              "batch_id",
              "concs_ng/ul",
              "yields_ng",
              "Tube_Rack_ID",
              "Well_Name",
              "Tube_ID"]]

    suffix = str(datetime.now()).replace(" ", "_").replace(":", "-")\
            .split(".")[0]
    filtered_ex_df.to_csv(f"/Users/{username}/Desktop/fluidx_tube_output_"
            f"{suffix}.csv", index=False)

    print(f"\nDONE! Find:\nfluidx_tube_output_{suffix}.csv\non Desktop\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', dest='username', type=str,
                        help='your username')
    args = parser.parse_args()

    get_fluidxTube_info(args.username)

