# TaxID Parsing

This is a simple script that will parse a file containg TaxIDs and left join species level or high names.

## Installation

Add installation instructions here. Ideally include commands to make  
the process as easy as possible for users.  

Clone repo and create environment:  
`git clone git@github.com:ukhsa-collaboration/taxid_parsing.git`  

`conda env create -n taxid_parsing `  

`conda activate taxid_parsing`  

Installation for users:  
`cd taxid_parsing`  
`pip install .`

Installation for developers (installs code in editable mode):  
`cd taxid_parsing`  
`pip install --editable '.[dev]'`

## Usage

```
taxid_parsing \
    -i # input tsv 
    -c # column number with taxid
    -o # output filename 
```

