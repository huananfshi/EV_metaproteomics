#!/bin/bash
#combine quant file with unipept output
path=/Users/huananshi/Documents/Graduate_school/EV_proteomics/MS_quant
unipept_output=/Users/huananshi/Documents/Graduate_school/EV_proteomics/Unipept
output_path=/Users/huananshi/Documents/Graduate_school/EV_proteomics/intermediate

cd $unipept_output
for unipept_file in `ls -d *.csv`;
do python3 ../scripts/post_unipept.py $path/GutEV_${unipept_file%_mpa.csv}_quant.csv \
$unipept_file $output_path/${unipept_file%.csv}_quant.csv;
done
