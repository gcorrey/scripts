import sys,os,math
import numpy as np
from pymol import cmd, util
from pymol.cgo import *

cmd.feedback("disable","all","details")

print("####")
print("Run script using: pymol -qc extract_ligand-bound_state.py pdb_list.txt, where pdb_list.txt contains a list of PDBs e.g.")
print("7KQO")
print("7KQP")
print("...")
print("#####")

if len(sys.argv) > 3:
    pdb_list = sys.argv[3]
    
    # Read the list of PDB codes
    with open('./'+pdb_list,'r') as f:
        for line in f:
            ## read in the PDB code ##
            line_strip = line.strip()
            pdb = line_strip

            # fetch the coordinates from the PDB
            cmd.fetch(pdb)

            ## select the ligand bound state ##
            cmd.select(pdb+"_prot_wat","("+pdb+" and not alt A and not resn HOH) or ("+pdb+" and resn HOH and not alt A)")

            ## create a new model ##
            cmd.create(pdb+"_ligand-bound",pdb+"_prot_wat")

            ## for each residue, alter altlocs if needed ##
            # chain A
            for resi in range(1,170):
                # check if the residue is present
                res = cmd.select("res",pdb+"_ligand-bound and chain A and resi "+str(resi))
                if res != 0:
                    # check if residue has alternative conformation modeled
                    resB = cmd.select("resB",pdb+"_ligand-bound and chain A and resi "+str(resi)+" and alt B and not resn HOH")
                    if resB != 0:
                        resC = cmd.select("resC",pdb+"_ligand-bound and chain A and resi "+str(resi)+" and alt C and not resn HOH")
                        # if there is only alt B, then change altloc empty e.g. ""
                        if resC == 0:
                            cmd.alter(pdb+"_ligand-bound and chain A and resi "+str(resi)+" and not resn HOH",'alt=""')
                        else:
                            cmd.alter(pdb+"_ligand-bound and chain A and resi "+str(resi)+" and alt B and not resn HOH",'alt="A"')
                            cmd.alter(pdb+"_ligand-bound and chain A and resi "+str(resi)+" and alt C and not resn HOH",'alt="B"')

            # chain B
            for resi in range(1,170):
                # check if the residue is present
                res = cmd.select("res",pdb+"_ligand-bound and chain B and resi "+str(resi))
                if res != 0:
                    # check if residue has alternative conformation modeled
                    resB = cmd.select("resB",pdb+"_ligand-bound and chain B and resi "+str(resi)+" and alt B and not resn HOH")
                    if resB != 0:
                        resC = cmd.select("resC",pdb+"_ligand-bound and chain B and resi "+str(resi)+" and alt C and not resn HOH")
                        # if there is only alt B, then change altloc empty e.g. ""
                        if resC == 0:
                            cmd.alter(pdb+"_ligand-bound and chain B and resi "+str(resi)+" and not resn HOH",'alt=""')
                        else:
                            cmd.alter(pdb+"_ligand-bound and chain B and resi "+str(resi)+" and alt B and not resn HOH",'alt="A"')
                            cmd.alter(pdb+"_ligand-bound and chain B and resi "+str(resi)+" and alt C and not resn HOH",'alt="B"')

            ## rename the ligand to match the protein ##
            # Most of the ligands have resids 201/202/203 - although some seem to be 301/302/303 - this is based on PDB renaming (and is outside of my control)
            lig_01 = cmd.select("lig_01",pdb+"_ligand-bound and resi 201+301 and not resn HOH and alt B")
            lig_02 = cmd.select("lig_02",pdb+"_ligand-bound and resi 202+302 and not resn HOH and alt C")
            lig_03 = cmd.select("lig_03",pdb+"_ligand-bound and resi 203+303 and not resn HOH and alt D")

            if lig_01 != 0 and lig_02 == 0 and lig_03 == 0:
                cmd.alter(pdb+"_ligand-bound and resi 201+202+203+301+302+303 and not resn HOH and alt B",'alt=""')
            if lig_01 != 0 and lig_02 != 0 and lig_03 == 0:
                cmd.alter(pdb+"_ligand-bound and resi 201+202+203+301+302+303 and not resn HOH and alt B",'alt="A"')
                cmd.alter(pdb+"_ligand-bound and resi 201+202+203+301+302+303 and not resn HOH and alt C",'alt="B"')
            if lig_01 != 0 and lig_02 != 0 and lig_03 != 0:
                cmd.alter(pdb+"_ligand-bound and resi 201+202+203+301+302+303 and not resn HOH and alt B",'alt="A"')
                cmd.alter(pdb+"_ligand-bound and resi 201+202+203+301+302+303 and not resn HOH and alt C",'alt="B"')
                cmd.alter(pdb+"_ligand-bound and resi 201+202+203+301+302+303 and not resn HOH and alt D",'alt="C"')

            # rename the waters
            wat_B = cmd.select("wat_B",pdb+"_ligand-bound and resn HOH and alt B")
            wat_C = cmd.select("wat_C",pdb+"_ligand-bound and resn HOH and alt C")
            wat_D = cmd.select("wat_D",pdb+"_ligand-bound and resn HOH and alt D")            

            if wat_B != 0:
                cmd.alter("wat_B",'alt=""')
            if wat_C != 0:
                cmd.alter("wat_C",'alt="B"')
            if wat_D != 0:
                cmd.alter("wat_D",'alt="C"')

            ## now re-order the atoms in the ligand_bound state ##
            cmd.sort(pdb+"_ligand-bound")

            # save the model
            cmd.save("./"+pdb+"_ligand-bound_state.pdb",pdb+"_ligand-bound")

            # reset
            cmd.delete("all")
            cmd.reinitialize()
            
    print("You can safely ignore the following error")
    print("####")
    print(" Error: unsupported file type: txt")
    print(" Error: Argument processing aborted due to exception (above).")
    print("####")
else:
    print("Error: you need to give a list of PDB codes")
    print("####")
