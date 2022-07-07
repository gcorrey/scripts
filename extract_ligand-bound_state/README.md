extract_pandda_from_cif
======================

### Author:

Galen Correy

### Summary:

The ./extract_pandda.sh script does two things.

1. Splits a multi data block CIF into two data blocks using the split_cif.py script (the refined data and the original data go into one CIF, and the PanDDA event map goes into the other).

2. Converts the split CIFs into MTZ format using phenix.cif_as_mtz

### Example usage:

```bash
./pandda_extract.sh xxxx-sf.cif sym
```
where xxxx is the PDB code for the cif, and sym is the crystal space group (e.g. P43)

### Expected output:

xxxx-sf_data.cif - CIF containing map coefficients from final refinement with ligand, as well as the original data
xxxx-sf_pandda.cif - CIF containing map coefficients from the PanDDA event map

xxxx-sf_data.mtz - MTZ file containing map coefficients from final refinement with ligand, as well as the original data
xxxx-sf_pandda.mtz - MTZ file containing map coefficients from the PanDDA event map

xxxx-sf_data.log - output from phenix.cif_as_mtz
xxxx-sf_pandda.log - output from phenix.cif_as_mtz

### Software requirements:

Python 3

Phenix dev-4338

