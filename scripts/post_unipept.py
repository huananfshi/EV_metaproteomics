#!/usr/bin/env python
import numpy as np
import pandas as pd
import sys
quant_file = sys.argv[1] # path to quant file
unipept_file = sys.argv[2] # path to unipept output (saved as csv with \t sep)
output_file = sys.argv[3] # output path/name to combined quant_unipept file
EV_peptides = pd.read_csv(quant_file,header=0,index_col=0)
EV_unipept = pd.read_csv(unipept_file,header=0,index_col=0,sep='\t')
EV_peptides = EV_peptides.groupby('plain_peptide').mean()
EV_unipept_quant = EV_unipept.join(EV_peptides,how='left')
EV_unipept_quant.to_csv(output_file)





    
