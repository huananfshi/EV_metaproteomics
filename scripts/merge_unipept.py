#!/usr/bin/env python
import os
path = '/Users/huananshi/Documents/Graduate_school/EV_proteomics/'
f = []
for file in os.listdir(path+'intermediate'):
    mpa = pd.read_csv(path+'intermediate/'+file,header=0,index_col=None)
    mpa.rename(columns=({'PeakArea':file.split('_')[0]}),inplace=True)
    f.append(mpa)
for i in range(len(f)):
    cols = f[i].columns.values.tolist()[0:-1]
    f[i][cols]=f[i][cols].astype(str)

f_merged = f[0]
colnames = f_merged.columns.values.tolist()[0:-1]
for i in range(1,len(f)):
    f_merged = pd.merge(f_merged,f[i],on=colnames,how='outer')

f_merged[f_merged.columns[-12:]] = f_merged[f_merged.columns[-12:]].fillna(0)
f_merged = f_merged.replace('nan',np.nan)
f_merged = f_merged.drop(f_merged.columns[f_merged.isna().sum()>=f_merged.shape[0]],axis=1)
f_merged.to_csv(path+'intermediate/unipept_merged.csv',index=False)
