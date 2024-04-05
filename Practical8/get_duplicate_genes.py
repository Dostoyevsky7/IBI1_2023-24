import re   
seqlist = open('duplicate_genes.fa','w')
genelist = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
gene = genelist.read()
#find put all the lines have the word'duplication', make it into one large string
find_dup = re.findall(r'.+duplication.+\n', gene)
split_dup = "".join(find_dup)
#find all the gene names in it
find_name = re.findall(r">([^']+?_mRNA)", split_dup)
#the names allhave the format"'>YXXXXX", delete the single quotation "'"
cleaned_names = [name.replace("'", "") for name in find_name]
#write name and sequence into the file 
for cleaned_name in cleaned_names:    
    match = re.search(rf">({cleaned_name})_mRNA\n([^>]+)", gene)  
    if match:  
        seqlist.write(f">{cleaned_name}_mRNA\n{match.group(2)}\n")