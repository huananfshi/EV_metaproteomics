#!/bin/bash
path=/Users/huananshi/Documents/Graduate_school/EV_proteomics/
path_raw=$path/MS_quant
db_path_rno=$path/rno6.dmnd
db_path_uniref90=/opt/anaconda3/envs/py2/bin/uniref90/uniref/uniref90_201901b_full.dmnd #from humann_database
diamond_output_path=$path/diamond_output
unipept_output=$path/Unipept


#MS quant file frocessing
cd $path_raw
for file in `ls`; do Rscript ../scripts/fasta_processing.R $path_raw $file; done

#remove host sequences
for fasta_file in `ls *fasta`;
do diamond blastp -q $fasta_file -d $db_path_rno -p=4 -o $diamond_output_path/${fasta_file%.fasta}_rat.tsv \
--outfmt 6 --fast --unal 1 --un $diamond_output_path/${fasta_file%.fasta}_rno_removed.fasta;
done

#match MGX uniref90 database
cd $diamond_output_path
for file_rno in `ls *_rno_removed.fasta`;
do diamond blastp -q $file_rno -d $db_path_uniref90 -p=4 -o ${file_rno%.fasta}_uniref90.tsv \
--outfmt 6 --evalue 0.001 --top 1 --query-cover 80 --very-sensitive;
done

#filter sequences for unipept
cd $path_raw
for file_peptide in `ls -d *.csv`;
do sample=${file_peptide%_quant.csv};
python3 ../scripts/fasta_filter.py $file_peptide $diamond_output_path/${sample}_rno_removed_uniref90.tsv $unipept_output/${sample}_unipept.txt;
done
