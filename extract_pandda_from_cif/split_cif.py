import sys,os,math

## this python script is called by the ./extract_pandda.sh script

## usage ##
## python modify_cif.py xxxx-sf.cif
## where xxxx-sf.cif is the cif file to be split into groups
## output will be xxxx-sf_data.cif and xxxx-sf_pandda.cif

cif = sys.argv[1]
cif_new = cif[0:7]
pdb = cif[0:4]

ref_data_block = 'data_r'+pdb+'sf' # the refined data block
pandda_block = 'data_r'+pdb+'Asf' # the PanDDA event map data block
ori_data_block = 'data_r'+pdb+'Bsf' # the 

block = 'data' # assume that the first block is the refined data
with open(cif_new+'_data.cif','w') as b1, open(cif_new+'_pandda.cif','w') as b2, open(cif,'r') as f1:
    for line in f1:        
        # find out which block the line is in
        if ref_data_block in line:
            block = 'data'
        elif pandda_block in line:
            block = 'pandda'
        elif ori_data_block in line:
            block = 'data'
        # now write out the line to seperate files
        if block == 'data':
            b1.write(line)
        elif block == 'pandda':
            b2.write(line)
                
