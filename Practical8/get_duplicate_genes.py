import re
#open files and read them
seqlist = open('duplicate_genes.fa','w', encoding = 'utf-8')
gene = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
flag = False
clean = ''
sequence = ''
#read each line in the file, chack if there is 'duplication' in the line
for line in gene:
    if line.startswith('>'):
        if 'duplication' in line:
            flag = True
            clean = line.strip()
            gene_name = clean.split()[0][1:] 
            seqlist.write(f">{gene_name}\n")
        else:
            flag = False
            clean = ''
            sequence = ''
    elif flag == True:
        sequence += line.strip()
        seqlist.write(line)