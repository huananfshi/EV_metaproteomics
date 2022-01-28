args = commandArgs()
setwd(args[6])
raw_file_name = args[7]
raw_file = read.csv(raw_file_name, header = T, sep = '\t',stringsAsFactors = F)
file_quant = raw_file[c('plain_peptide','PeakArea')]
fasta_header = vector(dim(file_quant)[1],mode = "character")

for (i in 1: dim(file_quant)[1]){
  fasta_header[i] = paste(">Peptide",i,sep = "")
  rownames(file_quant)[i]=paste("Peptide",i,sep = "")
}
peptide_seq = file_quant[,'plain_peptide']
peptide_fasta = c(rbind(fasta_header,peptide_seq))
file_name = paste(unlist(strsplit(raw_file_name,'_'))[5],unlist(strsplit(raw_file_name,'_'))[6],sep = '_')
write(peptide_fasta,paste(file_name,'.fasta',sep=''))
write.csv(file_quant,paste(file_name,'_quant.csv',sep=''))
