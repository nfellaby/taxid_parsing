#!/usr/bin/env python3

"""
Example main script that pulls in functions from module(s) and runs the code. Suggested layout
and example helper functions provided below. These can be amended as required.
"""

# Imports - ordered (can use ruff to do this automatically)
import argparse
import logging
import sys

import pandas  # type: ignore

# from taxaplease import TaxaPlease


# Arg parse setup
def get_args():
    """Get command line arguments. Arguments can be added or removed as
    required. It is however recommended to keep the arguments below as
    a minimum for development purposes."""
    parser = argparse.ArgumentParser(
        prog="mscape script",
        description="""Script to left join TaxID with species name onto a table.
        """,
    )
    parser.add_argument("--input", "-i", type=str, required=True, help="File Name")
    parser.add_argument("--column", "-c", type=int, required=True, help="Column number for TaxaID")
    parser.add_argument("--output", "-o", type=str, required=True, help="Output file name")

    return parser.parse_args()


# Logger set up
def set_up_logger(stdout_file):
    """Example logger set up which can be amended as required. In this example,
    all logging messages go to a stdout log file, and error messages also go to
    stderr log. If the component runs correctly, stderr is empty. The logger is
    set to append mode so logs from older runs are not overwritten.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")

    out_handler = logging.FileHandler(stdout_file, mode="a")
    out_handler.setFormatter(formatter)
    logger.addHandler(out_handler)

    return logger


# Get TaxIDs
def get_taxid(df: pandas.DataFrame, column: int) -> list:
    """Extract unique taxid from pandas dataframe, ensure column only contains integers.
    Return unique integers as list
    """
    print(df)


# Main function
def main():
    "Main function description here"

    # Retrieve command line arguments:
    args = get_args()  # noqa: F841

    # Set up log file:
    log_file = "./taxid_parsing_logfile.txt"
    set_up_logger(log_file)

    # Add in rest of code including logging messages:
    logging.info(
        "TaxID Parsing code beginning"
    )  # Example only - add more informative logging messages

    # Read in table (csv/tsv)
    df = pandas.read_csv(args.input, sep=None)

    # Get TaxID
    get_taxid(df, args.column)

    # Get species name or higher for taxids
    # Left join Name onto original table

    # Write to logs if component finished successfully (or not):
    logging.info("TaxID Parsing code successfully completed")

    return


# Run
if __name__ == "__main__":
    sys.exit(main())
