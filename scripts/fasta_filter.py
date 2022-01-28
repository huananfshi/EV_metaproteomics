#!/usr/bin/env python
import sys
import numpy as np
import pandas as pd
import requests
peptide_file = sys.argv[1] #MS_Quant/*quant.csv file
diamond_file = sys.argv[2] #diamond_output/*_rno_removed.tsv file
output_file =  sys.argv[3] #output file for unipept
EV_peptides = pd.read_csv(peptide_file,header=0,index_col=0,usecols=[0,1])
EV_peptides_list = EV_peptides.to_dict()['plain_peptide']
EV_diamond = pd.read_csv(diamond_file,header=0,names=['qseqid', 'sseqid', 'pident','length', 'mismatch','gapopen', 'qstart', 'qend','sstart', 'send', 'evalue', 'bitscore'], sep='\t')
EV_diamond = EV_diamond.replace(EV_peptides_list)
EV_diamond_unique = EV_diamond['qseqid'].unique()
url = "http://api.unipept.ugent.be/api/v1/pept2lca"
EV_diamond_taxa = {}
for pept in EV_diamond_unique:
    r = requests.post(url,data={'input[]':pept,'equate_il':'true','names':'true','extra':'true'}).json()
    if r !=[] and r[0]['superkingdom_name']=='Bacteria':
        EV_diamond_taxa[pept] = r[0]['taxon_rank']+'_'+r[0]['taxon_name']
    else: EV_diamond_taxa[pept] = 'other'
EV_diamond['taxa']=EV_diamond['qseqid']
EV_diamond['taxa'] = EV_diamond['taxa'].replace(EV_diamond_taxa)
EV_diamond['taxa'].unique()
EV_bac=[]
for key, values in EV_diamond_taxa.items():
    if values != 'other':
        EV_bac.append(key)

np.savetxt(output_file,EV_bac,fmt='%s')
