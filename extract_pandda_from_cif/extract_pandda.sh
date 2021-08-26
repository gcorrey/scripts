#!/bin/bash

## usage ##
## ./extract_pandda.sh xxxx-sf.cif SG
## where xxxx is the PDB code and SG is the spacegroup

## example ##
## ./extract_pandda.sh 5rvp-sf.cif C2

# take input from the command line
cif=${1}
cif_new=${cif:0:7}
sym=${2}

# splits the cif into two parts, XXXX-sf_data has the refinedl data and the original data, and XXXX-sf_pandda has the PanDDA event map coefficients
python split_cif.py ${cif}

# now convert the split cifs into mtzs
phenix.cif_as_mtz ${cif_new}_data.cif --symmetry=${sym} > ${cif_new}_data.log
phenix.cif_as_mtz ${cif_new}_pandda.cif --symmetry=P1 > ${cif_new}_pandda.log
