extract_pandda_from_cif
======================

### Author:

Galen Correy

### Summary:

The script extracts the ligand-bound state from multi-state PDB files. The script removes the altloc records for residues that only have a single conformation modeled in the ligand-bound state and renames the altloc records for residues with multiple conformations. 

### Example usage:

```bash
pymol -qc extract_ligand-bound_state.py pdb_list.txt
```
where pdb_list.txt contains a list of PDB codes to be fetched/extracted. For example:
```
5SQP
5SQQ
```

### Expected output:

XXXX_ligand-bound_state.pdb, where XXXX is a PDB code. 

### Software requirements:

PyMOL version 2.5.1
